using GamiPort.Infrastructure.Security;
using GamiPort.Infrastructure.Time;
using GamiPort.Models;
using Microsoft.EntityFrameworkCore;

namespace GamiPort.Areas.MiniGame.Services
{
	/// <summary>
	/// 寵物服務實現 (GamiPort 前台)
	/// </summary>
	public class PetService : IPetService
	{
		private readonly GameSpacedatabaseContext _context;
		private readonly IAppClock _appClock;

		// 互動點數成本配置
		private const int INTERACT_POINT_COST = 5;

		public PetService(GameSpacedatabaseContext context, IAppClock appClock)
		{
			_context = context;
			_appClock = appClock;
		}

		/// <summary>
		/// 獲取用戶寵物信息
		/// </summary>
		public async Task<Pet?> GetUserPetAsync(int userId)
		{
			return await _context.Pets
				.AsNoTracking()
				.FirstOrDefaultAsync(p => p.UserId == userId && !p.IsDeleted);
		}

		/// <summary>
		/// 執行寵物互動（餵食/洗澡/玩耍/睡覺）
		/// </summary>
		public async Task<PetInteractionResult> InteractWithPetAsync(int userId, string action)
		{
			// 獲取用戶的寵物
			var pet = await _context.Pets
				.FirstOrDefaultAsync(p => p.UserId == userId && !p.IsDeleted);

			if (pet == null)
			{
				return new PetInteractionResult
				{
					Success = false,
					Message = "未找到寵物信息"
				};
			}

			// 檢查寵物健康狀態 - 任一屬性為0時無法互動
			if (pet.Hunger == 0 || pet.Mood == 0 || pet.Stamina == 0 ||
				pet.Cleanliness == 0 || pet.Health == 0)
			{
				return new PetInteractionResult
				{
					Success = false,
					Message = "寵物狀態不佳，無法進行互動"
				};
			}

			// 檢查用戶錢包是否有足夠點數
			var wallet = await _context.UserWallets
				.FirstOrDefaultAsync(w => w.UserId == userId && !w.IsDeleted);

			if (wallet == null || wallet.UserPoint < INTERACT_POINT_COST)
			{
				return new PetInteractionResult
				{
					Success = false,
					Message = "會員點數不足，無法進行互動"
				};
			}

			// 開啟事務
			using var transaction = await _context.Database.BeginTransactionAsync();
			try
			{
				// 根據互動類型修改寵物屬性（鉗位到 0-100）
				// 商業規則用詞：餵食/洗澡/哄睡/休息
				var actionLower = action?.ToLower() ?? string.Empty;
				switch (actionLower)
				{
					case "feed":
						// 餵食：飢餓值增加10
						pet.Hunger = Math.Max(0, Math.Min(pet.Hunger + 10, 100));
						break;
					case "bath":
						// 洗澡：清潔值增加10
						pet.Cleanliness = Math.Max(0, Math.Min(pet.Cleanliness + 10, 100));
						break;
					case "comfort":
					case "play": // 向後兼容，但建議使用 comfort
						// 哄睡：心情值增加10
						pet.Mood = Math.Max(0, Math.Min(pet.Mood + 10, 100));
						break;
					case "rest":
					case "sleep": // 向後兼容，但建議使用 rest
						// 休息：體力值增加10
						pet.Stamina = Math.Max(0, Math.Min(pet.Stamina + 10, 100));
						break;
					default:
						await transaction.RollbackAsync();
						return new PetInteractionResult
						{
							Success = false,
							Message = "無效的互動類型（有效值：feed/bath/comfort/rest）"
						};
				}

				// 商業規則：全滿回復
				// 當飢餓、心情、體力、清潔四項值均達到 100 時，寵物健康值恢復至 100
				string bonusMessage = "";
				if (pet.Hunger == 100 && pet.Mood == 100 &&
					pet.Stamina == 100 && pet.Cleanliness == 100)
				{
					pet.Health = 100;

					// 商業規則：每日狀態全滿獎勵
					// 寵物若於每日首次同時達到飢餓、心情、體力、清潔值皆 100，則額外獲得 100 點寵物經驗值
					var today = _appClock.ToAppTime(_appClock.UtcNow).Date; // UTC+8
					var todayItemCode = $"PET-FULLSTATS-{today:yyyy-MM-dd}";

					// 檢查今日是否已發放全滿獎勵
					var alreadyGrantedToday = await _context.WalletHistories
						.AnyAsync(w => w.UserId == userId
									&& w.ItemCode == todayItemCode
									&& !w.IsDeleted);

					if (!alreadyGrantedToday)
					{
						// 讀取獎勵配置（預設 100 經驗值、0 點數）
						int bonusExp = 100; // 商業規則：每日狀態全滿獎勵 +100 經驗值
						int bonusPoints = 100; // 商業規則：每日狀態全滿獎勵 +100 點會員點數

						// 發放寵物經驗值
						pet.Experience += bonusExp;

						// 檢查升級（內嵌升級邏輯，避免重複事務）
						var requiredExp = await GetRequiredExpForLevelAsync(pet.Level + 1);
						while (pet.Experience >= requiredExp && requiredExp > 0)
						{
							// 執行升級
							pet.Level++;
							pet.LevelUpTime = _appClock.UtcNow;
							pet.Experience -= requiredExp; // 保留溢出經驗值

							// 計算升級獎勵
							var pointsReward = CalculateLevelUpReward(pet.Level);
							wallet.UserPoint += pointsReward;

							// 記錄升級獎勵到錢包歷史
							_context.WalletHistories.Add(new WalletHistory
							{
								UserId = userId,
								ChangeType = "Pet",
								PointsChanged = pointsReward,
								ItemCode = $"PET_LEVELUP_{pet.Level}",
								Description = $"寵物升級至 Level {pet.Level}",
								ChangeTime = _appClock.UtcNow,
								IsDeleted = false
							});

							// 檢查下一級
							requiredExp = await GetRequiredExpForLevelAsync(pet.Level + 1);
						}

						// 發放會員點數（如果有配置）
						if (bonusPoints > 0)
						{
							wallet.UserPoint += bonusPoints;
						}

						// 記錄到 WalletHistory（用於防重複發放全滿獎勵）
						var historyRecord = new WalletHistory
						{
							UserId = userId,
							ChangeType = "Point",
							PointsChanged = bonusPoints,
							ItemCode = todayItemCode,
							Description = $"寵物狀態全滿獎勵（經驗值+{bonusExp}，點數+{bonusPoints}）",
							ChangeTime = _appClock.UtcNow,
							IsDeleted = false
						};
						_context.WalletHistories.Add(historyRecord);

						bonusMessage = $" | 🎉 首次達成今日狀態全滿！獲得額外 {bonusExp} 經驗值和 {bonusPoints} 點數！";
					}
				}

				// 扣除會員點數（鉗位確保不為負）
				wallet.UserPoint = Math.Max(0, wallet.UserPoint - INTERACT_POINT_COST);

				// 保存更改
				_context.Pets.Update(pet);
				_context.UserWallets.Update(wallet);
				await _context.SaveChangesAsync();
				await transaction.CommitAsync();

				return new PetInteractionResult
				{
					Success = true,
					Message = $"互動成功！消耗{INTERACT_POINT_COST}點點數{bonusMessage}",
					Pet = pet
				};
			}
			catch (Exception ex)
			{
				await transaction.RollbackAsync();
				return new PetInteractionResult
				{
					Success = false,
					Message = $"互動失敗：{ex.Message}"
				};
			}
		}

