const sql = require('mssql');

const config = {
    server: '(local)\\SQLEXPRESS',
    database: 'GameSpacedatabase',
    options: {
        trustServerCertificate: true,
        enableArithAbort: true
    },
    authentication: {
        type: 'default',
        options: {
            userName: '',
            password: ''
        }
    }
};

// Use Windows Authentication
const windowsConfig = {
    server: '(local)\\SQLEXPRESS',
    database: 'GameSpacedatabase',
    options: {
        trustServerCertificate: true,
        enableArithAbort: true,
        encrypt: false
    },
    authentication: {
        type: 'ntlm',
        options: {
            domain: '',
            userName: '',
            password: ''
        }
    }
};

// Simpler config for Windows Auth
const simpleConfig = {
    server: '(local)\\SQLEXPRESS',
    database: 'GameSpacedatabase',
    options: {
        trustServerCertificate: true,
        enableArithAbort: true,
        encrypt: false,
        instanceName: 'SQLEXPRESS'
    }
};

const queries = [
    {
        name: 'User_Wallet',
        query: 'SELECT * FROM User_Wallet WHERE User_Id IN (10000001, 10000002)'
    },
    {
        name: 'WalletHistory',
        query: 'SELECT * FROM WalletHistory WHERE UserID IN (10000001, 10000002)'
    },
    {
        name: 'Coupon',
        query: 'SELECT * FROM Coupon WHERE UserID IN (10000001, 10000002)'
    },
    {
        name: 'EVoucher',
        query: 'SELECT * FROM EVoucher WHERE UserID IN (10000001, 10000002)'
    },
    {
        name: 'EVoucherToken',
        query: 'SELECT * FROM EVoucherToken WHERE EVoucherID IN (SELECT EVoucherID FROM EVoucher WHERE UserID IN (10000001, 10000002))'
    },
    {
        name: 'EVoucherRedeemLog',
        query: 'SELECT * FROM EVoucherRedeemLog WHERE EVoucherID IN (SELECT EVoucherID FROM EVoucher WHERE UserID IN (10000001, 10000002))'
    },
    {
        name: 'UserSignInStats',
        query: 'SELECT * FROM UserSignInStats WHERE UserID IN (10000001, 10000002)'
    },
    {
        name: 'Pet',
        query: 'SELECT * FROM Pet WHERE UserID IN (10000001, 10000002)'
    },
    {
        name: 'MiniGame',
        query: 'SELECT * FROM MiniGame WHERE UserID IN (10000001, 10000002)'
    }
];

async function executeQueries() {
    try {
        console.log('Connecting to SQL Server...');
        console.log(`Server: ${simpleConfig.server}`);
        console.log(`Database: ${simpleConfig.database}`);

        const pool = await sql.connect(simpleConfig);
        console.log('Connected successfully!\n');

        for (const queryInfo of queries) {
            console.log('='.repeat(80));
            console.log(`TABLE: ${queryInfo.name}`);
            console.log('='.repeat(80));
            console.log(`Query: ${queryInfo.query}\n`);

            try {
                const result = await pool.request().query(queryInfo.query);

                if (result.recordset && result.recordset.length > 0) {
                    console.log(`Found ${result.recordset.length} record(s):\n`);

                    // Print column headers
                    const columns = Object.keys(result.recordset[0]);
                    console.log(columns.join(' | '));
                    console.log('-'.repeat(80));

                    // Print each record
                    result.recordset.forEach((record, index) => {
                        console.log(`\nRecord ${index + 1}:`);
                        columns.forEach(col => {
                            let value = record[col];
                            if (value instanceof Date) {
                                value = value.toISOString();
                            } else if (value === null) {
                                value = 'NULL';
                            }
                            console.log(`  ${col}: ${value}`);
                        });
                    });
                } else {
                    console.log('No records found.');
                }

                console.log('\n');
            } catch (queryError) {
                console.error(`Error executing query for ${queryInfo.name}:`, queryError.message);
                console.log('\n');
            }
        }

        await pool.close();
        console.log('Connection closed.');

    } catch (err) {
        console.error('Database connection error:', err);
        console.error('Error details:', {
            message: err.message,
            code: err.code,
            state: err.state
        });
    }
}

executeQueries();
