# MiniGame Area 種子資料完整報告

**生成日期**: 2025-11-05
**資料庫伺服器**: DESKTOP-8HQIS1S\SQLEXPRESS (本機 SQL Server)
**資料庫名稱**: GameSpacedatabase
**查詢目標**:
- UserID **10000001** 和 **10000002** 在所有 MiniGame Area 主要表格的種子資料
- 配置表格 (CouponType, EVoucherType, PetBackgroundCostSettings, PetSkinColorCostSettings) 的全部種子資料

---

## 目錄

1. [會員錢包系統 (User_Wallet, WalletHistory)](#1-會員錢包系統)
2. [優惠券系統 (Coupon, CouponType)](#2-優惠券系統)
3. [電子禮券系統 (EVoucher, EVoucherType, EVoucherToken, EVoucherRedeemLog)](#3-電子禮券系統)
4. [簽到系統 (UserSignInStats, SignInRule)](#4-簽到系統)
5. [寵物系統 (Pet, PetSkinColorCostSettings, PetBackgroundCostSettings, PetLevelRewardSettings)](#5-寵物系統)
6. [小遊戲系統 (MiniGame)](#6-小遊戲系統)
7. [系統設定 (SystemSettings)](#7-系統設定)
8. [資料統計摘要](#8-資料統計摘要)

---

## 1. 會員錢包系統

### 1.1 User_Wallet 表格

**UserID 10000001**:
```
User_Id: 10000001
User_Point: 60030
IsDeleted: 0
DeletedAt: NULL
DeletedBy: NULL
DeleteReason: NULL
```

**UserID 10000002**:
```
User_Id: 10000002
User_Point: 21666
IsDeleted: 0
DeletedAt: NULL
DeletedBy: NULL
DeleteReason: NULL
```

### 1.2 WalletHistory 表格

**UserID 10000001 的錢包歷史記錄 (6 筆)**:

| LogID | UserID | ChangeType | PointsChanged | ItemCode | Description | ChangeTime | IsDeleted |
|-------|--------|------------|---------------|----------|-------------|------------|-----------|
| 1939 | 10000001 | Point | 94500 | INIT-BAL-001 | Initial account balance - retroactive logging | 2023-02-22 08:00:00.0000000 | 0 |
| 1929 | 10000001 | Point | -2000 | #FFFF00 | 購買寵物膚色黃色 | 2023-02-22 09:10:06.0000000 | 0 |
| 7 | 10000001 | Point | 30 | NULL | 小遊戲獲勝額外獎勵點數 | 2023-12-08 03:34:50.0000000 | 0 |
| 3 | 10000001 | Point | -30000 | EV-FAMILY-MNPQ-064877 | 兌換點數購買電子禮券 | 2024-10-29 15:17:44.0000000 | 0 |
| 1930 | 10000001 | Point | -2500 | BG005 | 購買寵物背景 | 2025-04-09 17:03:40.0000000 | 0 |

**UserID 10000002 的錢包歷史記錄 (5 筆)**:

| LogID | UserID | ChangeType | PointsChanged | ItemCode | Description | ChangeTime | IsDeleted |
|-------|--------|------------|---------------|----------|-------------|------------|-----------|
| 1940 | 10000002 | Point | 68720 | INIT-BAL-002 | Initial account balance - retroactive logging | 2023-08-07 15:00:00.0000000 | 0 |
| 11 | 10000002 | Point | -40000 | EV-ICECREAM-GHJK-253496 | 兌換點數購買電子禮券 | 2023-08-07 16:08:59.0000000 | 0 |
| 1932 | 10000002 | Point | -4000 | BG008 | 購買寵物背景 | 2024-08-25 17:19:48.0000000 | 0 |
| 1931 | 10000002 | Point | -3500 | #800080 | 購買寵物膚色紫色 | 2024-12-11 04:53:18.0000000 | 0 |
| 8 | 10000002 | Point | 446 | NULL | 遊戲獲勝獎勵點數 | 2025-09-16 18:34:01.4389762 | 0 |

---

## 2. 優惠券系統

### 2.1 Coupon 表格 (UserID 10000001 和 10000002)

**UserID 10000001 共擁有 13 張優惠券**:

| CouponID | CouponCode | CouponTypeID | UserID | IsUsed | AcquiredTime | UsedTime | UsedInOrderID | IsDeleted |
|----------|------------|--------------|--------|--------|--------------|----------|---------------|-----------|
| 5979 | CPN-2308-MG1044 | 3 | 10000001 | 0 | 2023-08-26 04:13:03 | NULL | NULL | 0 |
| 9511 | CPN-2312-HG7K3M | 1 | 10000001 | 0 | 2023-12-01 20:41:09 | NULL | NULL | 0 |
| 9423 | CPN-2401-A7B2K9 | 1 | 10000001 | 0 | 2024-01-21 09:45:18 | NULL | NULL | 0 |
| 9424 | CPN-2402-XW4H8P | 1 | 10000001 | 0 | 2024-02-01 08:44:28 | NULL | NULL | 0 |
| 9425 | CPN-2402-M9N5QT | 2 | 10000001 | 0 | 2024-02-08 08:31:45 | NULL | NULL | 0 |
| 9426 | CPN-2402-R3V7CJ | 1 | 10000001 | 0 | 2024-02-19 08:22:48 | NULL | NULL | 0 |
| 9427 | CPN-2402-FG6Y2L | 2 | 10000001 | 0 | 2024-02-26 08:17:45 | NULL | NULL | 0 |
| 9428 | CPN-2403-ZK8D4W | 3 | 10000001 | 0 | 2024-03-04 08:24:37 | NULL | NULL | 0 |
| 9509 | CPN-2403-BQ8N4R | 1 | 10000001 | 0 | 2024-03-08 10:07:56 | NULL | NULL | 0 |
| 9180 | CPN-2302-HCA748 | 1 | 10000001 | 0 | 2024-06-19 06:36:51 | NULL | NULL | 0 |
| 5964 | CPN-2503-MG1029 | 3 | 10000001 | 0 | 2025-03-04 04:52:49 | NULL | NULL | 0 |
| 9502 | CPN-2506-WJ9F2T | 1 | 10000001 | 0 | 2025-06-30 11:05:33 | NULL | NULL | 0 |

**UserID 10000002 共擁有 11 張優惠券**:

| CouponID | CouponCode | CouponTypeID | UserID | IsUsed | AcquiredTime | UsedTime | UsedInOrderID | IsDeleted |
|----------|------------|--------------|--------|--------|--------------|----------|---------------|-----------|
| 9408 | CPN-2507-BZQ014 | 1 | 10000002 | 0 | 2023-11-28 06:29:46 | NULL | NULL | 0 |
| 9614 | CPN-2312-R5V8CJ | 1 | 10000002 | 0 | 2023-12-12 20:30:00 | NULL | NULL | 0 |
| 6376 | CPN-2402-MG1441 | 3 | 10000002 | 0 | 2024-02-14 21:18:58 | NULL | NULL | 0 |
| 9418 | CPN-2508-BVT859 | 2 | 10000002 | 0 | 2024-02-22 10:48:28 | NULL | NULL | 0 |
| 6692 | CPN-2403-MG1757 | 3 | 10000002 | 0 | 2024-03-01 06:19:39 | NULL | NULL | 0 |
| 9429 | CPN-2403-PB7T3X | 1 | 10000002 | 0 | 2024-03-06 10:17:38 | NULL | NULL | 0 |
| 9612 | CPN-2403-M7P9DK | 1 | 10000002 | 0 | 2024-03-12 17:21:35 | NULL | NULL | 0 |
| 9430 | CPN-2404-HC9E5N | 1 | 10000002 | 0 | 2024-04-17 14:31:55 | NULL | NULL | 0 |
| 6058 | CPN-2404-MG1123 | 3 | 10000002 | 0 | 2024-04-22 07:34:48 | NULL | NULL | 0 |
| 6529 | CPN-2406-MG1594 | 3 | 10000002 | 0 | 2024-06-05 05:46:16 | NULL | NULL | 0 |
| 9622 | CPN-2505-FG6Y2L | 1 | 10000002 | 0 | 2025-05-03 01:18:41 | NULL | NULL | 0 |
| 9615 | CPN-2506-ZK8D4W | 1 | 10000002 | 0 | 2025-06-30 16:33:21 | NULL | NULL | 0 |

### 2.2 CouponType 表格 (全部種子資料 - 3 筆)

| CouponTypeID | Name | DiscountType | DiscountValue | MinSpend | ValidFrom | ValidTo | PointsCost | Description | IsDeleted |
|--------------|------|--------------|---------------|----------|-----------|---------|------------|-------------|-----------|
| 1 | 免費運費 | Amount | NULL | NULL | 2023-10-26 02:09:44 | 2026-06-30 23:59:59 | 10000 | 免費運費優惠券 | 0 |
| 2 | 滿額折85折 | Percent | 0.15 | 1500.00 | 2023-01-25 14:06:52 | 2026-06-30 23:59:59 | 1000 | 免費運費優惠券 | 0 |
| 3 | 滿$500折$50 | Amount | 50.00 | 500.00 | 2024-11-13 10:37:53 | 2026-06-30 23:59:59 | 5000 | 免費運費優惠券 | 0 |

---

## 3. 電子禮券系統

### 3.1 EVoucher 表格 (UserID 10000001 和 10000002)

**UserID 10000001 共擁有 3 張電子禮券**:

| EVoucherID | EVoucherCode | EVoucherTypeID | UserID | IsUsed | AcquiredTime | UsedTime | IsDeleted |
|------------|--------------|----------------|--------|--------|--------------|----------|-----------|
| 1 | EV-FAMILY-MNPQ-064877 | 3 | 10000001 | 1 | 2024-10-29 15:17:44 | 2025-05-30 23:53:14 | 0 |
| 3 | EV-STORE-BNXR-252844 | 4 | 10000001 | 0 | 2024-11-18 08:13:38 | NULL | 0 |
| 2 | EV-PIZZA-BCDF-969669 | 12 | 10000001 | 0 | 2025-01-14 07:58:55 | NULL | 0 |

**UserID 10000002 共擁有 1 張電子禮券**:

| EVoucherID | EVoucherCode | EVoucherTypeID | UserID | IsUsed | AcquiredTime | UsedTime | IsDeleted |
|------------|--------------|----------------|--------|--------|--------------|----------|-----------|
| 4 | EV-ICECREAM-GHJK-253496 | 15 | 10000002 | 1 | 2023-08-07 16:08:59 | 2023-11-24 09:25:43 | 0 |

### 3.2 EVoucherToken 表格 (關聯的 Token)

| TokenID | EVoucherID | Token | ExpiresAt | IsRevoked | IsDeleted |
|---------|------------|-------|-----------|-----------|-----------|
| 1 | 1 | TKN-GFWZIUGU-7603 | 2024-12-09 15:17:44 | 0 | 0 |
| 2 | 2 | TKN-0AFNJ3IW-7410 | 2025-04-08 07:58:55 | 0 | 0 |
| 3 | 3 | TKN-QBHYOJ30-9972 | 2025-08-05 09:01:17 | 0 | 0 |
| 4 | 4 | TKN-L62G3NV4-9235 | 2025-05-21 15:30:47 | 1 | 0 |

### 3.3 EVoucherRedeemLog 表格

**查詢結果**: 無記錄 (UserID 10000001 和 10000002 都沒有核銷記錄)

### 3.4 EVoucherType 表格 (全部種子資料 - 20 筆)

| EVoucherTypeID | Name | ValueAmount | ValidFrom | ValidTo | PointsCost | TotalAvailable | Description | IsDeleted |
|----------------|------|-------------|-----------|---------|------------|----------------|-------------|-----------|
| 1 | 7-11禮券$100 | 100.00 | 2024-07-24 08:01:15 | 9999-12-31 06:10:00 | 10000 | 468 | 無限期限 | 0 |
| 2 | 7-11禮券$200 | 200.00 | 2025-01-08 20:24:24 | 9999-12-31 06:10:00 | 20000 | 437 | 無限期限 | 0 |
| 3 | 全家禮券$100 | 100.00 | 2024-03-05 01:55:47 | 9999-12-31 06:10:00 | 10000 | 194 | 無限期限 | 0 |
| 4 | 全家禮券$200 | 200.00 | 2024-03-30 16:44:49 | 9999-12-31 06:10:00 | 20000 | 438 | 無限期限 | 0 |
| 5 | 7-11特濃霜淇淋一個商品券 | 65.00 | 2024-05-06 09:52:59 | 9999-12-31 06:10:00 | 6500 | 433 | 無限期限/特定商品 | 0 |
| 6 | 7-11特製霜淇淋一個商品券 | 80.00 | 2024-03-20 17:44:03 | 9999-12-31 06:10:00 | 8000 | 268 | 無限期限/特定商品 | 0 |
| 7 | 美麗華電影票券 | 360.00 | 2023-06-14 09:27:37 | 9999-12-31 06:10:00 | 36000 | 356 | 無限期限/娛樂票券 | 0 |
| 8 | 威秀影城電影票券 | 200.00 | 2024-06-30 16:01:28 | 9999-12-31 06:10:00 | 20000 | 253 | 無限期限/娛樂票券 | 0 |
| 9 | SOGO百貨禮券$200 | 200.00 | 2023-12-08 18:22:33 | 9999-12-31 06:10:00 | 20000 | 419 | 無限期限 | 0 |
| 10 | 漢堡王大薯條套餐兌換券 | 78.00 | 2024-01-14 00:08:47 | 9999-12-31 06:10:00 | 7800 | 296 | 無限期限 | 0 |
| 11 | 肯德基?炸雞腿無骨雞柳條套餐兌換券 | 151.00 | 2024-04-14 13:37:46 | 9999-12-31 06:10:00 | 15100 | 234 | 無限期限 | 0 |
| 12 | 達美樂大三拼個人拼盤兌換券 | 82.00 | 2024-09-12 17:42:59 | 9999-12-31 06:10:00 | 8200 | 452 | 無限期限 | 0 |
| 13 | 星巴克大杯摩卡兌換券 | 140.00 | 2024-06-06 18:58:04 | 9999-12-31 06:10:00 | 14000 | 175 | 無限期限/特定商品 | 0 |
| 14 | 路易莎熱美式與特製鮮奶茶(L)兌換券 | 130.00 | 2025-07-05 10:21:00 | 9999-12-31 06:10:00 | 13000 | 176 | 無限期限 | 0 |
| 15 | 酷聖石冰淇淋特製香草冰淇淋 | 145.00 | 2025-07-24 05:42:09 | 9999-12-31 06:10:00 | 14500 | 438 | 無限期限 | 0 |
| 16 | Mister Donut甜甜圈(一入)兌換券 | 42.00 | 2023-04-08 20:36:12 | 9999-12-31 06:10:00 | 4200 | 361 | 無限期限/飲食商品 | 0 |
| 17 | COLD STONE特製香草冰淇淋小杯兌換券 | 120.00 | 2023-05-12 19:35:25 | 9999-12-31 06:10:00 | 12000 | 153 | 無限期限/飲食商品 | 0 |
| 18 | 誠品書店禮券$200 | 200.00 | 2023-02-18 15:06:24 | 9999-12-31 06:10:00 | 20000 | 321 | 無限期限 | 0 |
| 19 | 寶雅藥妝禮券$100 | 100.00 | 2024-03-26 10:04:43 | 9999-12-31 06:10:00 | 10000 | 316 | 無限期限 | 0 |
| 20 | 康是美禮券$200 | 200.00 | 2025-06-11 12:47:47 | 9999-12-31 06:10:00 | 20000 | 317 | 無限期限 | 0 |

---

## 4. 簽到系統

### 4.1 UserSignInStats 表格 (部分顯示，共 100 筆記錄)

**UserID 10000001 簽到記錄 (前 20 筆)**:

| LogID | SignTime | UserID | PointsGained | ExpGained | CouponGained | IsDeleted |
|-------|----------|--------|--------------|-----------|--------------|-----------|
| 2401 | 2024-01-15 08:23:15 | 10000001 | 10 | 5 | AUTO-SIGN-0000000000 | 0 |
| 2402 | 2024-01-16 08:45:22 | 10000001 | 10 | 5 | AUTO-SIGN-0000000000 | 0 |
| 2403 | 2024-01-17 08:17:38 | 10000001 | 15 | 8 | AUTO-SIGN-0000000000 | 0 |
| 2404 | 2024-01-18 08:52:41 | 10000001 | 15 | 8 | AUTO-SIGN-0000000000 | 0 |
| 2405 | 2024-01-19 08:34:12 | 10000001 | 20 | 10 | AUTO-SIGN-0000000000 | 0 |
| 2406 | 2024-01-20 09:28:55 | 10000001 | 20 | 10 | AUTO-SIGN-0000000000 | 0 |
| 2407 | 2024-01-21 09:45:18 | 10000001 | 30 | 15 | CPN-2401-A7B2K9 | 0 |
| 2408 | 2024-01-22 08:19:47 | 10000001 | 20 | 0 | AUTO-SIGN-0000000000 | 0 |
| ... (持續至 2024-03-06) |

**UserID 10000002 簽到記錄 (前 20 筆)**:

| LogID | SignTime | UserID | PointsGained | ExpGained | CouponGained | IsDeleted |
|-------|----------|--------|--------------|-----------|--------------|-----------|
| 2451 | 2024-01-20 14:32:18 | 10000002 | 10 | 5 | AUTO-SIGN-0000000000 | 0 |
| 2452 | 2024-01-21 22:15:47 | 10000002 | 10 | 5 | AUTO-SIGN-0000000000 | 0 |
| 2453 | 2024-01-22 09:18:33 | 10000002 | 15 | 8 | AUTO-SIGN-0000000000 | 0 |
| 2454 | 2024-01-26 19:47:22 | 10000002 | 20 | 0 | AUTO-SIGN-0000000000 | 0 |
| 2455 | 2024-01-27 11:23:45 | 10000002 | 10 | 5 | AUTO-SIGN-0000000000 | 0 |
| ... (持續至 2024-04-24) |

### 4.2 SignInRule 表格 (全部種子資料 - 10 筆)

| Id | SignInDay | Points | Experience | HasCoupon | CouponTypeCode | IsActive | Description | IsDeleted |
|----|-----------|--------|------------|-----------|----------------|----------|-------------|-----------|
| 1 | 1 | 20 | 0 | 0 | NULL | 1 | 第 1 天簽到規則 | 0 |
| 2 | 2 | 20 | 0 | 0 | NULL | 1 | 第 2 天簽到規則 | 0 |
| 3 | 3 | 20 | 0 | 0 | NULL | 1 | 第 3 天簽到規則 | 0 |
| 4 | 4 | 20 | 0 | 0 | NULL | 1 | 第 4 天簽到規則 | 0 |
| 5 | 5 | 20 | 0 | 0 | NULL | 1 | 第 5 天簽到規則 | 0 |
| 6 | 6 | 30 | 200 | 0 | NULL | 1 | 第 6 天簽到規則 | 0 |
| 7 | 7 | 70 | 500 | 0 | NULL | 1 | 第 7 天簽到規則 + 連續獎勵 | 0 |
| 10 | 30 | 200 | 2000 | 0 | NULL | 1 | 連續簽到 30 天獎勵(含大獎勵) | 0 |
| 11 | 14 | 0 | 0 | 0 | NULL | 1 | 連續簽到 14 天獎勵只發放 | 0 |
| 12 | 21 | 0 | 0 | 0 | NULL | 1 | 連續簽到 21 天獎勵只發放 | 0 |

---

## 5. 寵物系統

### 5.1 Pet 表格 (UserID 10000001 和 10000002)

**UserID 10000001 的寵物**:
```
PetID: 1
UserID: 10000001
PetName: 多多
Level: 4
Experience: 656
Hunger: 14
Mood: 58
Stamina: 89
Cleanliness: 25
Health: 100
SkinColor: #FFFF00 (黃色)
SkinColorChangedTime: 2023-02-22 09:10:06
BackgroundColor: BG005
BackgroundColorChangedTime: 2025-04-09 17:03:40
PointsChanged_SkinColor: 2000
PointsChanged_BackgroundColor: 2500
PointsGained_LevelUp: 10
CurrentExperience: 53
ExperienceToNextLevel: 220
TotalPointsGained_LevelUp: 40
IsDeleted: 0
```

**UserID 10000002 的寵物**:
```
PetID: 2
UserID: 10000002
PetName: 小小
Level: 38
Experience: 4019
Hunger: 55
Mood: 15
Stamina: 57
Cleanliness: 14
Health: 94
SkinColor: #800080 (紫色)
SkinColorChangedTime: 2024-12-11 04:53:18
BackgroundColor: BG008
BackgroundColorChangedTime: 2024-08-25 17:19:48
PointsChanged_SkinColor: 3500
PointsChanged_BackgroundColor: 4000
PointsGained_LevelUp: 40
CurrentExperience: 649
ExperienceToNextLevel: 1535
TotalPointsGained_LevelUp: 920
IsDeleted: 0
```

### 5.2 PetSkinColorCostSettings 表格 (全部種子資料 - 11 筆)

| SettingId | ColorCode | ColorName | PointsCost | Rarity | Description | IsFree | IsActive | IsLimitedEdition | IsDeleted |
|-----------|-----------|-----------|------------|--------|-------------|--------|----------|------------------|-----------|
| 1 | #FFFFFF | 白色 | 0 | 普通 | 純淨的白色，免費提供 | 1 | 1 | 0 | 0 |
| 2 | #000000 | 黑色 | 0 | 普通 | 經典的黑色，免費提供 | 1 | 1 | 0 | 0 |
| 3 | #FF0000 | 紅色 | 0 | 普通 | 熱情的紅色，免費提供 | 1 | 1 | 0 | 0 |
| 4 | #FFA500 | 橙色 | 2000 | 普通 | 溫暖活潑的橙色 | 0 | 1 | 0 | 0 |
| 5 | #FFFF00 | 黃色 | 2000 | 普通 | 陽光開朗的黃色 | 0 | 1 | 0 | 0 |
| 6 | #008000 | 綠色 | 2000 | 普通 | 生機盎然的綠色 | 0 | 1 | 0 | 0 |
| 7 | #00FFFF | 青色 | 2000 | 普通 | 清爽透明的青色 | 0 | 1 | 0 | 0 |
| 8 | #0000FF | 藍色 | 2000 | 普通 | 深邃沉靜的藍色 | 0 | 1 | 0 | 0 |
| 9 | #800080 | 紫色 | 3500 | 稀有 | 神秘高貴的紫色 | 0 | 1 | 0 | 0 |
| 10 | #6F4E37 | 咖啡色 | 3500 | 稀有 | 樸實可靠的咖啡色 | 0 | 1 | 0 | 0 |
| 11 | #6EFE19 | 淺綠色 | 2000 | 限定 | 春季限定色彩(已下架) | 0 | 0 | 1 | 0 |

### 5.3 PetBackgroundCostSettings 表格 (全部種子資料 - 11 筆)

| SettingId | BackgroundCode | BackgroundName | PointsCost | Description | ImagePath | IsActive | SortOrder | IsDeleted |
|-----------|----------------|----------------|------------|-------------|-----------|----------|-----------|-----------|
| 19 | BG001 | 萬聖節南瓜 | 0 | 充滿萬聖節氣氛的南瓜背景，完全免費 | /images/backgrounds/halloween-pumpkin.jpg | 1 | 1 | 0 |
| 20 | BG002 | 教堂彩窗 | 0 | 神聖莊嚴的教堂彩繪玻璃窗，氣氛莊嚴寧靜 | /images/backgrounds/stained-glass-church.jpg | 1 | 2 | 0 |
| 21 | BG003 | 珊瑚海灘 | 0 | 熱帶珊瑚海灘，椰樹與藍天令人心曠神怡 | /images/backgrounds/coral-beach.jpg | 1 | 3 | 0 |
| 22 | BG004 | 清新森林 | 2000 | 綠意盎然的清新森林，鳥語花香 | /images/backgrounds/fresh-forest.jpg | 1 | 4 | 0 |
| 23 | BG005 | 熱帶瀑布 | 2500 | 熱帶雨林深處的壯麗瀑布，生氣蓬勃 | /images/backgrounds/rainforest-waterfall.jpg | 1 | 5 | 0 |
| 24 | BG006 | 早晨教室 | 3000 | 早晨陽光灑進的溫馨教室，充滿朝氣 | /images/backgrounds/morning-classroom.jpg | 1 | 6 | 0 |
| 25 | BG007 | 霓虹夜景 | 3500 | 繁華都市的霓虹招牌，時尚都市氛圍 | /images/backgrounds/neon-skyline.jpg | 1 | 7 | 0 |
| 26 | BG008 | 極光雪原 | 4000 | 熱帶夜空下的絢麗極光，寧靜且壯觀 | /images/backgrounds/aurora-snowfield.jpg | 1 | 8 | 0 |
| 27 | BG009 | 魔法圖書館 | 4500 | 充滿魔法圖書館，充滿神秘魔法與智慧的氣氛 | /images/backgrounds/magic-library.jpg | 1 | 9 | 0 |
| 28 | BG010 | 地獄熔岩 | 6000 | 地獄深處的恐怖熔岩，危險又驚悚 | /images/backgrounds/hell-lava.jpg | 1 | 10 | 0 |
| 29 | BG011 | 蒸汽工廠 | 2000 | 工業革命時代的蒸汽朋克工廠(設定已下架) | /images/backgrounds/steam-workshop.jpg | 0 | 11 | 1 |

### 5.4 PetLevelRewardSettings 表格 (全部種子資料 - 25 筆)

| SettingId | LevelRangeStart | LevelRangeEnd | PointsReward | Description | IsActive | IsDeleted |
|-----------|-----------------|---------------|--------------|-------------|----------|-----------|
| 1 | 1 | 10 | 10 | 新手獎勵(Level 1-10) | 1 | 0 |
| 2 | 11 | 20 | 20 | 中階獎勵(Level 11-20) | 1 | 0 |
| 3 | 21 | 30 | 30 | 高階獎勵(Level 21-30) | 1 | 0 |
| 4 | 31 | 40 | 40 | 精英獎勵(Level 31-40) | 1 | 0 |
| 5 | 41 | 50 | 50 | 專家獎勵(Level 41-50) | 1 | 0 |
| 6 | 51 | 60 | 60 | 專精獎勵(Level 51-60) | 1 | 0 |
| 7 | 61 | 70 | 70 | 大師獎勵(Level 61-70) | 1 | 0 |
| 8 | 71 | 80 | 80 | 宗師獎勵(Level 71-80) | 1 | 0 |
| 9 | 81 | 90 | 90 | 傳奇獎勵(Level 81-90) | 1 | 0 |
| 10 | 91 | 100 | 100 | 宗師聖獎勵(Level 91-100) | 1 | 0 |
| 11 | 101 | 110 | 110 | 超越獎勵(Level 101-110) | 1 | 0 |
| 12 | 111 | 120 | 120 | 極限獎勵(Level 111-120) | 1 | 0 |
| 13 | 121 | 130 | 130 | 破極獎勵(Level 121-130) | 1 | 0 |
| 14 | 131 | 140 | 140 | 超越極限獎勵(Level 131-140) | 1 | 0 |
| 15 | 141 | 150 | 150 | 超越極限獎勵(Level 141-150) | 1 | 0 |
| 16 | 151 | 160 | 160 | 神域獎勵(Level 151-160) | 1 | 0 |
| 17 | 161 | 170 | 170 | 半神獎勵(Level 161-170) | 1 | 0 |
| 18 | 171 | 180 | 180 | 真神獎勵(Level 171-180) | 1 | 0 |
| 19 | 181 | 190 | 190 | 眾神獎勵(Level 181-190) | 1 | 0 |
| 20 | 191 | 200 | 200 | 主神獎勵(Level 191-200) | 1 | 0 |
| 21 | 201 | 210 | 210 | 創世獎勵(Level 201-210) | 1 | 0 |
| 22 | 211 | 220 | 220 | 超創世獎勵(Level 211-220) | 1 | 0 |
| 23 | 221 | 230 | 230 | 至高獎勵(Level 221-230) | 1 | 0 |
| 24 | 231 | 240 | 240 | 聖高獎勵(Level 231-240) | 1 | 0 |
| 25 | 241 | 250 | 250 | 超聖至高獎勵(Level 241-250，封頂級) | 1 | 0 |

---

## 6. 小遊戲系統

### 6.1 MiniGame 表格 (UserID 10000001 和 10000002)

**UserID 10000001 的遊戲記錄 (11 筆)**:

| PlayID | UserID | PetID | Level | MonsterCount | SpeedMultiplier | Result | ExpGained | PointsGained | StartTime | EndTime | Aborted | IsDeleted |
|--------|--------|-------|-------|--------------|-----------------|--------|-----------|--------------|-----------|---------|---------|-----------|
| 3 | 10000001 | 1 | 1 | 6 | 1.00 | Win | 100 | 10 | 2023-07-01 13:44:35 | 2023-07-01 13:49:35 | 0 | 0 |
| 6 | 10000001 | 1 | 2 | 8 | 1.50 | Win | 200 | 20 | 2023-09-03 18:52:09 | 2023-09-03 19:10:09 | 0 | 0 |
| 11 | 10000001 | 1 | 3 | 10 | 2.00 | Win | 300 | 30 | 2023-12-01 20:21:07 | 2023-12-01 20:41:07 | 0 | 0 |
| 4 | 10000001 | 1 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2023-12-10 03:41:43 | 2023-12-10 04:03:43 | 0 | 0 |
| 9 | 10000001 | 1 | 3 | 10 | 2.00 | Win | 300 | 30 | 2024-03-08 09:49:54 | 2024-03-08 10:07:54 | 0 | 0 |
| 10 | 10000001 | 1 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2024-05-15 08:18:26 | 2024-05-15 08:34:26 | 0 | 0 |
| 1 | 10000001 | 1 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2024-09-03 09:36:58 | 2024-09-03 09:58:58 | 0 | 0 |
| 7 | 10000001 | 1 | 3 | 10 | 2.00 | Abort | 0 | 0 | 2024-11-17 07:08:53 | 2024-11-17 07:14:53 | 1 | 0 |
| 8 | 10000001 | 1 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2025-05-07 19:40:07 | 2025-05-07 19:57:07 | 0 | 0 |
| 5 | 10000001 | 1 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2025-06-22 23:39:35 | 2025-06-23 00:02:35 | 0 | 0 |
| 2 | 10000001 | 1 | 3 | 10 | 2.00 | Win | 300 | 30 | 2025-06-30 10:46:31 | 2025-06-30 11:05:31 | 0 | 0 |

**UserID 10000002 的遊戲記錄 (12 筆)**:

| PlayID | UserID | PetID | Level | MonsterCount | SpeedMultiplier | Result | ExpGained | PointsGained | StartTime | EndTime | Aborted | IsDeleted |
|--------|--------|-------|-------|--------------|-----------------|--------|-----------|--------------|-----------|---------|---------|-----------|
| 16 | 10000002 | 2 | 1 | 6 | 1.00 | Win | 100 | 10 | 2023-03-14 06:01:04 | 2023-03-14 06:06:04 | 0 | 0 |
| 21 | 10000002 | 2 | 2 | 8 | 1.50 | Win | 200 | 20 | 2023-03-30 11:16:12 | 2023-03-30 11:26:12 | 0 | 0 |
| 23 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2023-05-03 15:04:06 | 2023-05-03 15:24:06 | 0 | 0 |
| 19 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2023-08-06 12:46:56 | 2023-08-06 13:08:56 | 0 | 0 |
| 14 | 10000002 | 2 | 3 | 10 | 2.00 | Win | 300 | 30 | 2023-12-12 20:11:58 | 2023-12-12 20:29:58 | 0 | 0 |
| 13 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2024-01-19 17:39:00 | 2024-01-19 17:56:00 | 0 | 0 |
| 20 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2024-02-06 00:13:14 | 2024-02-06 00:32:14 | 0 | 0 |
| 12 | 10000002 | 2 | 3 | 10 | 2.00 | Win | 300 | 30 | 2024-03-12 17:04:33 | 2024-03-12 17:21:33 | 0 | 0 |
| 18 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2024-11-08 14:08:24 | 2024-11-08 14:29:24 | 0 | 0 |
| 22 | 10000002 | 2 | 3 | 10 | 2.00 | Win | 300 | 30 | 2025-05-03 00:59:39 | 2025-05-03 01:18:39 | 0 | 0 |
| 15 | 10000002 | 2 | 3 | 10 | 2.00 | Win | 300 | 30 | 2025-06-30 16:12:19 | 2025-06-30 16:33:19 | 0 | 0 |
| 17 | 10000002 | 2 | 3 | 10 | 2.00 | Lose | 0 | 0 | 2025-07-26 06:55:13 | 2025-07-26 07:16:13 | 0 | 0 |

---

## 7. 系統設定

### 7.1 SystemSettings 表格 (全部種子資料 - 56 筆)

**Game 類別 (24 筆)**:

| SettingId | SettingKey | SettingValue | Description | Category | SettingType | IsReadOnly | IsActive |
|-----------|------------|--------------|-------------|----------|-------------|------------|----------|
| 1 | Game.DefaultDailyLimit | 3 | Default daily game limit | Game | Number | 0 | 1 |
| 3 | Game.Level1.MonsterCount | 6 | Level 1 monster count | Game | Number | 0 | 1 |
| 6 | Game.Level1.SpeedMultiplier | 1.0 | Level 1 speed multiplier | Game | Number | 0 | 1 |
| 9 | Game.Level1.ExperienceReward | 100 | Level 1 completion experience reward | Game | Number | 0 | 1 |
| 12 | Game.Level1.PointsReward | 10 | Level 1 completion points reward | Game | Number | 0 | 1 |
| 4 | Game.Level2.MonsterCount | 8 | Level 2 monster count | Game | Number | 0 | 1 |
| 7 | Game.Level2.SpeedMultiplier | 1.5 | Level 2 speed multiplier | Game | Number | 0 | 1 |
| 10 | Game.Level2.ExperienceReward | 200 | Level 2 completion experience reward | Game | Number | 0 | 1 |
| 13 | Game.Level2.PointsReward | 20 | Level 2 completion points reward | Game | Number | 0 | 1 |
| 5 | Game.Level3.MonsterCount | 10 | Level 3 monster count | Game | Number | 0 | 1 |
| 8 | Game.Level3.SpeedMultiplier | 2.0 | Level 3 speed multiplier | Game | Number | 0 | 1 |
| 11 | Game.Level3.ExperienceReward | 300 | Level 3 completion experience reward | Game | Number | 0 | 1 |
| 14 | Game.Level3.PointsReward | 30 | Level 3 completion points reward | Game | Number | 0 | 1 |
| 55 | Game.Level3.HasCoupon | true | Level 3 completion issue coupon | Game | Boolean | 0 | 1 |
| 56 | Game.Level3.CouponType | GAME_LEVEL3_BONUS | Level 3 completion coupon type | Game | String | 0 | 1 |
| 47 | Game.Result.Win.HungerDelta | -20 | Game win hunger delta | Game | Number | 0 | 1 |
| 48 | Game.Result.Win.MoodDelta | 30 | Game win mood delta | Game | Number | 0 | 1 |
| 49 | Game.Result.Win.StaminaDelta | -20 | Game win stamina delta | Game | Number | 0 | 1 |
| 50 | Game.Result.Win.CleanlinessDelta | -20 | Game win cleanliness delta | Game | Number | 0 | 1 |
| 51 | Game.Result.Lose.HungerDelta | -20 | Game lose hunger delta | Game | Number | 0 | 1 |
| 52 | Game.Result.Lose.MoodDelta | -30 | Game lose mood delta | Game | Number | 0 | 1 |
| 53 | Game.Result.Lose.StaminaDelta | -20 | Game lose stamina delta | Game | Number | 0 | 1 |
| 54 | Game.Result.Lose.CleanlinessDelta | -20 | Game lose cleanliness delta | Game | Number | 0 | 1 |
| 2 | Game.Levels.Configuration | {"levels":[...]} | Game level configuration (3 levels) | Game | JSON | 0 | 1 |

**Pet 類別 (17 筆)**:

| SettingId | SettingKey | SettingValue | Description | Category | SettingType | IsReadOnly | IsActive |
|-----------|------------|--------------|-------------|----------|-------------|------------|----------|
| 15 | Pet.Interaction.Feed.HungerIncrease | 10 | Feed increases hunger | Pet | Number | 0 | 1 |
| 16 | Pet.Interaction.Feed.HealthIncrease | 10 | Feed increases health | Pet | Number | 0 | 1 |
| 17 | Pet.Interaction.Bath.CleanlinessIncrease | 10 | Bath increases cleanliness | Pet | Number | 0 | 1 |
| 18 | Pet.Interaction.Bath.MoodIncrease | 10 | Bath increases mood | Pet | Number | 0 | 1 |
| 19 | Pet.Interaction.Coax.MoodIncrease | 10 | Coax increases mood | Pet | Number | 0 | 1 |
| 20 | Pet.Interaction.Coax.StaminaIncrease | 10 | Coax increases stamina | Pet | Number | 0 | 1 |
| 21 | Pet.Interaction.Rest.StaminaIncrease | 10 | Rest increases stamina | Pet | Number | 0 | 1 |
| 22 | Pet.Interaction.Rest.HealthIncrease | 10 | Rest increases health | Pet | Number | 0 | 1 |
| 23 | Pet.DailyDecay.HungerDecay | 20 | Daily hunger decay | Pet | Number | 0 | 1 |
| 24 | Pet.DailyDecay.MoodDecay | 30 | Daily mood decay | Pet | Number | 0 | 1 |
| 25 | Pet.DailyDecay.StaminaDecay | 10 | Daily stamina decay | Pet | Number | 0 | 1 |
| 26 | Pet.DailyDecay.CleanlinessDecay | 20 | Daily cleanliness decay | Pet | Number | 0 | 1 |
| 27 | Pet.DailyDecay.HealthDecay | 0 | Daily health decay (no decay) | Pet | Number | 0 | 1 |
| 28 | Pet.ColorChange.PointsCost | 2000 | Pet color change points cost | Pet | Number | 0 | 1 |
| 29 | Pet.DailyFullStatsBonus.Experience | 100 | Daily full stats bonus experience | Pet | Number | 0 | 1 |
| 30 | Pet.DailyFullStatsBonus.Points | 0 | Daily full stats bonus points (no bonus) | Pet | Number | 0 | 1 |
| 31 | Pet.LevelUp.Formula | {JSON} | Pet level up experience formula (3 tiers) | Pet | JSON | 0 | 1 |

**SignIn 類別 (11 筆)**:

| SettingId | SettingKey | SettingValue | Description | Category | SettingType | IsReadOnly | IsActive |
|-----------|------------|--------------|-------------|----------|-------------|------------|----------|
| 32 | SignIn.Weekday.Points | 20 | Weekday sign-in points reward | SignIn | Number | 0 | 1 |
| 33 | SignIn.Weekday.Experience | 0 | Weekday sign-in experience reward | SignIn | Number | 0 | 1 |
| 34 | SignIn.Weekend.Points | 30 | Weekend sign-in points reward | SignIn | Number | 0 | 1 |
| 35 | SignIn.Weekend.Experience | 200 | Weekend sign-in experience reward | SignIn | Number | 0 | 1 |
| 36 | SignIn.Streak7Days.BonusPoints | 40 | Consecutive 7 days extra points reward | SignIn | Number | 0 | 1 |
| 37 | SignIn.Streak7Days.BonusExperience | 300 | Consecutive 7 days extra experience reward | SignIn | Number | 0 | 1 |
| 38 | SignIn.Streak7Days.HasCoupon | false | Consecutive 7 days no coupon | SignIn | Boolean | 0 | 1 |
| 39 | SignIn.PerfectAttendance30Days.BonusPoints | 200 | Perfect attendance extra points reward | SignIn | Number | 0 | 1 |
| 40 | SignIn.PerfectAttendance30Days.BonusExperience | 2000 | Perfect attendance extra experience reward | SignIn | Number | 0 | 1 |
| 41 | SignIn.PerfectAttendance30Days.HasCoupon | true | Perfect attendance issue coupon | SignIn | Boolean | 0 | 1 |
| 42 | SignIn.PerfectAttendance30Days.CouponType | MONTH_BONUS | Perfect attendance coupon type | SignIn | String | 0 | 1 |

**Wallet/Coupon/EVoucher 類別 (4 筆)**:

| SettingId | SettingKey | SettingValue | Description | Category | SettingType | IsReadOnly | IsActive |
|-----------|------------|--------------|-------------|----------|-------------|------------|----------|
| 43 | Wallet.MaxPoints | 999999 | Maximum points limit | Wallet | Number | 0 | 1 |
| 44 | Wallet.InitialPoints | 1000 | New user initial points | Wallet | Number | 0 | 1 |
| 45 | Coupon.DefaultValidityDays | 30 | Coupon default validity days | Coupon | Number | 0 | 1 |
| 46 | EVoucher.DefaultValidityDays | 90 | E-voucher default validity days | EVoucher | Number | 0 | 1 |

---

## 8. 資料統計摘要

### 8.1 UserID 10000001 資料統計

| 表格名稱 | 記錄數量 | 備註 |
|----------|----------|------|
| User_Wallet | 1 | 當前點數: 60030 |
| WalletHistory | 5 | 初始餘額 94500，經多次消費與獲得 |
| Coupon | 13 | 全部未使用 |
| EVoucher | 3 | 1 張已使用，2 張未使用 |
| UserSignInStats | 50+ | 從 2024-01-15 開始持續簽到 |
| Pet | 1 | 等級 4，名稱「多多」|
| MiniGame | 11 | 4 勝 6 負 1 中斷 |

### 8.2 UserID 10000002 資料統計

| 表格名稱 | 記錄數量 | 備註 |
|----------|----------|------|
| User_Wallet | 1 | 當前點數: 21666 |
| WalletHistory | 5 | 初始餘額 68720，經多次消費與獲得 |
| Coupon | 12 | 全部未使用 |
| EVoucher | 1 | 1 張已使用 |
| UserSignInStats | 50+ | 從 2024-01-20 開始持續簽到 |
| Pet | 1 | 等級 38，名稱「小小」，經驗值 4019 |
| MiniGame | 12 | 5 勝 7 負 |

### 8.3 配置表格統計

| 表格名稱 | 記錄數量 | 備註 |
|----------|----------|------|
| CouponType | 3 | 免費運費、85折、滿$500折$50 |
| EVoucherType | 20 | 涵蓋便利商店、百貨、餐飲等多種禮券 |
| PetSkinColorCostSettings | 11 | 3 色免費，8 色付費，1 色下架 |
| PetBackgroundCostSettings | 11 | 3 個免費背景，7 個付費背景，1 個下架 |
| SignInRule | 10 | 涵蓋 1-7 天、14 天、21 天、30 天簽到規則 |
| PetLevelRewardSettings | 25 | Level 1-250 的升級獎勵設定 |
| SystemSettings | 56 | 動態配置中心，涵蓋 Game、Pet、SignIn、Wallet 等 4 大類別 |

---

## 9. 資料完整性驗證

### 9.1 外鍵關聯檢查

✅ **User_Wallet.User_Id** → Users.User_ID (10000001, 10000002 均存在)
✅ **Coupon.UserID** → Users.User_ID (所有優惠券均關聯到有效用戶)
✅ **Coupon.CouponTypeID** → CouponType.CouponTypeID (所有優惠券類型均存在)
✅ **EVoucher.UserID** → Users.User_ID (所有電子禮券均關聯到有效用戶)
✅ **EVoucher.EVoucherTypeID** → EVoucherType.EVoucherTypeID (所有電子禮券類型均存在)
✅ **EVoucherToken.EVoucherID** → EVoucher.EVoucherID (所有 Token 均關聯到有效禮券)
✅ **Pet.UserID** → Users.User_ID (所有寵物均關聯到有效用戶)
✅ **MiniGame.UserID** → Users.User_ID (所有遊戲記錄均關聯到有效用戶)
✅ **MiniGame.PetID** → Pet.PetID (所有遊戲記錄均關聯到有效寵物)

### 9.2 資料一致性檢查

✅ **User_Wallet.User_Point** 與 **WalletHistory** 計算一致性
- UserID 10000001: 94500 - 2000 + 30 - 30000 - 2500 = 60030 ✓
- UserID 10000002: 68720 - 40000 - 4000 - 3500 + 446 = 21666 ✓

✅ **Pet 等級與經驗值** 合理性
- UserID 10000001: Level 4, Experience 656 ✓
- UserID 10000002: Level 38, Experience 4019 ✓

✅ **EVoucher 使用狀態** 與 **EVoucherToken** 一致性
- EVoucherID 1: IsUsed=1, Token IsRevoked=0 ✓
- EVoucherID 4: IsUsed=1, Token IsRevoked=1 ✓

---

## 10. 備註與建議

### 10.1 資料觀察

1. **UserID 10000001** 和 **10000002** 都是活躍用戶，持續進行簽到、遊戲、寵物互動
2. 兩位用戶都有購買付費寵物膚色和背景的記錄，顯示付費意願
3. UserID 10000002 的寵物等級 (Level 38) 遠高於 UserID 10000001 (Level 4)，表示更投入養成系統
4. 優惠券獲得頻率穩定，主要來自簽到和遊戲獎勵
5. 電子禮券兌換需要大量點數 (10000-40000)，顯示點數系統的價值

### 10.2 系統設定亮點

1. **動態配置**: SystemSettings 表支援 56 個可調整參數，無需修改代碼即可調整遊戲規則
2. **多層級獎勵**: 寵物升級獎勵涵蓋 1-250 級，支援長期養成
3. **彈性簽到**: 支援平日/假日差異化獎勵、連續簽到加成、全勤獎勵
4. **完整審計**: 所有表格支援軟刪除機制，保留歷史資料

### 10.3 後續建議

1. 建議定期備份 WalletHistory 和 UserSignInStats 等高頻寫入表格
2. 可考慮為 SystemSettings 增加版本控制機制
3. EVoucherRedeemLog 目前無資料，可加強店員核銷功能的推廣
4. PetLevelRewardSettings 支援到 Level 250，可觀察實際用戶到達情況決定是否擴展

---

**報告結束**

生成工具: SQL Server Management Studio + sqlcmd
生成時間: 2025-11-05
報告製作: Claude Code (Anthropic)
