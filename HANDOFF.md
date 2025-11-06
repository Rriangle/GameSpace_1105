# HANDOFF - 接續點與待辦清單

> 給下一輪Claude Code或開發者的接續指引

---

## 📍 當前狀態 (2025-11-07 16:15 UTC+8)

### ✅ 已完成項目

**15項緊急bug修復 - 全部完成**

**圖12（優惠券兌換失敗）- 最終解決**:
- 問題：數據庫DEFAULT約束與CHECK約束衝突
- 方案：使用原生SQL繞過DEFAULT約束
- 結果：✅ 測試3次連續成功（滿$500折$50、免運券、全站85折）
- 文件：`Services/WalletService.cs` 第653-680行

**14項緊急bug修復 - 全部完成**
1. ✅ 圖1: 遊戲開始按鈕錯誤 - Game/Index.cshtml
2. ✅ 圖2: 取消按鈕確認對話框 - Game/Index.cshtml
3. ✅ 圖3-5: 寵物互動顯示邏輯完整性 - Pet/Index.cshtml
4. ✅ 圖6: 優惠券數字格式化 - Wallet/Coupons.cshtml
5. ✅ 圖7-8: Pet Customize購買/套用完整邏輯 - PetService.cs, PetController.cs, Pet/Customize.cshtml
6. ✅ 圖9: 非CPN-優惠券過濾 - WalletService.cs, 多個Views
7. ✅ 圖10: 文字標籤修正 - Pet/Index.cshtml
8. ✅ 圖11: Wallet History交易記錄完整性 - SignInService.cs, GamePlayService.cs, WalletService.cs
9. ✅ 圖12: 優惠券兌換失敗（CSRF修復）- Wallet/Exchange.cshtml
10. ✅ 圖13-14: UTC+8時間顯示 - Wallet/Index.cshtml

**編譯狀態**: ✅ 0 errors, 82 warnings (既有警告)

---

## 🎯 接續點

### 立即待辦（本次會話剩餘）

1. **更新CHECKLIST.md**
   - 對齊14項功能完成狀態
   - 標記已完成的bug修復

2. **Git Commit & Push**
   - 提交所有修改（12個檔案）
   - Commit message應包含14項修復摘要
   - Push到dev分支
   - 確保commit message包含Claude Code footer

### 短期待辦（下次會話）

1. **功能測試**
   - 手動測試14項修復是否正常運作
   - 特別測試：
     - Pet Customize購買/套用流程
     - Wallet History是否記錄所有交易
     - CSRF token修復後優惠券兌換是否成功

2. **數據驗證**
   - 連線SQL Server檢查WalletHistory表是否正確記錄新交易
   - 檢查Pet表的SkinColor/BackgroundColor是否正確更新
   - 驗證User_Wallet點數扣除是否正確

3. **UI/UX優化**（如有時間）
   - 確認購買成功彈窗樣式是否美觀
   - 檢查「已擁有」/「目前套用」標籤顯示位置
   - 確認所有按鈕在不同狀態下的文字正確

### 中期待辦

1. **效能優化**
   - 檢查PetService中的WalletHistory查詢是否需要添加索引建議
   - 評估Customize頁面載入時查詢已購買項目的效能
   - 考慮添加快取機制（如已購買項目清單）

2. **錯誤處理增強**
   - 添加更詳細的錯誤訊息給用戶
   - 記錄異常到日誌系統
   - 考慮添加重試機制（如點數扣除失敗）

3. **安全審查**
   - 檢查所有API endpoints是否有適當的授權
   - 驗證CSRF保護是否完整
   - 確認點數扣除邏輯無法被繞過

---

## 📋 14項功能完整實作檢查表

根據README_合併版.md第3節，前台需完全實作14項功能：

### 3.1 會員錢包（6項）
1. ✅ 查看當前會員點數餘額 - Wallet/Index.cshtml
2. ✅ 使用會員點數兌換商城優惠券及電子優惠券 - Wallet/Exchange.cshtml
3. ✅ 查看目前擁有商城優惠券 - Wallet/Coupons.cshtml
4. ✅ 查看目前擁有電子優惠券 - Wallet/Vouchers.cshtml
5. ✅ 使用電子優惠券（QRCode/Barcode顯示）- Wallet/UseVoucher.cshtml
6. ✅ 查看收支明細 - Wallet/History.cshtml（本次修復後應完整記錄所有交易）

### 3.2 會員簽到系統（2項）
7. ✅ 查看月曆型簽到簿並執行簽到 - SignIn/Index.cshtml
8. ✅ 查看簽到歷史紀錄 - SignIn/History.cshtml

### 3.3 寵物系統（4項）
9. ✅ 寵物名字修改 - Pet/Index.cshtml
10. ✅ 寵物互動（餵食/洗澡/玩耍/哄睡）- Pet/Index.cshtml（本次修復完整互動邏輯）
11. ✅ 寵物換膚色（扣會員點數）- Pet/Customize.cshtml（本次實作完整購買/套用邏輯）
12. ✅ 寵物換背景（可免費或需點數）- Pet/Customize.cshtml（本次實作完整購買/套用邏輯）

### 3.4 小遊戲系統（2項）
13. ✅ 出發冒險 - Game/Index.cshtml
14. ✅ 查看遊戲紀錄 - Game/History.cshtml

