# MiniGame Area 開發核對清單

## 📊 數據庫對齊檢查

### 核心表格（16張）
- [x] User_Wallet - 會員點數系統
- [x] WalletHistory - 交易歷史記錄
- [x] CouponType - 商城優惠券類型
- [x] Coupon - 商城優惠券實例
- [x] EVoucherType - 電子禮券類型
- [x] EVoucher - 電子禮券實例
- [x] EVoucherToken - 電子禮券核銷碼
- [x] EVoucherRedeemLog - 電子禮券核銷記錄
- [x] SignInRule - 簽到規則配置
- [x] UserSignInStats - 會員簽到統計
- [x] Pet - 寵物基本資料
- [x] PetSkinColorCostSettings - 膚色費用設定
- [x] PetBackgroundCostSettings - 背景費用設定
- [x] PetLevelRewardSettings - 等級獎勵設定
- [x] MiniGame - 遊戲記錄
- [x] SystemSettings - 系統動態配置

## 🎯 功能需求對齊（14項）

### 3.1 會員錢包（6項）
- [x] 查看當前會員點數餘額
- [x] 使用會員點數兌換商城優惠券及電子優惠券
- [x] 查看目前擁有商城優惠券
- [x] 查看目前擁有電子優惠券
- [x] 使用電子優惠券（QRCode/Barcode顯示）
- [x] 查看收支明細

### 3.2 會員簽到系統（2+1項）
- [x] 查看月曆型簽到簿並執行簽到
- [x] 查看簽到歷史紀錄
- [x] **新增**: 簽到規則預覽功能

### 3.3 寵物系統（4項）
- [x] 寵物名字修改
- [x] 寵物互動（餵食/洗澡/玩耍/哄睡）
- [ ] 寵物換膚色（扣會員點數）- **需驗證前端顯示**
- [ ] 寵物換背景（可免費或需點數）- **需驗證前端顯示**

### 3.4 小遊戲系統（2項）
- [x] 出發冒險：啟動遊戲流程
- [x] 查看遊戲紀錄

## 🐛 Bug 修復清單

### 圖片1 - Wallet/Coupons
- [x] 優惠券標題統一為「商城優惠券」

### 圖片2 - Wallet/Exchange
- [x] 標題改為「商城優惠券兌換」
- [ ] 兌換功能測試（GUID生成與持久化）

### 圖片3 - Pet/Index（CRITICAL）
- [x] 黑色圈圈改為 #F0F0F0 顏色
- [ ] 經驗值條狀圖比例顯示修復
- [ ] 寵物背景圖片正確載入
- [ ] 互動功能即時更新（無需刷新）
- [x] 右下角「出發冒險」按鈕顯示（z-index修復）

### 圖片4 - Pet/Customize
- [ ] 點數顯示精緻化為「會員點數餘額」

### 圖片5 - Pet/Customize
- [ ] 預覽區「預覽」文字排版優化
- [ ] 寵物名排版優化
- [ ] 背景選擇即時套用到預覽區

### 圖片7 - SignIn/Index
- [ ] 連續簽到天數計算邏輯修復

### 全局問題
- [ ] 所有時間顯示修正為 UTC+8 台灣時區

## 🔍 技術債務檢查

### Code Quality
- [ ] dotnet build 無 error（目標：0 errors）
- [ ] 所有文件 UTF-8 with BOM
- [ ] 遵守 Area 邊界約束

### Time Handling
- [ ] SignInService.cs 使用 IAppClock
- [ ] WalletService.cs 使用 IAppClock
- [ ] 所有 View files 使用 IAppClock
- [ ] 移除所有 DateTime.Now / DateTime.UtcNow 直接調用

### Business Rules
- [x] 寵物屬性範圍 0-100
- [x] 寵物互動無冷卻時間
- [x] 每日狀態全滿獎勵：100 寵物經驗 + 100 會員點數
- [x] 每日遊戲限制 3 次
- [x] 簽到限制每日一次（UTC+8）

## 📝 文檔維護
- [x] RUNLOG.md 創建並更新
- [x] HANDOFF.md 創建並更新
- [x] CHECKLIST.md 創建並更新
- [ ] Git commit 定期執行

## 🚦 當前狀態摘要
- **已完成**: 8/14 功能，4/12 Bug修復
- **進行中**: Pet & Customize 優化
- **阻塞項**: 無
- **下一步**: 並行agents執行剩餘修復

---
**最後檢查時間**: 2025-11-06
**完成度**: ~60%
**緊急程度**: SUPER URGENT
