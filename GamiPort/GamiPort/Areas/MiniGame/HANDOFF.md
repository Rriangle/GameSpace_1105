# MiniGame Area 前台開發交接文檔 (HANDOFF)

## 📍 當前狀態 (2025-11-05 19:45 台北時間)

### 進度概覽
- **總體進度**: 70% - 核心功能已完成，關鍵缺失已識別
- **當前階段**: 文檔分析完成，準備實作缺失功能
- **下一階段**: 實作寵物升級系統 (最高優先級)

### 已完成項目
- [x] 確認專案目錄存在 (work-1105)
- [x] 確認 MiniGame Area 路徑存在
- [x] 確認所有必要文檔存在
- [x] 創建進度追蹤文件 (RUNLOG.md, HANDOFF.md, CHECKLIST.md)
- [x] 閱讀並分析所有關鍵文檔
  - [x] README_合併版.md - 後台完成，前台需求明確
  - [x] 前台開發藍圖文件.md - Vue.js + Unity WebGL 技術棧
  - [x] 巴哈姆特風格布局特色完整分析.md - 完整設計規格
  - [x] MiniGame Area 架構對比分析報告.md - 70% 完成度分析
  - [x] MiniGame_Area_完整描述文件.md - 四大子系統規格
- [x] 檢查 GamiPort MiniGame Area 現有結構
  - Controllers: 5 個 (Game, Home, Pet, SignIn, Wallet)
  - Services: 9 個檔案
  - Views: 12 個
  - Helpers: TimeHelper.cs (UTC+8 時間處理)

### 現有架構分析

**已實作功能** (70%):
- ✅ 核心查詢功能 (100%) - 錢包查詢、簽到查詢、寵物查詢、遊戲查詢
- ✅ 核心互動功能 (90%) - 簽到執行、寵物互動、遊戲玩法
- ✅ 前端 UI (91.7%) - 11/12 頁面完成
- ✅ 時間處理 (100%) - IAppClock + TimeHelper UTC+8 完整實作
- ✅ 模糊搜尋 (100%) - 5級優先順序匹配

### 待辦事項 (依優先級)

#### 🔴 高優先級 (立即執行)
1. [ ] **實作寵物升級系統** (最關鍵！)
   - 建立 IPetLevelingService 介面與實作
   - CheckAndLevelUpAsync() - 檢查並升級
   - 升級閾值計算（Level 1-10, 11-100, 101+）
   - 升級獎勵發放（點數、優惠券）
   - 整合至 GamePlayService 和 SignInService
   - 測試升級流程

2. [ ] **優惠券/電子禮券使用功能**
   - IWalletService 新增 UseCouponAsync()
   - IWalletService 新增 RedeemEVoucherAsync()
   - WalletController 新增對應 Actions
   - 建立使用/兌換頁面

3. [ ] **錢包交易歷史頁面**
   - WalletController.History Action
   - Wallet/History.cshtml
   - 分頁與篩選（日期、類型）

#### 🟡 中優先級 (後續執行)
4. [ ] **基礎設施補充 - Constants 目錄**
   - WalletConstants.cs（變更類型、項目代碼）
   - PetConstants.cs（屬性範圍、成本定義）
   - SignInConstants.cs（獎勵配置、閾值）
   - GameConstants.cs（遊戲常數）
   - 移除現有 Magic Numbers

5. [ ] **基礎設施補充 - Filters 目錄**
   - IdempotencyFilter.cs（防重機制，60秒）
   - FrontendProblemDetailsFilter.cs（統一錯誤處理）
   - 在關鍵 Actions 套用 IdempotencyFilter

6. [ ] **基礎設施補充 - Config 目錄**
   - config/ServiceExtensions.cs
   - 集中註冊 MiniGame Area 服務
   - 更新 Program.cs 調用擴展方法

7. [ ] **簽到規則預覽功能**
   - GetAllSignInRulesAsync() 方法
   - SignIn/Rules.cshtml 頁面
   - 顯示未來獎勵預覽

#### 🟢 低優先級 (有時間再做)
8. [ ] **儀表板數據展示**
   - 實作 HomeController.Index
   - 顯示用戶概覽（點數、寵物、簽到、遊戲）
   - 快捷操作按鈕

9. [ ] **排行榜系統**
   - 遊戲排行榜（勝率、總勝場）
   - 寵物排行榜（等級、經驗值）
   - 簽到排行榜（連續天數）
   - 實作快取機制

10. [ ] **優化與測試**
    - 編譯驗證（零錯誤）
    - UI/UX 測試
    - 性能優化
    - 完整功能測試

---

## 🚨 阻塞問題
*目前無阻塞*

---

## 📂 關鍵檔案路徑

### 必讀文檔
- `C:\Users\n2029\Desktop\work-1105\schema\README_合併版.md`
- `C:\Users\n2029\Desktop\work-1105\schema\前台開發藍圖文件.md`
- `C:\Users\n2029\Desktop\work-1105\schema\MiniGame Area 架構對比分析報告.md`
- `C:\Users\n2029\Desktop\work-1105\schema\巴哈姆特風格布局特色完整分析.md`
- `C:\Users\n2029\Desktop\work-1105\schema\MiniGameArea_DB架構與種子資料報告.md`

### 工作路徑
- **根目錄**: `C:\Users\n2029\Desktop\work-1105\GamiPort\GamiPort\Areas\MiniGame`
- **Controllers**: `./Controllers/`
- **Services**: `./Services/`
- **Views**: `./Views/`
- **Models**: (需確認位置，可能在上層 Models/)
- **wwwroot**: `./wwwroot/`

---

## 🔑 重要提醒

### 越界規範
- **絕對禁止**在 `Areas/MiniGame` 外修改檔案
- 如需越界，立即進入 **PAUSE-AND-ASK 模式**
- 提供 diff 與理由，等待批准

### Git 備份策略
- 每完成一小步就 `git add . && git commit && git push`
- 使用 `dev` 分支（不可創建新分支）
- Commit message 包含時間戳與里程碑

### 品質標準
- ✅ 零編譯錯誤
- ✅ 100% 對齊 SQL Server DB
- ✅ 巴哈姆特風格 + 淡藍現代系配色
- ✅ 高互動性、美觀、流暢

---

## 📞 下次接續點

**從這裡開始**:
1. 啟動 4-6 個代理並行閱讀所有必要文檔
2. 連接 SQL Server 驗證資料庫
3. 檢查 MiniGame Area 現有結構
4. 開始 Views 開發

**預期時間**: 2-3 小時完成文檔閱讀與環境準備

---

*最後更新: 2025-11-05 19:30 (台北時間)*
