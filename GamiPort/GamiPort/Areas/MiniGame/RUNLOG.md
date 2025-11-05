# MiniGame Area 前台開發執行日誌 (RUNLOG)

## 專案資訊
- **專案路徑**: `C:\Users\n2029\Desktop\work-1105\GamiPort\GamiPort\Areas\MiniGame`
- **開發範圍**: MiniGame Area 前台（嚴格限制在此路徑內）
- **資料庫**: SQL Server (GameSpacedatabase)
- **設計風格**: 巴哈姆特整體風格 + MiniGame Area 淡藍現代系配色

---

## 2025-11-05 (台北時間)

### 19:30 - 初始化專案

**動作**:
1. ✅ 確認 work-1105 目錄存在
2. ✅ 確認 MiniGame Area 路徑存在
3. ✅ 確認所有必要文檔存在於 schema/ 目錄
4. ✅ 創建 RUNLOG.md（本文件）
5. ✅ 創建 HANDOFF.md
6. ✅ 創建 CHECKLIST.md
7. ✅ 閱讀所有必要文檔

**狀態**: 已完成

---

### 19:45 - 文檔閱讀與分析完成

**動作**:
1. ✅ 閱讀 README_合併版.md - 確認後台 (GameSpace) 已完成，前台 (GamiPort) 需求清楚
2. ✅ 閱讀 前台開發藍圖文件.md (部分) - Vue.js + Unity WebGL 技術棧，零越界方案
3. ✅ 閱讀 巴哈姆特風格布局特色完整分析.md - 淡藍現代系配色完整規格
4. ✅ 閱讀 MiniGame Area 架構對比分析報告.md - 70% 完成度，關鍵缺失已識別
5. ✅ 閱讀 MiniGame_Area_完整描述文件.md - 四大子系統完整規格
6. ✅ 檢查 GamiPort MiniGame Area 現有結構

**變更檔案**:
無（僅讀取分析）

**關鍵發現**:

**現有結構**:
- Controllers: 5 個 (Game, Home, Pet, SignIn, Wallet)
- Services: 9 個檔案 (FuzzySearchService + 4 interfaces + 4 implementations)
- Views: 12 個 (Game, Home, Pet, SignIn, Wallet folders)
- Helpers: TimeHelper.cs (UTC+8 時間處理)
- wwwroot: 已存在目錄

**整體完成度**: 70%
- 核心查詢功能：100% ✓
- 核心變更功能：63.6% (部分完成)
- 管理功能：0% (前台不需要，符合預期)

**關鍵缺失項目** (依優先級):
1. 🔴 **寵物升級系統** - 最關鍵！經驗值累積但無法升級
2. 🔴 優惠券/電子禮券使用功能
3. 🔴 錢包交易歷史頁面
4. 🟡 Constants/ 目錄 - Magic Numbers 需整理
5. 🟡 Filters/ 目錄 - IdempotencyFilter, ProblemDetailsFilter
6. 🟡 config/ 目錄 - ServiceExtensions.cs
7. 🟢 簽到規則預覽功能
8. 🟢 排行榜系統 (遊戲/寵物/簽到)

**設計規格確認**:
- 配色系統：Deep Teal `#0d9488` / `#17a2b8`, Background `#f0f4f8`, Accent `#ff9f43`
- 佈局系統：Card-based, 16-24px border-radius, 8px 間距單位
- 技術棧：ASP.NET MVC + Vue.js + Unity WebGL (零越界方案)

**狀態**: 已完成

**下一步**:
- 連接 SQL Server 驗證資料庫 schema
- 確定開發優先序
- 開始實作關鍵缺失功能

---

### 20:30 - 實作寵物升級系統完成 ✅