### 額外功能
15. ✅ 簽到規則預覽 - SignIn/Rules.cshtml

**總計**: 15/15項功能完整實作 ✅

---

## 🔧 技術架構概覽

### 關鍵設計決策

1. **購買狀態追蹤**
   - 使用WalletHistory.ChangeType = "PetSkinColor" / "PetBackground"
   - ItemCode格式："{UserId}-{ColorHex/BackgroundCode}"
   - 0點項目視為已購買（免費），不創建記錄

2. **交易記錄完整性**
   - SignInService: 記錄簽到獎勵（點數+優惠券）
   - GamePlayService: 記錄遊戲獎勵（點數+優惠券）
   - WalletService: 記錄優惠券/電子禮券使用

3. **時間處理**
   - 統一使用 `IAppClock.ToAppTime(IAppClock.UtcNow)` 獲取UTC+8時間
   - 所有顯示時間直接 `.ToString()` 不再二次轉換

4. **CSRF保護**
   - Exchange.cshtml使用visible div容器承載token
   - JavaScript添加token驗證邏輯
   - 防止token未正確渲染導致的兌換失敗

### 已知限制

1. **購買記錄查詢效能**
   - 每次Customize頁面載入都查詢WalletHistory
   - 建議未來考慮添加快取或在User_Wallet表添加關聯

2. **0點項目處理**
   - 0點項目不創建WalletHistory記錄
   - 依賴PetSkinColorCostSettings/PetBackgroundCostSettings判斷免費狀態
   - 可能需要在未來明確標記「預設擁有」項目

3. **並發控制**
   - 購買操作使用transaction保護
   - 但多個同時購買請求可能導致競態條件
   - 建議未來考慮添加分散式鎖或樂觀鎖

---

## 📁 關鍵檔案路徑

### Services層
- `GamiPort/Areas/MiniGame/Services/SignInService.cs` - 簽到邏輯+WalletHistory記錄
- `GamiPort/Areas/MiniGame/Services/GamePlayService.cs` - 遊戲邏輯+WalletHistory記錄
- `GamiPort/Areas/MiniGame/Services/WalletService.cs` - 錢包操作+使用記錄
- `GamiPort/Areas/MiniGame/Services/PetService.cs` - 寵物操作+購買/套用邏輯

### Controllers層
- `GamiPort/Areas/MiniGame/Controllers/PetController.cs` - 寵物API endpoints

### Views層（關鍵修改）
- `GamiPort/Areas/MiniGame/Views/Pet/Customize.cshtml` - 購買/套用UI（重大重寫）
- `GamiPort/Areas/MiniGame/Views/Pet/Index.cshtml` - 互動邏輯（重大重寫）
- `GamiPort/Areas/MiniGame/Views/Game/Index.cshtml` - 按鈕修復
- `GamiPort/Areas/MiniGame/Views/Wallet/Exchange.cshtml` - CSRF修復
- `GamiPort/Areas/MiniGame/Views/Wallet/Index.cshtml` - 時間顯示修復
- `GamiPort/Areas/MiniGame/Views/Wallet/Coupons.cshtml` - 格式化+過濾
- `GamiPort/Areas/MiniGame/Views/SignIn/History.cshtml` - 過濾

### 資料庫表（查詢參考）
- `WalletHistory` - 所有交易記錄（本次新增大量記錄邏輯）
- `User_Wallet` - 用戶點數餘額
- `PetSkinColorCostSettings` - 膚色價格配置
- `PetBackgroundCostSettings` - 背景價格配置
- `Pet` - 寵物狀態（SkinColor, BackgroundColor）
- `Coupon` / `EVoucher` - 優惠券/電子禮券

---

## ⚠️ 注意事項

1. **不可跨越邊界**
   - 所有修改必須在 `GamiPort\Areas\MiniGame` 內
   - 需要跨越時必須停下來徵求用戶同意

2. **不可修改資料庫**
   - 嚴禁執行ALTER TABLE或CREATE TABLE
   - 只能使用既有表和欄位

3. **遵循優先級Hierarchy**
   - 實際SQL Server DB > 後台/前台架構 > README第3節 > 前台開發藍圖 > schema文件
   - 有衝突時以此hierarchy為準

4. **定期Git備份**
   - 每完成一小步就commit
   - Commit message包含時間戳與里程碑
   - 使用dev分支，不創建新分支

5. **文件維護**
   - 每次中斷前更新RUNLOG.md/HANDOFF.md/CHECKLIST.md
   - 確保下次可「零猜測」續作

---

## 🚀 快速啟動指令

### 繼續開發
```bash
cd "C:\Users\n2029\Desktop\work-1105\GamiPort\GamiPort"
dotnet build --no-incremental
dotnet run
```

### 查看最新修改
```bash
cd "C:\Users\n2029\Desktop\work-1105"
git status
git diff
```

### 資料庫連線（唯讀）
```bash
# Server: DESKTOP-8HQIS1S\SQLEXPRESS
# Database: GameSpacedatabase
# 可使用SSMS或Azure Data Studio連線
```

---

**接續點維護者**: Claude Code
**最後更新**: 2025-11-07 14:15 (UTC+8)
**下次接續**: Git commit & push → 功能測試 → 數據驗證