		/// <summary>
		/// 更新寵物外觀（膚色和背景）
		/// </summary>
		public async Task<PetUpdateAppearanceResult> UpdatePetAppearanceAsync(int userId, string skinColor, string background)
		{
			// 獲取用戶的寵物
			var pet = await _context.Pets
				.FirstOrDefaultAsync(p => p.UserId == userId && !p.IsDeleted);

			if (pet == null)
			{
				return new PetUpdateAppearanceResult
				{
					Success = false,
					Message = "未找到寵物信息"
				};
			}

			// 獲取用戶錢包
			var wallet = await _context.UserWallets
				.FirstOrDefaultAsync(w => w.UserId == userId && !w.IsDeleted);

			if (wallet == null)
			{
				return new PetUpdateAppearanceResult
				{
					Success = false,
					Message = "錢包信息不存在"
				};
			}

			var totalPointCost = 0;
			var updateMessage = new List<string>();

			// 檢查膚色變更
			if (!string.IsNullOrWhiteSpace(skinColor) && pet.SkinColor != skinColor)
			{
				var skinSetting = await _context.PetSkinColorCostSettings
					.AsNoTracking()
					.FirstOrDefaultAsync(s => s.ColorCode == skinColor && !s.IsDeleted && s.IsActive);

				if (skinSetting == null)
				{
					return new PetUpdateAppearanceResult
					{
						Success = false,
						Message = "所選膚色不存在或不可用"
					};
				}

				totalPointCost += skinSetting.PointsCost;
				updateMessage.Add($"膚色：{skinSetting.ColorName}（{skinSetting.PointsCost}點）");
			}

			// 檢查背景變更
			if (!string.IsNullOrWhiteSpace(background) && pet.BackgroundColor != background)
			{
				var backgroundSetting = await _context.PetBackgroundCostSettings
					.AsNoTracking()
					.FirstOrDefaultAsync(s => s.BackgroundCode == background && !s.IsDeleted && s.IsActive);

				if (backgroundSetting == null)
				{
					return new PetUpdateAppearanceResult
					{
						Success = false,
						Message = "所選背景不存在或不可用"
					};
				}

				totalPointCost += backgroundSetting.PointsCost;
				updateMessage.Add($"背景：{backgroundSetting.BackgroundName}（{backgroundSetting.PointsCost}點）");
			}

			// 檢查是否有足夠點數
			if (totalPointCost > 0 && wallet.UserPoint < totalPointCost)
			{
				return new PetUpdateAppearanceResult
				{
					Success = false,
					Message = $"會員點數不足！需要{totalPointCost}點，目前擁有{wallet.UserPoint}點"
				};
			}

			// 如果沒有任何變更
			if (totalPointCost == 0)
			{
				return new PetUpdateAppearanceResult
				{
					Success = true,
					Message = "未進行任何變更",
					Pet = pet
				};
			}

			// 開啟事務
			using var transaction = await _context.Database.BeginTransactionAsync();
			try
			{
				var utcNow = _appClock.UtcNow;

				// 更新膚色
				if (!string.IsNullOrWhiteSpace(skinColor) && pet.SkinColor != skinColor)
				{
					pet.SkinColor = skinColor;
					pet.SkinColorChangedTime = utcNow;
				}

				// 更新背景
				if (!string.IsNullOrWhiteSpace(background) && pet.BackgroundColor != background)
				{
					pet.BackgroundColor = background;
					pet.BackgroundColorChangedTime = utcNow;
				}

				// 扣除點數
				wallet.UserPoint -= totalPointCost;

				// 保存更改
				_context.Pets.Update(pet);
				_context.UserWallets.Update(wallet);
				await _context.SaveChangesAsync();
				await transaction.CommitAsync();

				var message = $"定制成功！消耗{totalPointCost}點點數。更新項目：{string.Join("、", updateMessage)}";
				return new PetUpdateAppearanceResult
				{
					Success = true,
					Message = message,
					Pet = pet
				};
			}
			catch (Exception ex)
			{
				await transaction.RollbackAsync();
				return new PetUpdateAppearanceResult
				{
					Success = false,
					Message = $"定制失敗：{ex.Message}"
				};
			}
		}

