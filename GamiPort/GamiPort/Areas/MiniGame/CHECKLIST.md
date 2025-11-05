# MiniGame Area 前台開發核對清單 (CHECKLIST)

## 📚 階段一：文檔閱讀與理解

### 必讀文檔（依層級）
- [ ] **SQL Server DB** - 實際連線查看 schema 與種子資料
  - [ ] 驗證所有 MiniGame 相關表格結構
  - [ ] 確認欄位型別、長度、非空約束
  - [ ] 確認 FK/PK/UK/CHECK/Identity 約束
  - [ ] 檢查種子資料範例

- [ ] **後台既有架構 + 前台現況**
  - [ ] GameSpace MiniGame Area 後台架構
  - [ ] GamiPort MiniGame Area 前台現況

- [ ] **README_合併版.md（第3節）**
  - [ ] 閱讀到檔尾
  - [ ] 摘要前台所需功能清單
  - [ ] 記錄關鍵需求

- [ ] **前台開發藍圖文件.md**
  - [ ] 閱讀到檔尾
  - [ ] 摘要開發計畫
  - [ ] 記錄里程碑

- [ ] **schema 資料夾所有檔案**
  - [ ] MiniGame Area 架構對比分析報告.md
  - [ ] 巴哈姆特風格布局特色完整分析.md
  - [ ] MiniGame_Area_完整描述文件.md
  - [ ] MiniGame_area功能彙整.txt
  - [ ] MiniGameArea_DB架構與種子資料報告.md
  - [ ] 專案規格敘述1.txt
  - [ ] 專案規格敘述2.txt
  - [ ] 其他相關文檔

- [ ] **設計資源**
  - [ ] MiniGame_Area想要採用的風格(淡藍現代系配色) 資料夾
  - [ ] PetBackgroundCostSettings表格_種子資料_圖片 資料夾

---

## 🏗️ 階段二：環境準備與現況檢查

### 資料庫連接
- [ ] 連接 SQL Server 成功
- [ ] 驗證連接字串：`(local)\SQLEXPRESS` 或 `DESKTOP-8HQIS1S\SQLEXPRESS`
- [ ] 確認 Database: `GameSpacedatabase`
- [ ] 列出所有 MiniGame 相關表格

### MiniGame Area 現有結構檢查
- [ ] **Controllers 檢查**
  - [ ] 列出所有現有 Controllers
  - [ ] 檢查命名規範
  - [ ] 檢查路由配置

- [ ] **Services 檢查**
  - [ ] 列出所有現有 Services
  - [ ] 檢查介面與實作分離
  - [ ] 檢查 DI 註冊

- [ ] **Views 檢查**
  - [ ] 列出所有現有 Views
  - [ ] 檢查佈局與樣式
  - [ ] 檢查靜態資源引用

- [ ] **Models 檢查**
  - [ ] 列出所有現有 Models
  - [ ] 檢查是否對齊 DB schema
  - [ ] 檢查資料註解與驗證

- [ ] **wwwroot 檢查**
  - [ ] 檢查目錄結構
  - [ ] 檢查靜態資源（CSS, JS, 圖片）
  - [ ] 確認 Unity/遊戲資源位置

---

## 🎨 階段三：Views 開發

### 寵物互動主頁
- [ ] **頁面結構**
  - [ ] 採用巴哈姆特風格佈局
  - [ ] 應用淡藍現代系配色（#0d9488, #17a2b8, #f0f4f8）
  - [ ] 響應式設計（RWD）

- [ ] **寵物顯示**
  - [ ] 顯示寵物基本資訊（名稱、等級、經驗值）
  - [ ] 顯示寵物狀態（飢餓度、心情、體力、清潔度、健康值）
  - [ ] 寵物外觀（膚色、背景）可視化
  - [ ] 互動按鈕（餵食、洗澡、玩耍、睡眠）

- [ ] **右下角「出發冒險」按鈕**
  - [ ] 固定位置（Fixed Position）
  - [ ] 橙色漸層（#ff9f43 → #ffa500）
  - [ ] Hover/Active 效果
  - [ ] 點擊跳轉到遊戲頁面

- [ ] **資料繫結**
  - [ ] 從 Controller 取得寵物資料
  - [ ] 使用 ViewBag/ViewModel 傳遞資料
  - [ ] 對齊 DB schema（Pet 表）

### 小遊戲頁面（Chrome 恐龍風格）
- [ ] **頁面結構**
  - [ ] 遊戲容器（Unity WebGL 或 HTML5 Canvas）
  - [ ] 載入提示動畫
  - [ ] 遊戲控制按鈕（開始、暫停、重玩）

- [ ] **遊戲邏輯**
  - [ ] 恐龍跑酷遊戲實作（參考 Chrome 離線恐龍）
  - [ ] 分數計算
  - [ ] 障礙物生成
  - [ ] 碰撞檢測