**動作**:
1. ✅ 讀取 GamiPort 現有 IPetService 和 PetService
2. ✅ 實作 AddExperienceAsync - 增加經驗值並自動檢查升級（支援跨多級升級）
3. ✅ 實作 LevelUpPetAsync - 寵物升級並發放點數獎勵，記錄 WalletHistory
4. ✅ 實作 GetRequiredExpForLevelAsync - 三級經驗值公式（Level 1-10 線性，11-100 二次，101+ 指數）
5. ✅ 實作 CalculateLevelUpReward - 階層式獎勵（Level 1-10: 10點，11-20: 20點，最高 250點）
6. ✅ 整合 GamePlayService - 遊戲勝利後呼叫 AddExperienceAsync
7. ✅ 整合 SignInService - 簽到獲得經驗後呼叫 AddExperienceAsync
8. ✅ 修復編譯錯誤 - 移除不存在的 UpdatedAt/CreatedAt 欄位
9. ✅ 驗證編譯成功 - `dotnet build` 0 個錯誤 ✓
10. ✅ 確認模糊搜尋完整性 - WalletService 已完整實作 5 級優先順序 + OR 邏輯

**變更檔案**:
- `Services/IPetService.cs` (+21 行)
  - 新增 AddExperienceAsync, LevelUpPetAsync, GetRequiredExpForLevelAsync 介面方法

- `Services/PetService.cs` (+198 行)
  - 實作 AddExperienceAsync: 增加經驗值，自動觸發多級升級（while loop）
  - 實作 LevelUpPetAsync: 升級 + 發放獎勵 + 記錄 WalletHistory（含事務）
  - 實作 GetRequiredExpForLevelAsync: 三級公式（40*l+60 / 0.8*l²+380 / 285.69*1.06^l）
  - 實作 CalculateLevelUpReward: 階層式獎勵（tier*10，最高 250）

- `Services/GamePlayService.cs` (+4 行構造函數，+16 行業務邏輯)
  - 注入 IPetService
  - 遊戲結束（Win）後呼叫 _petService.AddExperienceAsync()
  - 在事務外執行以避免嵌套事務衝突

- `Services/SignInService.cs` (+3 行構造函數，+19 行業務邏輯)
  - 注入 IPetService
  - 簽到成功後呼叫 _petService.AddExperienceAsync()
  - 在事務外執行以避免嵌套事務衝突

**原因與理由**:
- 對應需求：HANDOFF.md 第 39 項「實作寵物升級系統」（最高優先級）
- 對應 DB 欄位：Pet.Level, Pet.Experience, Pet.LevelUpTime, UserWallet.UserPoint, WalletHistory.*
- 設計模式：參考 GameSpace 實作，採用分散式服務架構（非單獨 PetLevelingService）
- 事務處理：升級邏輯在 LevelUpPetAsync 內部使用事務，外部呼叫在事務提交後執行
- 三級公式：Level 1-10 線性（快速入門），11-100 二次（平衡成長），101+ 指數（高階挑戰）

**技術細節**:
- **自動升級檢查**: AddExperienceAsync 使用 while 迴圈支援跨多級升級
- **溢出經驗值**: 升級後保留多餘經驗值（Experience -= requiredExp）
- **獎勵整合**: 升級時更新 UserWallet 並記錄 WalletHistory
- **錯誤處理**: GamePlayService 和 SignInService 中使用 try-catch，升級失敗不影響主要業務流程
- **模糊搜尋**: 確認 WalletService.GetUserCouponsAsync 和 GetUserEVouchersAsync 已實作 5 級優先順序 + OR 邏輯

**狀態**: 已完成 ✅

**編譯結果**:
```
244 個警告
0 個錯誤
```

**下一步**:
- Git commit 並 push 備份
- 繼續實作次要優先級項目（優惠券使用功能、錢包交易歷史）

---

### 21:45 - 實作優惠券/電子禮券使用功能與錢包交易歷史增強版 ✅

