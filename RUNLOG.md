# RUNLOG - GamiPort MiniGame Area 開發日誌

> 所有時間均為台北時間 (UTC+8)

---

## 2025-11-07 14:00 - 緊急Bug修復（14項問題）

### 背景
繼續前次會話，完成Pet/Index UI重構後，收到用戶提供的14個關鍵bug報告（圖1-14），需SUPER URGENT修復。

### 執行策略
採用多重平行agents策略，啟動7個diagnostic agents同時診斷問題，然後2個implementation agents並行實作複雜功能。

### 問題清單與解決狀態

#### ✅ 已完成 - 簡單修復（圖1-2, 3-5, 6, 9-10, 13-14）

**圖1: 遊戲開始按鈕錯誤**
- 問題：點擊「開始遊戲」導航到錯誤頁面
- 原因：表單提交與JavaScript AJAX衝突
- 解決：移除form包裝，改用直接onclick事件
- 檔案：`Views/Game/Index.cshtml` 第627-632行

**圖2: 取消按鈕確認對話框**
- 問題：取消按鈕顯示確認對話框
- 解決：創建新的cancelGame()函數，直接導航到`/MiniGame/Pet`
- 檔案：`Views/Game/Index.cshtml` 第917-920行

**圖3-5: 寵物互動顯示邏輯不完整**
- 問題：缺少詳細的互動反饋訊息
- 解決：實作完整訊息建構邏輯：
  - 顯示各屬性值變化（飢餓值+10等）
  - 健康值回復訊息
  - 每日首次全滿獎勵提示（100經驗+100點數）
  - 特殊訊息（屬性已滿時的提示）
- 檔案：`Views/Pet/Index.cshtml` 第1175-1242行

**圖6: 優惠券數字格式化**
- 問題：優惠券數字顯示為小數；標籤文字錯誤
- 解決：強制轉換為整數顯示；Percent類型顯示「折抵比率」
- 檔案：`Views/Wallet/Coupons.cshtml` 第544-586行

**圖9: 非CPN-優惠券過濾**
- 問題：測試數據優惠券顯示在前台
- 解決：在Service和View層添加`.StartsWith("CPN-")`過濾
- 檔案：
  - `Services/WalletService.cs` 第76, 169, 810-815行
  - `Views/Wallet/Coupons.cshtml`
  - `Views/SignIn/History.cshtml` 第72-79行

**圖10: 文字標籤修正**
- 問題：標籤文字不夠明確
- 解決：「當前經驗」→「當前經驗值」；「升級需求」→「升級所須經驗值」
- 檔案：`Views/Pet/Index.cshtml`

**圖13-14: UTC+8時間顯示**
- 問題：錢包更新時間未顯示UTC+8
- 原因：雙重轉換（ToAppTime後又ToUtc8String）
- 解決：直接使用.ToString()因lastUpdated已是UTC+8
- 檔案：`Views/Wallet/Index.cshtml` 第11-12, 43行

**圖12: 優惠券兌換失敗（CSRF修復）**
- 問題：優惠券兌換持續失敗
- 原因：隱藏表單可能未正確渲染CSRF token
- 解決：改用visible div容器，添加token驗證邏輯
- 檔案：`Views/Wallet/Exchange.cshtml` 第10-12, 235-244行

#### ✅ 已完成 - 複雜功能實作

**圖11: Wallet History交易記錄完整性**
- 問題：缺少2473筆簽到記錄、1159筆遊戲獎勵記錄、優惠券/電子禮券使用記錄
- 解決策略：在各Service的獎勵發放/使用邏輯中添加WalletHistory記錄
- 實作內容：
  1. **SignInService.cs (第142-230行)**
     - 添加簽到點數獎勵記錄（SIGNIN-DAILY/CONSECUTIVE-7/MONTHLY-PERFECT）
     - 添加簽到優惠券獎勵記錄
  2. **GamePlayService.cs (第248-311行)**
     - 添加遊戲勝利點數獎勵記錄（GAME-STAGE-1/2/3）
     - 添加第3關優惠券獎勵記錄
  3. **WalletService.cs**
     - UseCouponAsync (第321-351行)：添加優惠券使用記錄
     - RedeemEVoucherAsync (第425-462行)：添加電子禮券核銷記錄
- 技術細節：
  - 使用IAppClock.ToAppTime獲取UTC+8時間
  - 所有記錄在既有transaction內創建
  - 完整審計字段（CreatedBy, CreatedAt, IsDeleted）

**圖7-8: Pet Customize購買/套用完整邏輯**
- 問題：
  - 背景預覽不工作（顯示紫色）
  - 0點項目無法套用
  - 缺少購買狀態追蹤
  - 按鈕文字不隨擁有狀態變化
  - 無購買成功彈窗
  - 可重複購買
  - 取消按鈕行為錯誤