- [ ] **Unity WebGL 整合**（如採用）
  - [ ] Unity 專案建置
  - [ ] WebGL Build 輸出
  - [ ] 放置於 `wwwroot/Unity/PetAdventure/`
  - [ ] Razor View 中嵌入 Unity Loader

- [ ] **遊戲結果處理**
  - [ ] 成功提示（獲得獎勵）
  - [ ] 失敗提示（可重試）
  - [ ] 返回寵物主頁按鈕

- [ ] **資料繫結**
  - [ ] 遊戲次數限制（每日3次）
  - [ ] 難度選擇（Level 1/2/3）
  - [ ] 獎勵發放（點數、經驗值）
  - [ ] 對齊 DB schema（MiniGame 表）

### 其他 Views
- [ ] **錢包頁面** (Wallet/Index)
- [ ] **簽到頁面** (SignIn/Index)
- [ ] **遊戲歷史** (Game/History)
- [ ] **寵物定制** (Pet/Customize)

---

## 🗃️ 階段四：Models 開發

### Pet Models
- [ ] **Pet.cs** - 對齊 DB 的 Pet 表
  - [ ] PetId (int, PK, Identity)
  - [ ] UserId (int, FK)
  - [ ] PetName (nvarchar)
  - [ ] Level (int)
  - [ ] Experience (int)
  - [ ] ExperienceToNextLevel (int, nullable)
  - [ ] Hunger (int, 0-100)
  - [ ] Mood (int, 0-100)
  - [ ] Stamina (int, 0-100)
  - [ ] Cleanliness (int, 0-100)
  - [ ] Health (int, 0-100)
  - [ ] SkinColor (nvarchar)
  - [ ] BackgroundColor (nvarchar)
  - [ ] 軟刪除欄位（IsDeleted, DeletedAt, DeletedBy, DeleteReason）
  - [ ] 稽核欄位（CreatedAt, UpdatedAt, UpdatedBy）

### MiniGame Models
- [ ] **MiniGame.cs** - 對齊 DB 的 MiniGame 表
  - [ ] PlayId (int, PK, Identity)
  - [ ] UserId (int, FK)
  - [ ] PetId (int, FK)
  - [ ] Level (int, 1-3)
  - [ ] Result (nvarchar: Win/Lose/Abort)
  - [ ] ExpGained (int)
  - [ ] PointsGained (int)
  - [ ] 其他遊戲相關欄位
  - [ ] 軟刪除與稽核欄位

### ViewModels
- [ ] **PetIndexViewModel** - 寵物主頁 ViewModel
  - [ ] Pet 資料
  - [ ] UserWallet 資料
  - [ ] 互動冷卻狀態

- [ ] **GameIndexViewModel** - 遊戲頁面 ViewModel
  - [ ] 剩餘遊戲次數
  - [ ] 選擇的難度
  - [ ] 遊戲結果
  - [ ] 獎勵資訊

- [ ] **其他 ViewModels** (依需求新增)

---

## 🧪 階段五：測試與驗證

### 編譯驗證
- [ ] 專案編譯成功（零錯誤）
- [ ] 無警告（或僅剩無關緊要的警告）
- [ ] NuGet 套件完整

### 資料庫對齊驗證
- [ ] 所有 Model 欄位與 DB 完全一致
- [ ] 欄位型別正確（int, nvarchar, datetime, bit 等）
- [ ] 約束正確（FK, PK, UK, CHECK）
- [ ] 軟刪除與稽核欄位完整

### UI/UX 驗證
- [ ] 巴哈姆特風格正確應用
- [ ] 淡藍現代系配色正確（#0d9488, #17a2b8, #f0f4f8, #ff9f43）
- [ ] 響應式設計正常（手機、平板、桌面）
- [ ] Hover/Active/Focus 效果正常
- [ ] 載入提示正常顯示
- [ ] 錯誤訊息友善

### 功能驗證
- [ ] 寵物互動功能正常
- [ ] 遊戲可正常啟動與結束
- [ ] 獎勵正確發放
- [ ] 遊戲次數限制正確
- [ ] 資料庫讀寫正常

---

## 📦 階段六：Git 備份

### 每個小步驟
- [ ] `git add .`
- [ ] `git commit -m "[時間戳] [里程碑描述]"`
- [ ] `git push origin dev`

### Commit 訊息規範
- 格式：`[類型] 簡短描述 (檔案/模組)`
- 類型：feat, fix, docs, style, refactor, test
- 包含時間戳（台北時間）

---

## ✅ 最終檢查

### 品質門檻
- [ ] ✅ 零編譯錯誤
- [ ] ✅ 100% 對齊 SQL Server DB
- [ ] ✅ 巴哈姆特風格 + 淡藍現代系配色
- [ ] ✅ 高互動性、美觀、流暢
- [ ] ✅ 所有修改限制在 `Areas/MiniGame` 內
- [ ] ✅ RUNLOG.md 完整記錄
- [ ] ✅ HANDOFF.md 更新最新狀態
- [ ] ✅ Git 備份完成

---

*最後更新: 2025-11-05 19:30 (台北時間)*
