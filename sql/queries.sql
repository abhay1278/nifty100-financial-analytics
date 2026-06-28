-- Query 1
SELECT COUNT(*) AS total_companies
FROM companies;

-- Query 2
SELECT COUNT(*) AS total_profit_records
FROM profitandloss;

-- Query 3
SELECT company_id,
       COUNT(*) AS years_available
FROM profitandloss
GROUP BY company_id
ORDER BY years_available DESC;

-- Query 4
SELECT company_id,
       MAX(net_profit) AS highest_profit
FROM profitandloss
GROUP BY company_id
ORDER BY highest_profit DESC
LIMIT 10;

-- Query 5
SELECT company_id,
       AVG(roe_percentage) AS avg_roe
FROM companies
GROUP BY company_id
ORDER BY avg_roe DESC;

-- Query 6
SELECT broad_sector,
       COUNT(*) AS companies
FROM sectors
GROUP BY broad_sector
ORDER BY companies DESC;

-- Query 7
SELECT company_id,
       MAX(close_price) AS highest_price
FROM stock_prices
GROUP BY company_id
ORDER BY highest_price DESC
LIMIT 10;

-- Query 8
SELECT company_id,
       AVG(pe_ratio) AS avg_pe
FROM market_cap
GROUP BY company_id
ORDER BY avg_pe DESC;

-- Query 9
SELECT company_id,
       AVG(return_on_equity_pct) AS avg_roe
FROM financial_ratios
GROUP BY company_id
ORDER BY avg_roe DESC;

-- Query 10
SELECT COUNT(*)
FROM peer_groups;