- 解決策略：使用WalletHistory追蹤購買狀態（不修改DB schema）
  - 膚色購買：ItemCode="{UserId}-{ColorHex}", ChangeType="PetSkinColor"
  - 背景購買：ItemCode="{UserId}-{BackgroundCode}", ChangeType="PetBackground"
- 實作內容：
  1. **PetService.cs (第760-1298行)**
     - `GetPurchasedSkinColorsAsync()` - 獲取已購買膚色列表
     - `GetPurchasedBackgroundsAsync()` - 獲取已購買背景列表
     - `CheckSkinColorPurchasedAsync()` - 檢查膚色購買狀態（0點視為已購買）
     - `CheckBackgroundPurchasedAsync()` - 檢查背景購買狀態（0點視為已購買）
     - `PurchaseSkinColorAsync()` - 購買膚色（扣點、防重購、創建記錄）
     - `PurchaseBackgroundAsync()` - 購買背景（扣點、防重購、創建記錄）
     - `ApplySkinColorAsync()` - 套用已購買膚色（不扣點）
     - `ApplyBackgroundAsync()` - 套用已購買背景（不扣點）
  2. **PetController.cs (第117-130, 283-457行)**
     - 修改Customize() - 傳遞已購買項目數據到View
     - 新增6個API endpoints：
       - `[HttpGet] CheckSkinColorOwnership` - 查詢膚色擁有狀態
       - `[HttpGet] CheckBackgroundOwnership` - 查詢背景擁有狀態
       - `[HttpPost] PurchaseSkinColor` - 執行膚色購買
       - `[HttpPost] ApplySkinColor` - 執行膚色套用
       - `[HttpPost] PurchaseBackground` - 執行背景購買
       - `[HttpPost] ApplyBackground` - 執行背景套用
  3. **Views/Pet/Customize.cshtml (第3-13, 428-862行)**
     - 頁面載入時讀取purchasedSkinColors/purchasedBackgrounds
     - 為所有選項添加isOwned屬性
     - 修改初始化函數顯示「已擁有」/「目前套用」標籤
     - 修改選擇函數動態更新按鈕文字（「確認購買 $X」vs「套用」）
     - 重寫確認按鈕handlers實作完整購買→套用流程
     - 新增showPurchaseSuccessModal()顯示購買詳情
     - 修改取消按鈕直接返回寵物頁面
- 購買/套用流程：
  1. 未擁有項目：點擊→顯示「確認購買 $X」→購買（扣點+創建記錄）→自動套用→彈窗顯示詳情→更新按鈕為「套用」
  2. 已擁有項目：點擊→顯示「套用」→直接套用（不扣點）
  3. 0點項目：視為已購買，直接顯示「套用」按鈕

### 技術亮點
1. **多重平行處理**：7個診斷agents + 2個實作agents同時運行
2. **零資料庫修改**：使用WalletHistory的ChangeType/ItemCode欄位追蹤購買狀態
3. **交易保護**：所有金額操作使用transaction確保原子性
4. **時間統一**：全域使用IAppClock確保UTC+8一致性
5. **防禦性編程**：防重複購買、0點特殊處理、完整錯誤處理

### 編譯結果
```
dotnet build --no-incremental
82 個警告
0 個錯誤
經過時間 00:00:04.69
```
✅ 成功 - 所有警告為既有的nullable和平台兼容性警告

### 修改檔案總覽
**Services層 (4個檔案)**
- `Services/SignInService.cs` - 添加簽到獎勵WalletHistory記錄
- `Services/GamePlayService.cs` - 添加遊戲獎勵WalletHistory記錄
- `Services/WalletService.cs` - 添加優惠券/電子禮券使用記錄
- `Services/PetService.cs` - 添加8個新方法處理購買/套用邏輯

**Controllers層 (1個檔案)**
- `Controllers/PetController.cs` - 修改Customize action，新增6個API endpoints

**Views層 (7個檔案)**
- `Views/Game/Index.cshtml` - 修復開始/取消按鈕
- `Views/Pet/Index.cshtml` - 完整互動邏輯、文字修正
- `Views/Pet/Customize.cshtml` - 完整購買/套用流程重寫
- `Views/Wallet/Index.cshtml` - UTC+8時間修正
- `Views/Wallet/Coupons.cshtml` - 數字格式化、CPN-過濾
- `Views/Wallet/Exchange.cshtml` - CSRF token修復
- `Views/SignIn/History.cshtml` - CPN-過濾

**總計**：12個檔案修改，涵蓋14個bug修復

### 下一步
- ✅ 更新RUNLOG.md（本檔案）
- ⏳ 更新HANDOFF.md
- ⏳ 更新CHECKLIST.md
- ⏳ Git commit並push到dev分支

---

## 歷史記錄

### 2025-11-06 18:00 - Pet/Index UI重構
- 完成Pet頁面UI優化
- Git commit: debee01
- 詳細記錄見前次會話

---

**記錄維護者**: Claude Code
**最後更新**: 2025-11-07 14:15 (UTC+8)