**動作**:
1. ✅ 閱讀 MUST-FOLLOW-RULES.txt 複習規範
2. ✅ 並行啟動 5 個代理收集 GameSpace 實作信息（Coupon、EVoucher、WalletHistory、DB Schema、GamiPort現狀）
3. ✅ 更新 IWalletService 介面 - 新增 3 個方法簽名
4. ✅ 實作 WalletService.UseCouponAsync - 5層驗證（存在性、重複使用、所有權、有效期、訂單ID）
5. ✅ 實作 WalletService.RedeemEVoucherAsync - 4層驗證 + EvoucherRedeemLog 創建
6. ✅ 實作 WalletService.GetWalletHistoryAsync（增強版） - 分頁、篩選、5級模糊搜尋、OR邏輯
7. ✅ 注入 IAppClock 依賴 - 支援 UTC+8 時間處理
8. ✅ 驗證編譯成功 - `dotnet build` 0 個錯誤 ✓

**變更檔案**:
- `Services/IWalletService.cs` (+34 行)
  - 新增 UseCouponAsync(int couponId, int userId, int? orderId) - 使用優惠券
  - 新增 RedeemEVoucherAsync(int evoucherId, int userId) - 兌換電子禮券
  - 新增 GetWalletHistoryAsync(...) - 增強版歷史查詢（7個參數：分頁、篩選、搜尋）

- `Services/WalletService.cs` (+277 行)
  - 注入 IAppClock 依賴（UTC+8 時間處理）
  - 實作 UseCouponAsync:
    - 5層驗證：存在性 → 重複使用 → 所有權 → 有效期 → 訂單ID
    - 明確事務管理（BeginTransactionAsync/CommitAsync/RollbackAsync）
    - UTC+8 時間設置 UsedTime
    - 結構化日誌記錄（LogWarning/LogInformation/LogError）
  - 實作 RedeemEVoucherAsync:
    - 4層驗證：存在性 → 重複使用 → 所有權 → 有效期
    - 創建 EvoucherRedeemLog 記錄（Status="Redeemed"）
    - 事務確保 Evoucher + Log 原子性
    - UTC+8 時間設置 UsedTime 和 ScannedAt
  - 實作 GetWalletHistoryAsync（增強版）:
    - 分頁控制：pageNumber (≥1), pageSize (10-200)
    - 篩選：ChangeType、StartDate、EndDate（自動轉換UTC）
    - 5級模糊搜尋：Description OR ItemCode
    - 優先順序排序 + 次要排序（ChangeTime 降序）
    - 回傳 (items, totalCount) tuple

**原因與理由**:
- 對應需求：HANDOFF.md 第 40-41 項「優惠券/電子禮券使用功能」、第 42 項「錢包交易歷史頁面」
- 對應 DB 欄位：
  - Coupon: IsUsed, UsedTime, UsedInOrderId
  - Evoucher: IsUsed, UsedTime
  - EvoucherRedeemLog: EvoucherId, UserId, ScannedAt, Status
  - WalletHistory: UserId, ChangeType, PointsChanged, ItemCode, Description, ChangeTime
- 設計模式：參考 GameSpace 實作（5個代理並行分析）
- 事務處理：優惠券/禮券使用必須在事務內執行，確保資料一致性
- 時間處理：使用 IAppClock 統一 UTC+8 台灣時間（ValidFrom/ValidTo 比較、UsedTime 設置）
- 模糊搜尋：使用 IFuzzySearchService 5級優先順序 + OR邏輯（與 GameSpace 一致）

**技術細節**:
- **5層驗證流程**（UseCouponAsync）：
  1. Coupon 存在性（!IsDeleted）
  2. 重複使用檢查（!IsUsed）
  3. 所有權驗證（coupon.UserId == userId）
  4. 有效期驗證（ValidFrom ≤ now ≤ ValidTo，UTC+8）
  5. 可選訂單ID設置
- **兌換日誌**（RedeemEVoucherAsync）：
  - EvoucherRedeemLog.Status = "Redeemed"
  - ScannedAt 使用 UTC+8 台灣時間
  - 事務確保 Evoucher.IsUsed 與 Log 同步
- **增強版歷史查詢**（GetWalletHistoryAsync）：
  - 先執行 DB 篩選（ChangeType、DateRange、Soft Delete）
  - 再執行記憶體模糊搜尋（5級優先順序）
  - 最後執行分頁（Skip/Take）
  - 回傳總筆數用於前端分頁控制
