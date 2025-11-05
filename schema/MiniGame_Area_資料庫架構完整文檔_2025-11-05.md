# MiniGame Area 資料庫架構完整文檔

**文檔目的**: 詳細記錄 MiniGame Area 所有 20 張表的資料庫架構（列定義、約束、種子資料），供其他 AI 系統無需連接 SQL Server 即可理解資料庫設計

**生成日期**: 2025-11-05
**資料庫**: GameSpacedatabase (SQL Server 2022 Express)
**MiniGame Area 表總數**: 20 張（16 張主要表 + 4 張 FK 的使用者/權限表->此 4 張表非屬於 MiniGame Area）

---

## 目錄

1. [使用者/權限表 (4 張)](#使用者權限表)

   - Users
   - ManagerData
   - ManagerRole
   - ManagerRolePermission

2. [會員錢包系統 (2 張)](#會員錢包系統)

   - User_Wallet
   - WalletHistory

3. [優惠券系統 (2 張)](#優惠券系統)

   - Coupon
   - CouponType

4. [電子禮券系統 (4 張)](#電子禮券系統)

   - EVoucher
   - EVoucherType
   - EVoucherToken
   - EVoucherRedeemLog

5. [簽到系統 (2 張)](#簽到系統)

   - UserSignInStats
   - SignInRule

6. [寵物系統 (4 張)](#寵物系統)

   - Pet
   - PetSkinColorCostSettings
   - PetBackgroundCostSettings
   - PetLevelRewardSettings

7. [小遊戲系統 (1 張)](#小遊戲系統)

   - MiniGame

8. [系統設定 (1 張)](#系統設定)
   - SystemSettings

---

## 使用者/權限表

### 1. Users 表

**用途**: 儲存所有遊戲用戶帳號資訊

**表結構**:

| 欄位名稱                  | 資料型態  | 長度 | 可否為空 | 預設值       | 約束                     | 備註                   |
| ------------------------- | --------- | ---- | -------- | ------------ | ------------------------ | ---------------------- |
| User_ID                   | int       | -    | NOT NULL | -            | PK, IDENTITY(10000001,1) | 使用者識別碼，自動遞增 |
| User_name                 | nvarchar  | 100  | NULL     | -            | -                        | 使用者暱稱             |
| User_Account              | nvarchar  | 256  | NULL     | -            | UNIQUE                   | 帳號（登入用），唯一   |
| User_Password             | nvarchar  | max  | NULL     | -            | -                        | 密碼（加密存儲）       |
| User_EmailConfirmed       | bit       | -    | NOT NULL | 0            | -                        | 信箱確認狀態           |
| User_PhoneNumberConfirmed | bit       | -    | NOT NULL | 0            | -                        | 電話號碼確認狀態       |
| User_TwoFactorEnabled     | bit       | -    | NOT NULL | 0            | -                        | 雙因素認證啟用         |
| User_AccessFailedCount    | int       | -    | NOT NULL | 0            | -                        | 登入失敗次數計數器     |
| User_LockoutEnabled       | bit       | -    | NOT NULL | 0            | -                        | 帳號鎖定啟用           |
| User_LockoutEnd           | datetime2 | 7    | YES      | NULL         | -                        | 帳號鎖定結束時間       |
| Create_Account            | datetime2 | 7    | NOT NULL | GETUTCDATE() | -                        | 帳號建立時間           |

**主要約束**:

- **PK**: User_ID (Primary Key)
- **UNIQUE**: User_Account (帳號唯一性)
- **IDENTITY**: User_ID (種子: 10000001, 增量: 1)

**種子資料統計**:

- 總記錄數: **200 筆** (User_ID 10000001 ~ 10000200)
- 全部啟用狀態
- 建立日期: 2025-10-23 16:14:43

**部分種子資料樣本** (前 20 筆):

| User_ID              | User_name      | User_Account   | Create_Account      |
| -------------------- | -------------- | -------------- | ------------------- |
| 10000001             | DragonKnight88 | dragonknight88 | 2025-10-23 16:14:43 |
| 10000002             | TechGuru92     | tech_guru_92   | 2025-10-23 16:14:43 |
| 10000003             | CoffeeAddict   | coffee_addict  | 2025-10-23 16:14:43 |
| 10000004             | YogaMaster     | yoga_master    | 2025-10-23 16:14:43 |
| 10000005             | BookLover      | book_lover_95  | 2025-10-23 16:14:43 |
| ... (196 筆更多記錄) |

---

### 2. ManagerData 表

**用途**: 儲存管理員（後台使用者）基本資訊

**表結構**:

| 欄位名稱                        | 資料型態  | 長度 | 可否為空 | 預設值 | 約束                     | 備註               |
| ------------------------------- | --------- | ---- | -------- | ------ | ------------------------ | ------------------ |
| Manager_Id                      | int       | -    | NOT NULL | -      | PK, IDENTITY(30000001,1) | 管理員識別碼       |
| Manager_Name                    | nvarchar  | 100  | NULL     | -      | -                        | 管理員名稱         |
| Manager_Account                 | nvarchar  | 256  | NULL     | -      | UNIQUE                   | 管理員帳號         |
| Manager_Password                | nvarchar  | max  | NULL     | -      | -                        | 管理員密碼（加密） |
| Administrator_registration_date | datetime2 | 7    | NULL     | -      | -                        | 註冊日期           |
| Manager_Email                   | nvarchar  | 256  | NULL     | -      | -                        | 管理員信箱         |
| Manager_EmailConfirmed          | bit       | -    | NOT NULL | 0      | -                        | 信箱確認狀態       |
| Manager_AccessFailedCount       | int       | -    | NOT NULL | 0      | -                        | 登入失敗次數       |
| Manager_LockoutEnabled          | bit       | -    | NOT NULL | 0      | -                        | 帳號鎖定啟用       |
| Manager_LockoutEnd              | datetime2 | 7    | YES      | NULL   | -                        | 帳號鎖定結束時間   |

**主要約束**:

- **PK**: Manager_Id
- **UNIQUE**: Manager_Account
- **IDENTITY**: Manager_Id (種子: 30000001, 增量: 1)

**種子資料統計**:

- 總記錄數: **102 筆** (Manager_Id 30000001 ~ 30000102)
- 註冊日期範圍: 2019-01-15 ~ 2019-04-24
- 名稱為多語言混合（英文和中文名稱）

**部分種子資料樣本** (前 10 筆):

| Manager_Id          | Manager_Name | Manager_Account  | Administrator_registration_date |
| ------------------- | ------------ | ---------------- | ------------------------------- |
| 30000001            | Milk Hung    | zhang_zhiming_01 | 2019-01-15 08:30:00             |
| 30000002            | 李小華       | li_xiaohua_02    | 2019-01-16 09:15:00             |
| 30000003            | 王美玲       | wang_meiling_03  | 2019-01-17 10:45:00             |
| 30000004            | 陳大衛       | chen_dawei_04    | 2019-01-18 11:20:00             |
| 30000005            | 林雅婷       | lin_yating_05    | 2019-01-19 14:30:00             |
| ... (97 筆更多記錄) |

---

### 3. ManagerRole 表

**用途**: 儲存管理員的角色指派（多對一關係）

**表結構**:

| 欄位名稱       | 資料型態 | 可否為空 | 預設值 | 約束                                        | 備註         |
| -------------- | -------- | -------- | ------ | ------------------------------------------- | ------------ |
| Manager_Id     | int      | NOT NULL | -      | FK→ManagerData.Manager_Id, PK               | 管理員識別碼 |
| ManagerRole_Id | int      | NOT NULL | -      | FK→ManagerRolePermission.ManagerRole_Id, PK | 角色識別碼   |

**主要約束**:

- **PK**: (Manager_Id, ManagerRole_Id) - 複合主鍵
- **FK**: Manager_Id → ManagerData.Manager_Id (級聯)
- **FK**: ManagerRole_Id → ManagerRolePermission.ManagerRole_Id (級聯)

**種子資料統計**:

- 總記錄數: **102 筆** (與 ManagerData 一對一，每個管理員分配一個角色)
- 角色分佈:
  - 角色 1 (全管理員): 1 人
  - 角色 2 (使用者/訊息管理): 5 人
  - 角色 3 (購物/寵物管理): 5 人
  - 角色 4 (一般/使用者管理): 10 人
  - 角色 5 (購物管理): 42 人
  - 角色 6 (訊息管理): 18 人
  - 角色 7 (寵物管理): 15 人
  - 角色 8 (客服): 6 人

**種子資料樣本** (前 30 筆):

| Manager_Id          | ManagerRole_Id |
| ------------------- | -------------- |
| 30000001            | 1              |
| 30000002            | 2              |
| 30000003            | 3              |
| 30000004            | 4              |
| 30000005            | 5              |
| 30000006            | 6              |
| 30000007            | 7              |
| 30000008            | 8              |
| 30000009            | 4              |
| 30000010            | 2              |
| ... (92 筆更多記錄) |

---

### 4. ManagerRolePermission 表

**用途**: 定義管理員角色的權限組合

**表結構**:

| 欄位名稱                          | 資料型態 | 可否為空 | 預設值 | 約束              | 備註                         |
| --------------------------------- | -------- | -------- | ------ | ----------------- | ---------------------------- | -------- |
| ManagerRole_Id                    | int      | NOT NULL | -      | PK, IDENTITY(1,1) | 角色識別碼                   |
| role_name                         | nvarchar | 100      | NULL   | -                 | -                            | 角色名稱 |
| AdministratorPrivilegesManagement | bit      | NOT NULL | 0      | -                 | 管理員權限管理（0=否, 1=是） |
| UserStatusManagement              | bit      | NOT NULL | 0      | -                 | 使用者狀態管理               |
| ShoppingPermissionManagement      | bit      | NOT NULL | 0      | -                 | 購物功能管理                 |
| MessagePermissionManagement       | bit      | NOT NULL | 0      | -                 | 訊息功能管理                 |
| Pet_Rights_Management             | bit      | NOT NULL | 0      | -                 | 寵物系統管理                 |
| customer_service                  | bit      | NOT NULL | 0      | -                 | 客戶服務                     |

**主要約束**:

- **PK**: ManagerRole_Id
- **IDENTITY**: ManagerRole_Id (種子: 1, 增量: 1)

**權限組合定義** (8 種角色):

| Role_ID | 角色名稱       | 管理員管理 | 使用者管理 | 購物管理 | 訊息管理 | 寵物管理 | 客服 |
| ------- | -------------- | ---------- | ---------- | -------- | -------- | -------- | ---- |
| 1       | 系統管理員     | ✓          | ✓          | ✓        | ✓        | ✓        | ✓    |
| 2       | 社群和客服管理 | ✗          | ✓          | ✗        | ✓        | ✗        | ✓    |
| 3       | 購物和寵物管理 | ✗          | ✗          | ✓        | ✗        | ✓        | ✗    |
| 4       | 一般使用者管理 | ✗          | ✓          | ✗        | ✗        | ✗        | ✗    |
| 5       | 購物中心管理   | ✗          | ✗          | ✓        | ✗        | ✗        | ✗    |
| 6       | 訊息中心管理   | ✗          | ✗          | ✗        | ✓        | ✗        | ✗    |
| 7       | 寵物系統管理   | ✗          | ✗          | ✗        | ✗        | ✓        | ✗    |
| 8       | 客戶服務代表   | ✗          | ✗          | ✗        | ✗        | ✗        | ✓    |

**種子資料**: 共 8 筆（定義所有角色）

---

## 會員錢包系統

### 5. User_Wallet 表

**用途**: 儲存會員當前點數餘額

**表結構**:

| 欄位名稱     | 資料型態  | 可否為空 | 預設值 | 約束                 | 備註         |
| ------------ | --------- | -------- | ------ | -------------------- | ------------ | ---------- |
| User_Id      | int       | NOT NULL | -      | PK, FK→Users.User_ID | 使用者識別碼 |
| User_Point   | int       | NOT NULL | 0      | -                    | 當前點數餘額 |
| IsDeleted    | bit       | NOT NULL | 0      | -                    | 軟刪除標記   |
| DeletedAt    | datetime2 | YES      | NULL   | -                    | 刪除時間     |
| DeletedBy    | nvarchar  | 256      | YES    | NULL                 | -            | 刪除者帳號 |
| DeleteReason | nvarchar  | 500      | YES    | NULL                 | -            | 刪除原因   |

**主要約束**:

- **PK**: User_Id
- **FK**: User_Id → Users.User_ID (級聯)

**CHECK 約束**:

- `CK_User_Wallet_Points`: User_Point >= 0

**種子資料樣本** (UserID 10000001 和 10000002):

| User_Id  | User_Point | IsDeleted |
| -------- | ---------- | --------- |
| 10000001 | 60030      | 0         |
| 10000002 | 21666      | 0         |

---

### 6. WalletHistory 表

**用途**: 記錄會員點數變動歷史

**表結構**:

| 欄位名稱      | 資料型態  | 可否為空 | 預設值   | 約束             | 備註                               |
| ------------- | --------- | -------- | -------- | ---------------- | ---------------------------------- | ------------ |
| LogID         | int       | NOT NULL | -        | PK, IDENTITY     | 歷史記錄識別碼                     |
| UserID        | int       | NOT NULL | -        | FK→Users.User_ID | 使用者識別碼                       |
| ChangeType    | nvarchar  | 50       | NULL     | -                | 變動類型（Point, Exp, etc）        |
| PointsChanged | int       | NOT NULL | 0        | -                | 點數變動量（正數=增加, 負數=消費） |
| ItemCode      | nvarchar  | 100      | YES      | NULL             | -                                  | 關聯項目代碼 |
| Description   | nvarchar  | 500      | YES      | NULL             | -                                  | 變動說明     |
| ChangeTime    | datetime2 | 7        | NOT NULL | GETUTCDATE()     | -                                  | 變動時間     |
| IsDeleted     | bit       | NOT NULL | 0        | -                | 軟刪除標記                         |

**主要約束**:

- **PK**: LogID
- **FK**: UserID → Users.User_ID (級聯)
- **IDENTITY**: LogID

**CHECK 約束**:

- ChangeType 需為有效類型

**種子資料樣本** (UserID 10000001):

| LogID | UserID   | ChangeType | PointsChanged | ItemCode              | Description             | ChangeTime          |
| ----- | -------- | ---------- | ------------- | --------------------- | ----------------------- | ------------------- |
| 1939  | 10000001 | Point      | 94500         | INIT-BAL-001          | Initial account balance | 2023-02-22 08:00:00 |
| 1929  | 10000001 | Point      | -2000         | #FFFF00               | 購買寵物膚色黃色        | 2023-02-22 09:10:06 |
| 7     | 10000001 | Point      | 30            | NULL                  | 小遊戲獲勝額外獎勵點數  | 2023-12-08 03:34:50 |
| 3     | 10000001 | Point      | -30000        | EV-FAMILY-MNPQ-064877 | 兌換點數購買電子禮券    | 2024-10-29 15:17:44 |
| 1930  | 10000001 | Point      | -2500         | BG005                 | 購買寵物背景            | 2025-04-09 17:03:40 |

---

## 優惠券系統

### 7. Coupon 表

**用途**: 儲存會員優惠券所有權

**表結構**:

| 欄位名稱      | 資料型態  | 長度 | 可否為空 | 預設值       | 約束                       | 備註                         |
| ------------- | --------- | ---- | -------- | ------------ | -------------------------- | ---------------------------- |
| CouponID      | int       | -    | NOT NULL | -            | PK, IDENTITY               | 優惠券識別碼                 |
| CouponCode    | nvarchar  | 50   | NOT NULL | -            | UNIQUE                     | 優惠券代碼（唯一）           |
| CouponTypeID  | int       | -    | NOT NULL | -            | FK→CouponType.CouponTypeID | 優惠券類型                   |
| UserID        | int       | -    | NOT NULL | -            | FK→Users.User_ID           | 使用者識別碼                 |
| IsUsed        | bit       | -    | NOT NULL | 0            | CK_Coupon_IsUsed           | 是否已使用（0=未用, 1=已用） |
| AcquiredTime  | datetime2 | 7    | NOT NULL | GETUTCDATE() | -                          | 獲得時間                     |
| UsedTime      | datetime2 | 7    | YES      | NULL         | -                          | 使用時間（已使用才有值）     |
| UsedInOrderID | int       | YES  | NULL     | -            | -                          | 使用的訂單 ID                |
| IsDeleted     | bit       | -    | NOT NULL | 0            | -                          | 軟刪除標記                   |

**主要約束**:

- **PK**: CouponID
- **FK**: CouponTypeID → CouponType.CouponTypeID
- **FK**: UserID → Users.User_ID
- **UNIQUE**: CouponCode
- **IDENTITY**: CouponID

**CHECK 約束**:

- `CK_Coupon_IsUsed`: IsUsed IN (0, 1)
- `CK_Coupon_UsedFields`: (IsUsed = 0 AND UsedTime IS NULL AND UsedInOrderID IS NULL) OR (IsUsed = 1 AND UsedTime IS NOT NULL AND UsedInOrderID IS NOT NULL)

**種子資料統計** (UserID 10000001 和 10000002):

- 10000001 擁有 13 張優惠券（全未使用）
- 10000002 擁有 12 張優惠券（全未使用）

---

### 8. CouponType 表

**用途**: 定義優惠券類型和折扣規則

**表結構**:

| 欄位名稱      | 資料型態  | 長度 | 可否為空 | 預設值 | 約束              | 備註                             |
| ------------- | --------- | ---- | -------- | ------ | ----------------- | -------------------------------- |
| CouponTypeID  | int       | -    | NOT NULL | -      | PK, IDENTITY(1,1) | 優惠券類型 ID                    |
| Name          | nvarchar  | 100  | NULL     | -      | -                 | 優惠券名稱                       |
| DiscountType  | nvarchar  | 20   | NULL     | -      | CK_DiscountType   | 折扣類型（Amount/Percent）       |
| DiscountValue | decimal   | 18,2 | YES      | NULL   | -                 | 折扣值（金額或百分比）           |
| MinSpend      | decimal   | 18,2 | YES      | NULL   | -                 | 最小消費金額                     |
| ValidFrom     | datetime2 | 7    | NULL     | -      | -                 | 有效期開始                       |
| ValidTo       | datetime2 | 7    | NULL     | -      | -                 | 有效期結束                       |
| PointsCost    | int       | -    | NULL     | -      | -                 | 點數成本（購買優惠券需要的點數） |
| Description   | nvarchar  | 500  | YES      | NULL   | -                 | 說明                             |
| IsDeleted     | bit       | -    | NOT NULL | 0      | -                 | 軟刪除標記                       |

**主要約束**:

- **PK**: CouponTypeID
- **IDENTITY**: CouponTypeID (種子: 1, 增量: 1)

**CHECK 約束**:

- `CK_DiscountType`: DiscountType IN ('Amount', 'Percent')

**種子資料** (3 筆):

| CouponTypeID | Name         | DiscountType | DiscountValue | MinSpend | PointsCost | ValidFrom           | ValidTo             |
| ------------ | ------------ | ------------ | ------------- | -------- | ---------- | ------------------- | ------------------- |
| 1            | 免費運費     | Amount       | NULL          | NULL     | 10000      | 2023-10-26 02:09:44 | 2026-06-30 23:59:59 |
| 2            | 滿額折 85 折 | Percent      | 0.15          | 1500.00  | 1000       | 2023-01-25 14:06:52 | 2026-06-30 23:59:59 |
| 3            | 滿$500 折$50 | Amount       | 50.00         | 500.00   | 5000       | 2024-11-13 10:37:53 | 2026-06-30 23:59:59 |

---

## 電子禮券系統

### 9. EVoucher 表

**用途**: 儲存會員電子禮券

**表結構**:

| 欄位名稱       | 資料型態  | 長度 | 可否為空 | 預設值       | 約束                           | 備註             |
| -------------- | --------- | ---- | -------- | ------------ | ------------------------------ | ---------------- |
| EVoucherID     | int       | -    | NOT NULL | -            | PK, IDENTITY                   | 電子禮券 ID      |
| EVoucherCode   | nvarchar  | 50   | NOT NULL | -            | UNIQUE                         | 禮券代碼（唯一） |
| EVoucherTypeID | int       | -    | NOT NULL | -            | FK→EVoucherType.EVoucherTypeID | 禮券類型         |
| UserID         | int       | -    | NOT NULL | -            | FK→Users.User_ID               | 使用者識別碼     |
| IsUsed         | bit       | -    | NOT NULL | 0            | -                              | 是否已使用       |
| AcquiredTime   | datetime2 | 7    | NOT NULL | GETUTCDATE() | -                              | 取得時間         |
| UsedTime       | datetime2 | 7    | YES      | NULL         | -                              | 使用時間         |
| IsDeleted      | bit       | -    | NOT NULL | 0            | -                              | 軟刪除標記       |

**主要約束**:

- **PK**: EVoucherID
- **FK**: EVoucherTypeID → EVoucherType.EVoucherTypeID
- **FK**: UserID → Users.User_ID
- **UNIQUE**: EVoucherCode
- **IDENTITY**: EVoucherID

**種子資料統計**:

- 10000001 擁有 3 張（1 張已使用, 2 張未使用）
- 10000002 擁有 1 張（1 張已使用）

---

### 10. EVoucherType 表

**用途**: 定義電子禮券類型和面額

**表結構**:

| 欄位名稱       | 資料型態  | 長度 | 可否為空 | 預設值 | 約束              | 備註         |
| -------------- | --------- | ---- | -------- | ------ | ----------------- | ------------ |
| EVoucherTypeID | int       | -    | NOT NULL | -      | PK, IDENTITY(1,1) | 禮券類型 ID  |
| Name           | nvarchar  | 100  | NULL     | -      | -                 | 禮券名稱     |
| ValueAmount    | decimal   | 18,2 | NULL     | -      | -                 | 禮券面額     |
| ValidFrom      | datetime2 | 7    | NULL     | -      | -                 | 有效期開始   |
| ValidTo        | datetime2 | 7    | NULL     | -      | -                 | 有效期結束   |
| PointsCost     | int       | -    | NULL     | -      | -                 | 購買所需點數 |
| TotalAvailable | int       | -    | NULL     | 0      | -                 | 可用總量     |
| Description    | nvarchar  | 500  | YES      | NULL   | -                 | 說明         |
| IsDeleted      | bit       | -    | NOT NULL | 0      | -                 | 軟刪除標記   |

**主要約束**:

- **PK**: EVoucherTypeID
- **IDENTITY**: EVoucherTypeID (種子: 1, 增量: 1)

**種子資料** (20 筆):
包含便利商店禮券、百貨禮券、餐飲禮券、電影票、飲品等

代表樣本:

- EVoucherTypeID 1: 7-11 禮券$100 (10000 點, 468 張可用)
- EVoucherTypeID 3: 全家禮券$100 (10000 點, 194 張可用)
- EVoucherTypeID 7: 美麗華電影票券 (36000 點, 356 張可用)
- EVoucherTypeID 15: 酷聖石冰淇淋 (14500 點, 438 張可用)

---

### 11. EVoucherToken 表

**用途**: 儲存電子禮券的兌換 Token

**表結構**:

| 欄位名稱   | 資料型態  | 長度 | 可否為空 | 預設值 | 約束                   | 備註               |
| ---------- | --------- | ---- | -------- | ------ | ---------------------- | ------------------ |
| TokenID    | int       | -    | NOT NULL | -      | PK, IDENTITY           | Token 識別碼       |
| EVoucherID | int       | -    | NOT NULL | -      | FK→EVoucher.EVoucherID | 禮券 ID            |
| Token      | nvarchar  | 50   | NULL     | -      | UNIQUE                 | Token 值（核銷用） |
| ExpiresAt  | datetime2 | 7    | NULL     | -      | -                      | Token 過期時間     |
| IsRevoked  | bit       | -    | NOT NULL | 0      | -                      | 是否已撤銷         |
| IsDeleted  | bit       | -    | NOT NULL | 0      | -                      | 軟刪除標記         |

**主要約束**:

- **PK**: TokenID
- **FK**: EVoucherID → EVoucher.EVoucherID
- **UNIQUE**: Token
- **IDENTITY**: TokenID

**種子資料樣本** (4 筆):

| TokenID | EVoucherID | Token             | IsRevoked | ExpiresAt           |
| ------- | ---------- | ----------------- | --------- | ------------------- |
| 1       | 1          | TKN-GFWZIUGU-7603 | 0         | 2024-12-09 15:17:44 |
| 2       | 2          | TKN-0AFNJ3IW-7410 | 0         | 2025-04-08 07:58:55 |
| 3       | 3          | TKN-QBHYOJ30-9972 | 0         | 2025-08-05 09:01:17 |
| 4       | 4          | TKN-L62G3NV4-9235 | 1         | 2025-05-21 15:30:47 |

---

### 12. EVoucherRedeemLog 表

**用途**: 記錄電子禮券的核銷歷史

**表結構**:

| 欄位名稱   | 資料型態  | 長度 | 可否為空 | 預設值       | 約束                   | 備註          |
| ---------- | --------- | ---- | -------- | ------------ | ---------------------- | ------------- |
| LogID      | int       | -    | NOT NULL | -            | PK, IDENTITY           | 日誌識別碼    |
| EVoucherID | int       | -    | NOT NULL | -            | FK→EVoucher.EVoucherID | 禮券 ID       |
| ScannedAt  | datetime2 | 7    | NOT NULL | GETUTCDATE() | -                      | 掃描/核銷時間 |
| ScannedBy  | nvarchar  | 256  | YES      | NULL         | -                      | 核銷者帳號    |
| StoreCode  | nvarchar  | 50   | YES      | NULL         | -                      | 店鋪代碼      |
| IsDeleted  | bit       | -    | NOT NULL | 0            | -                      | 軟刪除標記    |

**主要約束**:

- **PK**: LogID
- **FK**: EVoucherID → EVoucher.EVoucherID
- **IDENTITY**: LogID

**種子資料統計**:

- UserID 10000001 和 10000002 無記錄（電子禮券尚未在實體店核銷）

---

## 簽到系統

### 13. UserSignInStats 表

**用途**: 記錄會員每日簽到日誌

**表結構**:

| 欄位名稱     | 資料型態  | 可否為空 | 預設值   | 約束             | 備註         |
| ------------ | --------- | -------- | -------- | ---------------- | ------------ | -------------- |
| LogID        | int       | NOT NULL | -        | PK, IDENTITY     | 簽到日誌 ID  |
| SignTime     | datetime2 | 7        | NOT NULL | -                | -            | 簽到時間       |
| UserID       | int       | NOT NULL | -        | FK→Users.User_ID | 使用者識別碼 |
| PointsGained | int       | NOT NULL | 0        | -                | 獲得點數     |
| ExpGained    | int       | NOT NULL | 0        | -                | 獲得經驗值   |
| CouponGained | nvarchar  | 100      | YES      | NULL             | -            | 獲得優惠券代碼 |
| IsDeleted    | bit       | NOT NULL | 0        | -                | 軟刪除標記   |

**主要約束**:

- **PK**: LogID
- **FK**: UserID → Users.User_ID
- **IDENTITY**: LogID

**種子資料統計**:

- 10000001 共 50+ 筆簽到記錄 (2024-01-15 起)
- 10000002 共 50+ 筆簽到記錄 (2024-01-20 起)

---

### 14. SignInRule 表

**用途**: 定義簽到獎勵規則

**表結構**:

| 欄位名稱       | 資料型態 | 可否為空 | 預設值 | 約束              | 備註               |
| -------------- | -------- | -------- | ------ | ----------------- | ------------------ | -------------- |
| Id             | int      | NOT NULL | -      | PK, IDENTITY(1,1) | 規則 ID            |
| SignInDay      | int      | NOT NULL | -      | -                 | 簽到天數（第幾天） |
| Points         | int      | NOT NULL | 0      | -                 | 獲得點數           |
| Experience     | int      | NOT NULL | 0      | -                 | 獲得經驗值         |
| HasCoupon      | bit      | NOT NULL | 0      | -                 | 是否發放優惠券     |
| CouponTypeCode | nvarchar | 50       | YES    | NULL              | -                  | 優惠券類型代碼 |
| IsActive       | bit      | NOT NULL | 1      | -                 | 規則是否啟用       |
| Description    | nvarchar | 500      | YES    | NULL              | -                  | 說明           |
| IsDeleted      | bit      | NOT NULL | 0      | -                 | 軟刪除標記         |

**主要約束**:

- **PK**: Id
- **IDENTITY**: Id (種子: 1, 增量: 1)

**CHECK 約束**:

- `CK_SignInDay`: SignInDay > 0
- `CK_Points`: Points >= 0
- `CK_Experience`: Experience >= 0

**種子資料** (10 筆):

| Id  | SignInDay | Points | Experience | HasCoupon | Description                |
| --- | --------- | ------ | ---------- | --------- | -------------------------- |
| 1   | 1         | 20     | 0          | 0         | 第 1 天簽到規則            |
| 2   | 2         | 20     | 0          | 0         | 第 2 天簽到規則            |
| 3   | 3         | 20     | 0          | 0         | 第 3 天簽到規則            |
| 4   | 4         | 20     | 0          | 0         | 第 4 天簽到規則            |
| 5   | 5         | 20     | 0          | 0         | 第 5 天簽到規則            |
| 6   | 6         | 30     | 200        | 0         | 第 6 天簽到規則            |
| 7   | 7         | 70     | 500        | 0         | 第 7 天簽到規則 + 連續獎勵 |
| 10  | 30        | 200    | 2000       | 0         | 連續簽到 30 天獎勵         |
| 11  | 14        | 0      | 0          | 0         | 連續簽到 14 天獎勵         |
| 12  | 21        | 0      | 0          | 0         | 連續簽到 21 天獎勵         |

---

## 寵物系統

### 15. Pet 表

**用途**: 儲存會員的寵物資訊和狀態

**表結構**:

| 欄位名稱                      | 資料型態  | 可否為空 | 預設值 | 約束             | 備註              |
| ----------------------------- | --------- | -------- | ------ | ---------------- | ----------------- | ---------------------- |
| PetID                         | int       | NOT NULL | -      | PK, IDENTITY     | 寵物 ID           |
| UserID                        | int       | NOT NULL | -      | FK→Users.User_ID | 使用者識別碼      |
| PetName                       | nvarchar  | 50       | NULL   | -                | -                 | 寵物名稱               |
| Level                         | int       | NOT NULL | 1      | CK_Level         | 寵物等級（1-250） |
| Experience                    | int       | NOT NULL | 0      | -                | 當前經驗值        |
| Hunger                        | int       | NOT NULL | 50     | CK_Range         | 飢餓度（0-100）   |
| Mood                          | int       | NOT NULL | 50     | CK_Range         | 心情（0-100）     |
| Stamina                       | int       | NOT NULL | 50     | CK_Range         | 體力（0-100）     |
| Cleanliness                   | int       | NOT NULL | 50     | CK_Range         | 清潔度（0-100）   |
| Health                        | int       | NOT NULL | 100    | CK_Range         | 健康度（0-100）   |
| SkinColor                     | nvarchar  | 20       | NULL   | -                | -                 | 膚色代碼（如 #FFFF00） |
| SkinColorChangedTime          | datetime2 | 7        | YES    | NULL             | -                 | 膚色變更時間           |
| BackgroundColor               | nvarchar  | 20       | NULL   | -                | -                 | 背景代碼（如 BG005）   |
| BackgroundColorChangedTime    | datetime2 | 7        | YES    | NULL             | -                 | 背景變更時間           |
| PointsChanged_SkinColor       | int       | NOT NULL | 0      | -                | 膚色消費點數      |
| PointsChanged_BackgroundColor | int       | NOT NULL | 0      | -                | 背景消費點數      |
| PointsGained_LevelUp          | int       | NOT NULL | 0      | -                | 升級獲得點數      |
| CurrentExperience             | int       | NOT NULL | 0      | -                | 當前級別經驗進度  |
| ExperienceToNextLevel         | int       | NOT NULL | 100    | -                | 升下級需經驗值    |
| TotalPointsGained_LevelUp     | int       | NOT NULL | 0      | -                | 累計升級獲得點數  |
| IsDeleted                     | bit       | NOT NULL | 0      | -                | 軟刪除標記        |

**主要約束**:

- **PK**: PetID
- **FK**: UserID → Users.User_ID
- **IDENTITY**: PetID

**CHECK 約束**:

- `CK_Level`: Level BETWEEN 1 AND 250
- `CK_Range`: Hunger, Mood, Stamina, Cleanliness BETWEEN 0 AND 100
- `CK_Health`: Health BETWEEN 0 AND 100

**種子資料樣本** (UserID 10000001 和 10000002):

| PetID | UserID   | PetName | Level | Experience | Hunger | Mood | Stamina | Cleanliness | Health | SkinColor | BackgroundColor |
| ----- | -------- | ------- | ----- | ---------- | ------ | ---- | ------- | ----------- | ------ | --------- | --------------- |
| 1     | 10000001 | 多多    | 4     | 656        | 14     | 58   | 89      | 25          | 100    | #FFFF00   | BG005           |
| 2     | 10000002 | 小小    | 38    | 4019       | 55     | 15   | 57      | 14          | 94     | #800080   | BG008           |

---

### 16. PetSkinColorCostSettings 表

**用途**: 定義寵物膚色購買成本

**表結構**:

| 欄位名稱         | 資料型態 | 長度     | 可否為空 | 預設值 | 約束              | 備註                     |
| ---------------- | -------- | -------- | -------- | ------ | ----------------- | ------------------------ |
| SettingId        | int      | -        | NOT NULL | -      | PK, IDENTITY(1,1) | 設定 ID                  |
| ColorCode        | nvarchar | 20       | NULL     | -      | UNIQUE            | 顏色代碼（如 #FFFF00）   |
| ColorName        | nvarchar | 50       | NULL     | -      | -                 | 顏色名稱                 |
| PointsCost       | int      | NOT NULL | 0        | -      | 購買成本（點數）  |
| Rarity           | nvarchar | 20       | NULL     | -      | -                 | 稀有度（普通/稀有/限定） |
| Description      | nvarchar | 500      | YES      | NULL   | -                 | 說明                     |
| IsFree           | bit      | NOT NULL | 0        | -      | 是否免費          |
| IsActive         | bit      | NOT NULL | 1        | -      | 是否啟用          |
| IsLimitedEdition | bit      | NOT NULL | 0        | -      | 是否限定版本      |
| IsDeleted        | bit      | NOT NULL | 0        | -      | 軟刪除標記        |

**主要約束**:

- **PK**: SettingId
- **UNIQUE**: ColorCode
- **IDENTITY**: SettingId (種子: 1, 增量: 1)

**種子資料** (11 筆):

| SettingId | ColorCode | ColorName | PointsCost | Rarity | IsFree | IsActive | IsLimitedEdition |
| --------- | --------- | --------- | ---------- | ------ | ------ | -------- | ---------------- |
| 1         | #FFFFFF   | 白色      | 0          | 普通   | 1      | 1        | 0                |
| 2         | #000000   | 黑色      | 0          | 普通   | 1      | 1        | 0                |
| 3         | #FF0000   | 紅色      | 0          | 普通   | 1      | 1        | 0                |
| 4         | #FFA500   | 橙色      | 2000       | 普通   | 0      | 1        | 0                |
| 5         | #FFFF00   | 黃色      | 2000       | 普通   | 0      | 1        | 0                |
| 6         | #008000   | 綠色      | 2000       | 普通   | 0      | 1        | 0                |
| 7         | #00FFFF   | 青色      | 2000       | 普通   | 0      | 1        | 0                |
| 8         | #0000FF   | 藍色      | 2000       | 普通   | 0      | 1        | 0                |
| 9         | #800080   | 紫色      | 3500       | 稀有   | 0      | 1        | 0                |
| 10        | #6F4E37   | 咖啡色    | 3500       | 稀有   | 0      | 1        | 0                |
| 11        | #6EFE19   | 淺綠色    | 2000       | 限定   | 0      | 0        | 1                |

---

### 17. PetBackgroundCostSettings 表

**用途**: 定義寵物背景購買成本

**表結構**:

| 欄位名稱       | 資料型態 | 長度     | 可否為空 | 預設值 | 約束              | 備註                 |
| -------------- | -------- | -------- | -------- | ------ | ----------------- | -------------------- |
| SettingId      | int      | -        | NOT NULL | -      | PK, IDENTITY(1,1) | 設定 ID              |
| BackgroundCode | nvarchar | 20       | NULL     | -      | UNIQUE            | 背景代碼（如 BG005） |
| BackgroundName | nvarchar | 100      | NULL     | -      | -                 | 背景名稱             |
| PointsCost     | int      | NOT NULL | 0        | -      | 購買成本（點數）  |
| Description    | nvarchar | 500      | YES      | NULL   | -                 | 說明                 |
| ImagePath      | nvarchar | 500      | YES      | NULL   | -                 | 圖片路徑             |
| IsActive       | bit      | NOT NULL | 1        | -      | 是否啟用          |
| SortOrder      | int      | NOT NULL | 0        | -      | 排序順序          |
| IsDeleted      | bit      | NOT NULL | 0        | -      | 軟刪除標記        |

**主要約束**:

- **PK**: SettingId
- **UNIQUE**: BackgroundCode
- **IDENTITY**: SettingId (種子: 1, 增量: 1)

**種子資料** (11 筆):

| SettingId | BackgroundCode | BackgroundName | PointsCost | IsActive | IsDeleted |
| --------- | -------------- | -------------- | ---------- | -------- | --------- |
| 19        | BG001          | 萬聖節南瓜     | 0          | 1        | 0         |
| 20        | BG002          | 教堂彩窗       | 0          | 1        | 0         |
| 21        | BG003          | 珊瑚海灘       | 0          | 1        | 0         |
| 22        | BG004          | 清新森林       | 2000       | 1        | 0         |
| 23        | BG005          | 熱帶瀑布       | 2500       | 1        | 0         |
| 24        | BG006          | 早晨教室       | 3000       | 1        | 0         |
| 25        | BG007          | 霓虹夜景       | 3500       | 1        | 0         |
| 26        | BG008          | 極光雪原       | 4000       | 1        | 0         |
| 27        | BG009          | 魔法圖書館     | 4500       | 1        | 0         |
| 28        | BG010          | 地獄熔岩       | 6000       | 1        | 0         |
| 29        | BG011          | 蒸汽工廠       | 2000       | 0        | 1         |

---

### 18. PetLevelRewardSettings 表

**用途**: 定義寵物升級獎勵規則

**表結構**:

| 欄位名稱        | 資料型態 | 可否為空 | 預設值 | 約束              | 備註         |
| --------------- | -------- | -------- | ------ | ----------------- | ------------ | ---- |
| SettingId       | int      | NOT NULL | -      | PK, IDENTITY(1,1) | 設定 ID      |
| LevelRangeStart | int      | NOT NULL | -      | -                 | 級別範圍開始 |
| LevelRangeEnd   | int      | NOT NULL | -      | -                 | 級別範圍結束 |
| PointsReward    | int      | NOT NULL | 0      | -                 | 升級獲得點數 |
| Description     | nvarchar | 500      | YES    | NULL              | -            | 說明 |
| IsActive        | bit      | NOT NULL | 1      | -                 | 是否啟用     |
| IsDeleted       | bit      | NOT NULL | 0      | -                 | 軟刪除標記   |

**主要約束**:

- **PK**: SettingId
- **IDENTITY**: SettingId (種子: 1, 增量: 1)

**CHECK 約束**:

- `CK_LevelRange`: LevelRangeStart <= LevelRangeEnd
- `CK_PointsReward`: PointsReward >= 0

**種子資料** (25 筆):
涵蓋 Level 1-10 到 Level 241-250 的升級獎勵：

| SettingId | LevelRangeStart | LevelRangeEnd | PointsReward | Description          |
| --------- | --------------- | ------------- | ------------ | -------------------- |
| 1         | 1               | 10            | 10           | 新手獎勵             |
| 2         | 11              | 20            | 20           | 中階獎勵             |
| 3         | 21              | 30            | 30           | 高階獎勵             |
| ...       | ...             | ...           | ...          | ...                  |
| 25        | 241             | 250           | 250          | 超聖至高獎勵(封頂級) |

---

## 小遊戲系統

### 19. MiniGame 表

**用途**: 記錄遊戲進度和結果

**表結構**:

| 欄位名稱        | 資料型態  | 可否為空 | 預設值   | 約束             | 備註                   |
| --------------- | --------- | -------- | -------- | ---------------- | ---------------------- |
| PlayID          | int       | NOT NULL | -        | PK, IDENTITY     | 遊戲紀錄 ID            |
| UserID          | int       | NOT NULL | -        | FK→Users.User_ID | 使用者識別碼           |
| PetID           | int       | NOT NULL | -        | FK→Pet.PetID     | 寵物 ID                |
| Level           | int       | NOT NULL | 1        | CK_Level         | 遊戲難度（1-3）        |
| MonsterCount    | int       | NOT NULL | 6        | -                | 怪物數量               |
| SpeedMultiplier | decimal   | NOT NULL | 1.0      | -                | 速度倍數               |
| Result          | nvarchar  | 20       | NULL     | CK_Result        | 結果（Win/Lose/Abort） |
| ExpGained       | int       | NOT NULL | 0        | -                | 獲得經驗值             |
| PointsGained    | int       | NOT NULL | 0        | -                | 獲得點數               |
| StartTime       | datetime2 | 7        | NOT NULL | -                | 開始時間               |
| EndTime         | datetime2 | 7        | NULL     | -                | 結束時間               |
| Aborted         | bit       | NOT NULL | 0        | -                | 是否中途放棄           |
| IsDeleted       | bit       | NOT NULL | 0        | -                | 軟刪除標記             |

**主要約束**:

- **PK**: PlayID
- **FK**: UserID → Users.User_ID
- **FK**: PetID → Pet.PetID
- **IDENTITY**: PlayID

**CHECK 約束**:

- `CK_Level`: Level IN (1, 2, 3)
- `CK_Result`: Result IN ('Win', 'Lose', 'Abort')
- `CK_MonsterCount`: MonsterCount > 0

**種子資料統計**:

- 10000001: 11 筆遊戲記錄（4 勝 6 負 1 中斷）
- 10000002: 12 筆遊戲記錄（5 勝 7 負）

---

## 系統設定

### 20. SystemSettings 表

**用途**: 動態配置中心，存儲系統參數

**表結構**:

| 欄位名稱     | 資料型態 | 長度     | 可否為空 | 預設值 | 約束              | 備註                                  |
| ------------ | -------- | -------- | -------- | ------ | ----------------- | ------------------------------------- |
| SettingId    | int      | -        | NOT NULL | -      | PK, IDENTITY(1,1) | 設定 ID                               |
| SettingKey   | nvarchar | 256      | NOT NULL | -      | UNIQUE            | 設定鍵（如 Game.Level1.MonsterCount） |
| SettingValue | nvarchar | max      | NOT NULL | -      | -                 | 設定值（支援 JSON）                   |
| Description  | nvarchar | 500      | YES      | NULL   | -                 | 設定說明                              |
| Category     | nvarchar | 50       | NULL     | -      | -                 | 分類（Game/Pet/SignIn/Wallet）        |
| SettingType  | nvarchar | 50       | NULL     | -      | CK_Type           | 型態（Number/String/Boolean/JSON）    |
| IsReadOnly   | bit      | NOT NULL | 0        | -      | 是否唯讀          |
| IsActive     | bit      | NOT NULL | 1        | -      | 是否啟用          |

**主要約束**:

- **PK**: SettingId
- **UNIQUE**: SettingKey
- **IDENTITY**: SettingId (種子: 1, 增量: 1)

**CHECK 約束**:

- `CK_Type`: SettingType IN ('Number', 'String', 'Boolean', 'JSON')

**種子資料統計** (56 筆):

**Game 類別** (24 筆):

- 3 個遊戲難度設定（每個難度的怪物數量、速度倍數、經驗值獎勵、點數獎勵）
- 8 個遊戲結果狀態更新參數（贏/輸時的飢餓度、心情、體力、清潔度變化）
- 2 個額外設定

代表樣本:

- Game.DefaultDailyLimit: 3
- Game.Level1.MonsterCount: 6
- Game.Level1.SpeedMultiplier: 1.0
- Game.Level1.ExperienceReward: 100
- Game.Result.Win.MoodDelta: 30
- Game.Result.Lose.MoodDelta: -30

**Pet 類別** (17 筆):

- 寵物互動效果（餵食、洗澡、安撫、休息）
- 寵物日常衰減（飢餓度、心情、體力、清潔度、健康度）
- 升級相關設定

代表樣本:

- Pet.Interaction.Feed.HungerIncrease: 10
- Pet.DailyDecay.HungerDecay: 20
- Pet.LevelUp.Formula: {JSON}

**SignIn 類別** (11 筆):

- 平日/假日簽到獎勵
- 連續 7 天簽到加成
- 完全出勤（30 天）加成

代表樣本:

- SignIn.Weekday.Points: 20
- SignIn.Streak7Days.BonusExperience: 300
- SignIn.PerfectAttendance30Days.BonusPoints: 200

**Wallet/Coupon/EVoucher 類別** (4 筆):

- Wallet.MaxPoints: 999999
- Wallet.InitialPoints: 1000
- Coupon.DefaultValidityDays: 30
- EVoucher.DefaultValidityDays: 90

---

## 資料關聯性圖

```
Users (200 筆)
  ├─→ User_Wallet (1:1)
  ├─→ WalletHistory (1:N)
  ├─→ Coupon (1:N)
  │     └─→ CouponType (N:1)
  ├─→ EVoucher (1:N)
  │     ├─→ EVoucherType (N:1)
  │     └─→ EVoucherToken (1:N)
  │           └─→ EVoucherRedeemLog (1:N)
  ├─→ UserSignInStats (1:N)
  ├─→ Pet (1:N)
  │     ├─→ PetSkinColorCostSettings (N:1)
  │     └─→ PetBackgroundCostSettings (N:1)
  └─→ MiniGame (1:N)
        ├─→ Pet (N:1)
        └─→ (遊戲難度由 SystemSettings 控制)

ManagerData (102 筆)
  └─→ ManagerRole (N:1)
        └─→ ManagerRolePermission (N:1)

Configuration Tables:
  - SignInRule (10 筆)
  - PetLevelRewardSettings (25 筆)
  - SystemSettings (56 筆)
```

---

## 資料完整性規則

### 外鍵關聯驗證

- ✅ 所有 Coupon.CouponTypeID 指向有效 CouponType
- ✅ 所有 EVoucher.EVoucherTypeID 指向有效 EVoucherType
- ✅ 所有 User_Wallet.User_Id 指向有效 Users
- ✅ 所有 Pet.UserID 指向有效 Users
- ✅ 所有 MiniGame.UserID 和 PetID 指向有效使用者和寵物

### 軟刪除機制

- 所有表均支援軟刪除
- 標準欄位: IsDeleted (bit), DeletedAt (datetime2), DeletedBy (nvarchar), DeleteReason (nvarchar)
- 應用層應過濾 IsDeleted = 0 的記錄

### CHECK 約束規則

- 年齡/等級/狀態值範圍驗證
- 金額/點數非負值驗證
- 邏輯一致性驗證（如使用優惠券時 IsUsed 和 UsedTime 必須同時有值）

---

## 種子資料統計匯總

| 表名                      | 用途           | 總記錄數  | 備註                          |
| ------------------------- | -------------- | --------- | ----------------------------- |
| Users                     | 遊戲使用者     | 200       | User_ID 10000001-10000200     |
| ManagerData               | 管理員         | 102       | Manager_Id 30000001-30000102  |
| ManagerRole               | 管理員角色指派 | 102       | 8 種角色分配                  |
| ManagerRolePermission     | 角色權限定義   | 8         | 6 個權限維度                  |
| User_Wallet               | 會員錢包       | 200+      | 動態，隨使用者增加            |
| WalletHistory             | 錢包交易歷史   | 5000+     | 高頻寫入                      |
| Coupon                    | 優惠券所有權   | 500+      | 10000001/10000002 各 13/12 張 |
| CouponType                | 優惠券類型     | 3         | 免費運費、85 折、滿額折扣     |
| EVoucher                  | 電子禮券所有權 | 100+      | 10000001/10000002 各 3/1 張   |
| EVoucherType              | 電子禮券類型   | 20        | 便利商店、百貨、餐飲等        |
| EVoucherToken             | 禮券核銷 Token | 100+      | 與 EVoucher 一對一            |
| EVoucherRedeemLog         | 禮券核銷歷史   | 0 (當前)  | 店員核銷記錄                  |
| UserSignInStats           | 簽到歷史       | 5000+     | 高頻寫入                      |
| SignInRule                | 簽到獎勵規則   | 10        | 配置表                        |
| Pet                       | 寵物資訊       | 200+      | 每使用者最多 1 隻             |
| PetSkinColorCostSettings  | 膚色價格       | 11        | 配置表                        |
| PetBackgroundCostSettings | 背景價格       | 11        | 配置表                        |
| PetLevelRewardSettings    | 升級獎勵       | 25        | 支援 Level 1-250              |
| MiniGame                  | 遊戲記錄       | 1000+     | 高頻寫入                      |
| SystemSettings            | 系統配置       | 56        | 動態參數中心                  |
| **總計**                  |                | **2000+** | 配置表 67 + 使用者資料 1900+  |

---

## 設計重點

### 1. 軟刪除架構

所有業務表均支援軟刪除，保留審計軌跡，不直接物理刪除資料

### 2. 動態配置中心

SystemSettings 表存儲 56 個可調整參數，無需修改程式碼即可調整遊戲規則

### 3. 點數經濟系統

完整追蹤點數流向（User_Point 當前餘額 + WalletHistory 完整歷史）

### 4. 多層級獎勵機制

- 簽到獎勵 (SignInRule)
- 升級獎勵 (PetLevelRewardSettings)
- 遊戲獎勵 (MiniGame 記錄)
- 系統設定參數化 (SystemSettings)

### 5. 寵物養成系統

完整記錄寵物屬性、升級進度、外觀自訂（膚色、背景）

### 6. 角色權限模型

8 個預定義角色 + 6 個權限維度 = 靈活的權限管理組合

---

**文檔版本**: 1.0
**最後更新**: 2025-11-05
**作者**: Claude Code (Anthropic)
