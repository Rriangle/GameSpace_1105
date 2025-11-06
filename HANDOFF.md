# MiniGame Area 接續點與待辦清單

## 🎯 當前接續點
**階段**: 實現診斷完成的修復方案
**上次中斷點**: 確認部分修復已完成（z-index, Exchange標題），準備執行剩餘任務

## ✅ 已完成項目
1. ✅ 診斷階段完成（4個agents完成root cause分析）
2. ✅ Pet/Index - 出發冒險按鈕 z-index 已修復為 1100
3. ✅ Wallet/Exchange - 標題已統一為「商城優惠券兌換」
4. ✅ Wallet/Coupons - 標題已正確為「商城優惠券」

## 📋 TO-DO 清單（按優先級）

### P0 - CRITICAL（寵物系統）
- [ ] Pet/Index - 經驗值條狀圖比例顯示修復
- [ ] Pet/Index - 寵物背景圖片載入修復
- [ ] Pet/Index - 互動即時更新（移除頁面刷新需求）

### P1 - HIGH（客製化與顯示）
- [ ] Pet/Customize - 預覽背景即時套用
  - 實現 image preloading
  - 添加 error handling
  - 設置 explicit CSS properties
- [ ] Pet/Customize - 預覽區排版優化
  - 「預覽」文字添加半透明背景
  - 寵物名添加 backdrop-filter blur
- [ ] Pet/Customize - 點數顯示精緻化
  - 改名為「會員點數餘額」
  - 添加漸層背景和錢幣圖標

### P2 - MEDIUM（後端邏輯）
- [ ] SignInService.cs - 重寫 CalculateConsecutiveDays 算法
  - 修復 Lines 348-390
  - 修復 Lines 228, 230 的 timezone 問題
- [ ] WalletService.cs - Timezone 修復（Lines 868, 901）
- [ ] 全局 View files - 注入 IAppClock 並替換 DateTime.Now

### P3 - VERIFICATION
- [ ] Wallet/Exchange - 測試 GUID 兌換功能
- [ ] 執行 dotnet build 確保 0 errors
- [ ] Git commit 和 push

## 🔧 技術上下文

### 修復方案已就緒的文件
所有解決方案的完整代碼已在summary中提供：
1. **Pet/Index.cshtml** - 出發冒險按鈕相關
2. **Pet/Customize.cshtml** - 3個修復點的完整代碼
3. **SignInService.cs** - 重寫算法的完整實現
4. **WalletService.cs** - Timezone 修復點
5. **View files** - IAppClock 注入模式

### 關鍵約束
- 僅修改 GamiPort\Areas\MiniGame 內文件
- 使用 IAppClock 處理所有時間（UTC+8）
- 一次只有一個 todo 為 in_progress

### 已知問題
- 圖片3提到的經驗值條狀圖需要和5個屬性條一樣顯示比例
- 圖片3提到的背景圖片未正確載入
- 圖片3提到的互動功能顯示失敗但實際成功（需刷新）
- 圖片5提到的預覽背景空白
- 圖片7提到的連續簽到天數錯誤（顯示9天實際只1天）

## 🚀 恢復工作指引
1. 檢查 RUNLOG.md 最新狀態
2. 從 P0 任務開始執行
3. 使用 parallel agents 加速（用戶要求）
4. 每完成一項立即更新 TodoWrite 和 CHECKLIST.md
5. 定期 git commit

---
**最後更新**: 2025-11-06
**緊急程度**: SUPER URGENT DEADLINE PRESSURE