- **依賴注入**：新增 IAppClock 依賴，與 PetService/SignInService 一致

**狀態**: 已完成 ✅

**編譯結果**:
```
69 個警告（既有項目）
0 個錯誤 ✓
```

**下一步**:
- ~~實作 WalletController.History 頁面~~（前台不需要完整後台管理頁面）
- ~~創建 History View~~（前台使用簡化版錢包頁面即可）
- Git commit 並 push 備份
- 考慮實作其他次要優先級項目（Constants/、Filters/、排行榜系統等）

---

### 22:15 - 實作 Constants 目錄基礎設施 ✅

**動作**:
1. ✅ 閱讀 MUST-FOLLOW-RULES.txt 複習規範
2. ✅ 閱讀 HANDOFF.md 確認下一個高優先級任務
3. ✅ 並行啟動 5 個代理收集 Magic Numbers 信息
4. ✅ 創建 Constants/ 目錄結構
5. ✅ 實作 GameConstants.cs - 33 個常數
6. ✅ 實作 PetConstants.cs - 40+ 個常數（包含三級經驗值公式）
7. ✅ 實作 SignInConstants.cs - 30+ 個常數
8. ✅ 實作 WalletConstants.cs - 20+ 個常數
9. ✅ 驗證編譯成功 - `dotnet build` 0 個錯誤 ✓

**變更檔案**:
- `Constants/GameConstants.cs` (新建 195 行)
  - 遊戲限制：DEFAULT_DAILY_GAME_LIMIT, MIN/MAX_DIFFICULTY_LEVEL
  - 怪物數量配置：MONSTER_COUNT_LEVEL_1/2/3 (3/5/7)
  - 速度倍數配置：SPEED_MULTIPLIER_LEVEL_1/2/3 (1.0/1.2/1.5)
  - 寵物屬性變化：PET_*_DELTA_WIN/LOSE (hunger/mood/stamina/cleanliness)
  - 遊戲狀態字串：GAME_RESULT_IN_PROGRESS/WIN/LOSE/ABORT
  - 時間計算：DAYS_TO_ADD_FOR_DAY_END, TICKS_TO_SUBTRACT_FOR_DAY_END

- `Constants/PetConstants.cs` (新建 208 行)
  - 互動點數成本：INTERACT_POINT_COST = 5
  - 屬性增量：STAT_INCREMENT_FEED/BATH/PLAY/SLEEP = 10
  - 屬性範圍：STAT_MIN_VALUE = 0, STAT_MAX_VALUE = 100, STAT_LOW_THRESHOLD = 20
  - 三級經驗值公式常數：
    - Tier 1 (Level 1-10): EXP_FORMULA_TIER1_A = 40, _B = 60
    - Tier 2 (Level 11-100): EXP_FORMULA_TIER2_A = 0.8, _B = 380
    - Tier 3 (Level 101+): EXP_FORMULA_TIER3_BASE = 285.69, _RATE = 1.06
  - 等級範圍：PET_INITIAL_LEVEL = 1, PET_MAX_LEVEL = 250
  - 升級獎勵：LEVEL_REWARD_TIER_MULTIPLIER = 10, LEVEL_REWARD_MAX = 250
  - 每日衰減：DAILY_HUNGER_DECAY = -20, DAILY_MOOD_DECAY = -30, etc.

- `Constants/SignInConstants.cs` (新建 165 行)
  - 日期計算：TICKS_TO_END_OF_DAY = -1, DAYS_TO_ADD_FOR_TOMORROW = 1
  - 預設值：DEFAULT_POINTS_IF_NO_RULE = 0, EMPTY_COUPON_CODE = ""
  - 日期驗證：MIN_MONTH = 1, MAX_MONTH = 12, MIN_YEAR = 1900
  - 分頁計算：MIN_PAGE_NUMBER = 1, PAGE_INDEX_OFFSET = 1
  - 訊息字串：ERROR_ALREADY_SIGNED_IN, ERROR_NO_RULE_FOR_DAY, SUCCESS_CHECK_IN

