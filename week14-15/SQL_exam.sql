-- Requirement: Join Customer and Invoice. Calculate the total spend for each customer.
--  Then, use a Window Function to rank customers by their total spend within their own country.

-- Output: Country, FirstName, LastName, TotalSpent, and their Rank.
SELECT Country, FirstName, LastName, TotalSpent,
       RANK() OVER (PARTITION BY Country ORDER BY TotalSpent DESC) AS Rank
FROM (
    SELECT c.Country, c.FirstName, c.LastName, SUM(i.Total) AS TotalSpent
    FROM Customer c
    JOIN Invoice i ON c.Id = i.CustomerId
    GROUP BY c.CustomerId, c.Country, c.FirstName, c.LastName
) t;

-- Scenario: Logistics noticed that some invoices have an unusually high number of items.

-- Requirement: Find all InvoiceIds that contain more items (counts of InvoiceLineId) than the average number of items per invoice across the whole database.
-- Constraints: You must use a Subquery to calculate the average item count and Joins to connect the invoice data.
SELECT i.InvoiceId, Count(il.InvoiceLineId) as ItemNumber
FROM invoice i
JOIN InvoiceLine il on il.InvoiceId = i.Id
GROUP BY i.InvoiceId
HAVING count(il.InvoiceLineId) >(
    SELECT AVG(ItemNumber)
    FROM (
        SELECT COUNT(*)
        FROM InvoiceLine
        GROUP BY InvoiceId
    )
)

-- Task 3: The Monthly Momentum Analysis (Extra Hard)
-- Scenario: We need to track if our music genres are growing or shrinking month-to-month.
-- • Requirement:
-- Create a CTE that calculates the total revenue for each Genre per month (formatted as 'YYYY-MM').
-- Use a Window Function (LAG) to compare the current month's revenue to the previous month's revenue for that specific genre.
-- Calculate the Difference in revenue between the two months.
-- • Output: GenreName, Month, CurrentMonthRevenue, PreviousMonthRevenue, Difference.
WITH MonthlyRevenue AS (
    SELECT g.Name as GenreName,
    strftime('%Y-%m', i.InvoiceDate) AS Month
    SUM(il.Quantity *il.UnitPrice) AS CurrentMonthRevenue
    FROM Genre g
    JOIN Track t ON g.GenreId = t.GenreId
    JOIN InvoiceLine il ON t.TrackId = il.TrackId
    JOIN Invoice i ON il.InvoiceId = i.InvoiceId
    GROUP BY g.Name, strftime('%Y-%m', i.InvoiceDate)
)

SELECT GenreName, Month, CurrentMonthRevenue, 
LAG(CurrentMonthRevenue) OVER (PARTITION BY GenreName ORDER BY Month) AS PreviousMonthRevenue,
CurrentMonthRevenue - LAG(CurrentMonthRevenue) OVER (PARTITION BY GenreName ORDER BY Month) AS Difference
FROM MonthlyRevenue;
ORDER BY Month, GenreName