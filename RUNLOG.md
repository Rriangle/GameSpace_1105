# MiniGame Area (GamiPort) 開發執行日誌

## 2025-11-06 繼續修復任務（台北時間）

### 已完成項目
✅ Pet/Index - 出發冒險按鈕 z-index 修復（已確認 z-index: 1100）
✅ Wallet/Exchange - 標題已改為「商城優惠券兌換」

### 當前執行中
🔄 啟動多個parallel agents處理剩餘修復任務

### 待完成清單
1. **Pet/Index.cshtml 剩餘修復**
   - 經驗值條狀圖比例顯示
   - 寵物背景圖片載入
   - 互動即時更新（無需刷新頁面）

2. **Pet/Customize.cshtml 全面優化**
   - 預覽背景即時套用（含image preloading）
   - 預覽區排版優化（「預覽」文字 + 寵物名）
   - 點數顯示改為「會員點數餘額」並精緻化

3. **SignInService.cs 算法重寫**
   - CalculateConsecutiveDays 邏輯修復
   - Timezone 修復（使用 IAppClock）

4. **全局 UTC+8 時區修復**
   - WalletService.cs
   - 所有 View files（inject IAppClock）

### 技術決策記錄
- 使用 Task tool 並行處理複雜修復，提升效率
- 遵循 GamiPort\Areas\MiniGame 邊界約束
- 所有時間處理統一使用 IAppClock.ToAppTime()

### 下一步行動
並行啟動4個agents，每個負責一組相關修復任務

---
**更新時間**: 2025-11-06
**執行者**: Claude Code