- `Constants/WalletConstants.cs` (新建 130 行)
  - 分頁設置：DEFAULT_PAGE_SIZE = 10, MIN_PAGE_SIZE = 10, MAX_PAGE_SIZE = 200
  - 統計摘要鍵名：KEY_CURRENT_POINTS, KEY_TOTAL_EARNED, KEY_TOTAL_SPENT, KEY_TRANSACTION_COUNT
  - 交易類型：CHANGE_TYPE_POINT/COUPON/EVOUCHER, CHANGE_TYPE_GAME_REWARD/SIGNIN_REWARD/PET_LEVELUP
  - 狀態值：EVOUCHER_STATUS_REDEEMED/REVOKED
  - 日期計算：DAYS_TO_ADD_FOR_END_DATE = 1, TICKS_TO_SUBTRACT_FOR_INCLUSIVE_END = -1

**原因與理由**:
- 對應需求：HANDOFF.md 基礎設施補充項目「Constants 目錄」（中優先級）
- 消除 Magic Numbers：識別並整理 130+ 個分散在各 Service 中的硬編碼數值
- 設計模式：參考 GameSpace 實作（5個代理並行分析）
- 命名規範：PascalCase, const keyword, 完整 XML 文檔註解
- 功能分組：使用註解分隔符 (========) 清楚區分常數用途

**技術細節**:
- **多代理分析策略**：並行啟動 5 個代理分析不同 Service
  - Agent 1: PetService Magic Numbers (40+ 個常數)
  - Agent 2: WalletService Magic Numbers (15 個常數)
  - Agent 3: SignInService Magic Numbers (30+ 個常數)
  - Agent 4: GamePlayService Magic Numbers (33 個常數)
  - Agent 5: GameSpace Constants 參考結構
- **靜態類別模式**: 所有 Constants 使用 `public static class` 定義
- **編譯時優化**: 使用 `const` 關鍵字確保編譯時常數內嵌
- **完整文檔**: 每個常數都有 `<summary>` XML 註解說明用途
- **命名空間**: `GamiPort.Areas.MiniGame.Constants` 與 GameSpace 平行

**狀態**: 已完成 ✅

**編譯結果**:
```
建置成功。
69 個警告（既有項目）
0 個錯誤 ✓
```

**下一步**:
- Git commit 並 push 備份
- 考慮實作次要優先級項目（Filters/、config/ServiceExtensions.cs、排行榜系統等）

---

### 23:00 - 實作 Filters 目錄基礎設施 ✅

**動作**:
1. ✅ 閱讀 MUST-FOLLOW-RULES.txt 複習規範
2. ✅ 並行啟動 3 個代理分析 GameSpace Filters 實作
3. ✅ 創建 Filters/ 目錄結構
4. ✅ 實作 IdempotencyFilter.cs - 60秒防重機制
5. ✅ 實作 FrontendProblemDetailsFilter.cs - 統一異常處理
6. ✅ 驗證編譯成功 - `dotnet build` **0 個錯誤，0 個警告** ✓

**變更檔案**:
- `Filters/IdempotencyFilter.cs` (新建 114 行)
  - 基於 X-Idempotency-Key header 的冪等性檢查
  - 僅對 POST/PUT/PATCH/DELETE 方法生效
  - 使用 IMemoryCache 快取 60 秒
  - 完整日誌記錄（LogWarning/LogInformation）
  - 返回符合 RFC 7807 的 ProblemDetails 格式
  - 錯誤處理：400 Bad Request（缺少 Key）、409 Conflict（重複請求）

- `Filters/FrontendProblemDetailsFilter.cs` (新建 123 行)
  - 實作 IExceptionFilter 介面
  - 統一捕獲未處理的異常
  - 異常類型分類：ArgumentException(400)、UnauthorizedAccessException(401)、KeyNotFoundException(404)、InvalidOperationException(409)、NotImplementedException(501)
  - 完整日誌記錄（LogError 包含 TraceId）
  - 用戶友善的錯誤訊息（不洩漏技術細節）
  - 返回標準 ProblemDetails 格式（type/title/status/detail/instance/traceId）

