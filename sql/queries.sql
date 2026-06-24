-- Total Funds
SELECT COUNT(*) FROM fund_master;

-- Average NAV
SELECT AVG(nav) FROM nav_history;

-- Top 5 Funds by AUM
SELECT scheme_name,aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- SIP Transactions Count
SELECT COUNT(*)
FROM investor_transactions
WHERE transaction_type='SIP';

-- State Wise Investors
SELECT state,COUNT(*)
FROM investor_transactions
GROUP BY state;

-- KYC Status
SELECT kyc_status,COUNT(*)
FROM investor_transactions
GROUP BY kyc_status;

-- Highest Return Funds
SELECT scheme_name,return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- Average Expense Ratio
SELECT AVG(expense_ratio_pct)
FROM scheme_performance;

-- Fund House Count
SELECT fund_house,COUNT(*)
FROM fund_master
GROUP BY fund_house;

-- Gender Distribution
SELECT gender,COUNT(*)
FROM investor_transactions
GROUP BY gender;