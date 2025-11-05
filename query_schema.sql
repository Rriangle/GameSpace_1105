-- Complete Schema Information Query for GameSpacedatabase
-- This script queries all schema details for the specified 20 tables

-- Declare table list
DECLARE @tables TABLE (TableName NVARCHAR(128))
INSERT INTO @tables VALUES
    ('User_Wallet'),
    ('WalletHistory'),
    ('Coupon'),
    ('CouponType'),
    ('EVoucher'),
    ('EVoucherType'),
    ('EVoucherToken'),
    ('EVoucherRedeemLog'),
    ('UserSignInStats'),
    ('SignInRule'),
    ('Pet'),
    ('PetSkinColorCostSettings'),
    ('PetBackgroundCostSettings'),
    ('PetLevelRewardSettings'),
    ('MiniGame'),
    ('SystemSettings'),
    ('Users'),
    ('ManagerData'),
    ('ManagerRole'),
    ('ManagerRolePermission')

DECLARE @TableName NVARCHAR(128)
DECLARE table_cursor CURSOR FOR SELECT TableName FROM @tables
OPEN table_cursor
FETCH NEXT FROM table_cursor INTO @TableName

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT '=========================================='
    PRINT 'TABLE: ' + @TableName
    PRINT '=========================================='
    PRINT ''

    -- 1. Column Information with Identity
    PRINT '--- COLUMNS ---'
    SELECT
        c.COLUMN_NAME,
        c.DATA_TYPE,
        c.CHARACTER_MAXIMUM_LENGTH,
        c.NUMERIC_PRECISION,
        c.NUMERIC_SCALE,
        c.IS_NULLABLE,
        c.COLUMN_DEFAULT,
        c.ORDINAL_POSITION,
        CASE
            WHEN COLUMNPROPERTY(OBJECT_ID(c.TABLE_SCHEMA + '.' + c.TABLE_NAME), c.COLUMN_NAME, 'IsIdentity') = 1
            THEN 'YES'
            ELSE 'NO'
        END AS IS_IDENTITY,
        ISNULL(CAST(IDENT_SEED(c.TABLE_SCHEMA + '.' + c.TABLE_NAME) AS VARCHAR), '') AS IDENTITY_SEED,
        ISNULL(CAST(IDENT_INCR(c.TABLE_SCHEMA + '.' + c.TABLE_NAME) AS VARCHAR), '') AS IDENTITY_INCREMENT
    FROM INFORMATION_SCHEMA.COLUMNS c
    WHERE c.TABLE_NAME = @TableName
    ORDER BY c.ORDINAL_POSITION

    PRINT ''

    -- 2. Table Constraints
    PRINT '--- CONSTRAINTS ---'
    SELECT
        CONSTRAINT_NAME,
        CONSTRAINT_TYPE
    FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
    WHERE TABLE_NAME = @TableName
    ORDER BY CONSTRAINT_TYPE, CONSTRAINT_NAME

    PRINT ''

    -- 3. Primary Keys and Key Columns
    PRINT '--- PRIMARY KEYS ---'
    SELECT
        kcu.CONSTRAINT_NAME,
        kcu.COLUMN_NAME,
        kcu.ORDINAL_POSITION
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
        ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
        AND kcu.TABLE_NAME = tc.TABLE_NAME
    WHERE kcu.TABLE_NAME = @TableName
        AND tc.CONSTRAINT_TYPE = 'PRIMARY KEY'
    ORDER BY kcu.ORDINAL_POSITION

    PRINT ''

    -- 4. Unique Constraints
    PRINT '--- UNIQUE CONSTRAINTS ---'
    SELECT
        kcu.CONSTRAINT_NAME,
        kcu.COLUMN_NAME,
        kcu.ORDINAL_POSITION
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
        ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
        AND kcu.TABLE_NAME = tc.TABLE_NAME
    WHERE kcu.TABLE_NAME = @TableName
        AND tc.CONSTRAINT_TYPE = 'UNIQUE'
    ORDER BY kcu.CONSTRAINT_NAME, kcu.ORDINAL_POSITION

    PRINT ''

    -- 5. Foreign Keys with Referenced Tables
    PRINT '--- FOREIGN KEYS ---'
    SELECT
        fk.CONSTRAINT_NAME AS FK_NAME,
        kcu.COLUMN_NAME AS FK_COLUMN,
        rc.UNIQUE_CONSTRAINT_NAME AS REFERENCED_CONSTRAINT,
        kcu2.TABLE_NAME AS REFERENCED_TABLE,
        kcu2.COLUMN_NAME AS REFERENCED_COLUMN,
        rc.UPDATE_RULE,
        rc.DELETE_RULE
    FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS rc
    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS fk
        ON rc.CONSTRAINT_NAME = fk.CONSTRAINT_NAME
    INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
        ON fk.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME
    LEFT JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu2
        ON rc.UNIQUE_CONSTRAINT_NAME = kcu2.CONSTRAINT_NAME
        AND kcu.ORDINAL_POSITION = kcu2.ORDINAL_POSITION
    WHERE fk.TABLE_NAME = @TableName
    ORDER BY fk.CONSTRAINT_NAME

    PRINT ''

    -- 6. Check Constraints
    PRINT '--- CHECK CONSTRAINTS ---'
    SELECT
        cc.CONSTRAINT_NAME,
        cc.CHECK_CLAUSE
    FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS cc
    WHERE cc.CONSTRAINT_NAME IN (
        SELECT CONSTRAINT_NAME
        FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
        WHERE TABLE_NAME = @TableName
        AND CONSTRAINT_TYPE = 'CHECK'
    )
    ORDER BY cc.CONSTRAINT_NAME

    PRINT ''

    -- 7. Default Constraints (more detailed)
    PRINT '--- DEFAULT CONSTRAINTS ---'
    SELECT
        dc.name AS CONSTRAINT_NAME,
        c.name AS COLUMN_NAME,
        dc.definition AS DEFAULT_VALUE
    FROM sys.default_constraints dc
    INNER JOIN sys.columns c ON dc.parent_object_id = c.object_id AND dc.parent_column_id = c.column_id
    INNER JOIN sys.tables t ON dc.parent_object_id = t.object_id
    WHERE t.name = @TableName
    ORDER BY c.column_id

    PRINT ''
    PRINT ''

    FETCH NEXT FROM table_cursor INTO @TableName
END

CLOSE table_cursor
DEALLOCATE table_cursor