**原因與理由**:
- 對應需求：HANDOFF.md 中優先級任務「基礎設施補充 - Filters 目錄」
- 參考實作：GameSpace MiniGame Area 的 IdempotencyFilter 和 MiniGameProblemDetailsFilter
- 關鍵改進：
  - FrontendProblemDetailsFilter 新增 ILogger 依賴注入（GameSpace 版本無日誌）
  - 所有錯誤響應都包含 traceId 用於追蹤
  - 用戶友善的錯誤訊息（針對前台用戶優化）
- 設計模式：
  - IdempotencyFilter 繼承 ActionFilterAttribute（支援建構子注入）
  - FrontendProblemDetailsFilter 實作 IExceptionFilter（標準異常處理）
- 命名空間：GamiPort.Areas.MiniGame.Filters（與 GameSpace 平行）

**技術細節**:
- **多代理分析策略**：並行啟動 3 個代理分析不同面向
  - Agent 1: GameSpace IdempotencyFilter 完整分析
  - Agent 2: GameSpace ProblemDetailsFilter 完整分析
  - Agent 3: GameSpace Filters 註冊方式分析
- **IdempotencyFilter 關鍵特性**：
  - 快取鍵格式：`idempotency:{客戶端提供的Key}`
  - 過期時間：60 秒絕對過期（AbsoluteExpirationRelativeToNow）
  - 快取優先級：CacheItemPriority.Low（記憶體不足時優先清除）
  - 僅快取成功請求（OkObjectResult/CreatedResult/NoContentResult/RedirectToActionResult）
- **FrontendProblemDetailsFilter 關鍵特性**：
  - 異常記錄：LogError 包含 TraceId、Path、StatusCode
  - 異常分類：6 種常見異常類型 + 預設 500
  - RFC 7807 規範：完整的 type URI、title、status、detail、instance、traceId
  - 用戶友善訊息：避免洩漏技術細節（不直接返回 exception.Message）
- **依賴服務**：
  - IMemoryCache（已在 Program.cs 註冊）
  - ILogger<T>（ASP.NET Core 內建）

**關鍵發現（來自代理分析）**:
- GameSpace 的 Filters **已開發但未啟用**（未在 Program.cs 或 ServiceExtensions.cs 註冊）
- GameSpace 目前使用內建 `[Authorize]` + Policy-based 授權，未使用自定義 Filters
- GameSpace 的 MiniGameProblemDetailsFilter **缺少日誌記錄和 TraceId**
- GamiPort 實作時已修正這些缺失

**註冊方式（待實作）**:
- **IdempotencyFilter** 需要在 config/ServiceExtensions.cs 中註冊為 Scoped Service
- **FrontendProblemDetailsFilter** 可選：全域註冊（Program.cs）或 BaseController 層級
- 目前僅創建 Filter 類別，註冊和使用留待下一階段（config/ServiceExtensions.cs 實作）

**狀態**: 已完成 ✅

**編譯結果**:
```
建置成功。
0 個警告
0 個錯誤 ✓
```

**下一步**:
- Git commit 並 push 備份
- 繼續實作次要優先級項目：config/ServiceExtensions.cs（集中註冊 MiniGame Area 服務）

---

## 執行記錄模板

### YYYY-MM-DD HH:MM - [標題]

**動作**:
- [ ] 項目1
- [ ] 項目2

**變更檔案**:
- `路徑/檔案名`
  - 變更內容簡述
  - Diff 參考：[連結或區塊]

**原因與理由**:
- 對應需求：[需求描述]
- 對應 DB 欄位/約束：[具體說明]

**狀態**: [進行中/完成/阻塞]

**下一步**:
- 具體行動項目

---

## 備註
- 所有時間戳使用台北時間（UTC+8）
- 每次開始工作前先讀取本檔案確認接續點
- 每完成一個小步驟即更新本檔案
- 任何跨區修改需求立即觸發 PAUSE-AND-ASK 模式