		/// <summary>
		/// 修改寵物名稱
		/// </summary>
		public async Task<PetUpdateNameResult> UpdatePetNameAsync(int userId, string newName)
		{
			// 驗證名稱
			if (string.IsNullOrWhiteSpace(newName))
			{
				return new PetUpdateNameResult
				{
					Success = false,
					Message = "寵物名稱不能為空"
				};
			}

			// 名稱長度驗證（1-20字元）
			newName = newName.Trim();
			if (newName.Length < 1 || newName.Length > 20)
			{
				return new PetUpdateNameResult
				{
					Success = false,
					Message = "寵物名稱長度必須為 1-20 字元"
				};
			}

			// 獲取用戶的寵物
			var pet = await _context.Pets
				.FirstOrDefaultAsync(p => p.UserId == userId && !p.IsDeleted);

			if (pet == null)
			{
				return new PetUpdateNameResult
				{
					Success = false,
					Message = "未找到寵物信息"
				};
			}

			// 檢查名稱是否與當前名稱相同
			if (pet.PetName == newName)
			{
				return new PetUpdateNameResult
				{
					Success = true,
					Message = "名稱未變更",
					Pet = pet
				};
			}

			try
			{
				// 更新名稱
				pet.PetName = newName;

				// 保存更改
				_context.Pets.Update(pet);
				await _context.SaveChangesAsync();

				return new PetUpdateNameResult
				{
					Success = true,
					Message = "寵物名稱更新成功",
					Pet = pet
				};
			}
			catch (Exception ex)
			{
				return new PetUpdateNameResult
				{
					Success = false,
					Message = $"名稱更新失敗：{ex.Message}"
				};
			}
		}

		/// <summary>
		/// 獲取可用的膚色列表（包括所有11種，含限時活動限定已失效的）
		/// </summary>
		public async Task<IEnumerable<PetSkinColorCostSetting>> GetAvailableSkinsAsync()
		{
			return await _context.PetSkinColorCostSettings
				.AsNoTracking()
				.Where(s => !s.IsDeleted)
				.OrderBy(s => s.DisplayOrder)
				.ToListAsync();
		}

		/// <summary>
		/// 獲取可用的背景列表（包括所有11種，含限時活動限定已失效的）
		/// </summary>
		public async Task<IEnumerable<PetBackgroundCostSetting>> GetAvailableBackgroundsAsync()
		{
			return await _context.PetBackgroundCostSettings
				.AsNoTracking()
				.Where(s => !s.IsDeleted)
				.OrderBy(s => s.DisplayOrder ?? 0)
				.ToListAsync();
		}

		/// <summary>
		/// 增加寵物經驗值，並自動檢查升級
		/// </summary>
		public async Task<bool> AddExperienceAsync(int petId, int exp)
		{
			if (exp < 0)
			{
				return false;
			}

			var pet = await _context.Pets
				.FirstOrDefaultAsync(p => p.PetId == petId && !p.IsDeleted);

			if (pet == null)
			{
				return false;
			}

			// 增加經驗值
			pet.Experience += exp;

			// 自動檢查升級（支援跨多級升級）
			var requiredExp = await GetRequiredExpForLevelAsync(pet.Level + 1);
			while (pet.Experience >= requiredExp && requiredExp > 0)
			{
				// 執行升級
				var levelUpSuccess = await LevelUpPetAsync(petId);
				if (!levelUpSuccess)
				{
					break;
				}

				// 重新取得寵物資料
				pet = await _context.Pets
					.FirstOrDefaultAsync(p => p.PetId == petId && !p.IsDeleted);

				if (pet == null)
				{
					break;
				}

				// 檢查下一級
				requiredExp = await GetRequiredExpForLevelAsync(pet.Level + 1);
			}

			// 保存最終經驗值變更
			_context.Pets.Update(pet);
			await _context.SaveChangesAsync();

			return true;
		}

		/// <summary>
		/// 寵物升級並發放獎勵
		/// </summary>
		public async Task<bool> LevelUpPetAsync(int petId)
		{
			var pet = await _context.Pets
				.FirstOrDefaultAsync(p => p.PetId == petId && !p.IsDeleted);

			if (pet == null)
			{
				return false;
			}

			// 獲取當前等級所需經驗值
			var requiredExp = await GetRequiredExpForLevelAsync(pet.Level + 1);
			if (requiredExp == 0)
			{
				// 已達最高等級
				return false;
			}

			if (pet.Experience < requiredExp)
			{
				// 經驗值不足
				return false;
			}

			// 開啟事務
			using var transaction = await _context.Database.BeginTransactionAsync();
			try
			{
				var utcNow = _appClock.UtcNow;

				// 升級
				pet.Level++;
				pet.LevelUpTime = utcNow;
				pet.Experience -= requiredExp; // 保留溢出經驗值

				// 計算獎勵
				var pointsReward = CalculateLevelUpReward(pet.Level);

				// 更新用戶錢包
				var wallet = await _context.UserWallets
					.FirstOrDefaultAsync(w => w.UserId == pet.UserId && !w.IsDeleted);

				if (wallet != null)
				{
					wallet.UserPoint += pointsReward;

					// 記錄到錢包歷史
					_context.WalletHistories.Add(new WalletHistory
					{
						UserId = pet.UserId,
						ChangeType = "Pet",
						PointsChanged = pointsReward,
						ItemCode = $"PET_LEVELUP_{pet.Level}",
						Description = $"寵物升級至 Level {pet.Level}",
						ChangeTime = utcNow
					});
				}

				// 保存更改
				_context.Pets.Update(pet);
				if (wallet != null)
				{
					_context.UserWallets.Update(wallet);
				}
				await _context.SaveChangesAsync();
				await transaction.CommitAsync();

				return true;
			}
			catch
			{
				await transaction.RollbackAsync();
				return false;
			}
		}

		/// <summary>
		/// 獲取指定等級所需的經驗值（三級公式）
		/// </summary>
		public Task<int> GetRequiredExpForLevelAsync(int level)
		{
			if (level < 1)
			{
				return Task.FromResult(0);
			}

			if (level > 250)
			{
				// 超過250級視為最高等級
				return Task.FromResult(0);
			}

			// 三級經驗值公式
			if (level <= 10)
			{
				// Level 1-10: 線性公式
				// EXP = 40 * level + 60
				return Task.FromResult(40 * level + 60);
			}
			else if (level <= 100)
			{
				// Level 11-100: 二次公式
				// EXP = 0.8 * level^2 + 380
				return Task.FromResult((int)(0.8 * level * level + 380));
			}
			else
			{
				// Level 101+: 指數公式
				// EXP = 285.69 * (1.06 ^ level)
				return Task.FromResult((int)(285.69 * Math.Pow(1.06, level)));
			}
		}

		/// <summary>
		/// 計算升級獎勵（階層式獎勵）
		/// </summary>
		private int CalculateLevelUpReward(int level)
		{
			if (level < 1)
			{
				return 0;
			}

			if (level > 250)
			{
				return 250; // 最高獎勵250點
			}

			// 階層式獎勵：每10級一個階層，每個階層獎勵 +10 點
			// Level 1-10: +10 點
			// Level 11-20: +20 點
			// Level 21-30: +30 點
			// ...
			// Level 241-250: +250 點
			int tier = Math.Min((level - 1) / 10 + 1, 25);
			return tier * 10;
		}
	}
}
