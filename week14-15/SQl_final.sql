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

-- Find the tracks that are included in more than 3 playlists but have never been sold (i.e., they do not exist in the InvoiceLine table).

-- Use Joins to connect tracks, playlists, and genres.

-- Use a Subquery to exclude tracks that have sales.

-- Use a Window Function (RANK()) to rank these "hidden hits" by their duration (Milliseconds) within each genre.

SELECT t.Name as TrackName, t.Milliseconds
RANK() OVER (PARTITION BY g.Name ORDER BY t.Milliseconds DESC) AS GenreRank 
FROM Tracks t
JOIN playlists p on p.TrackId = t.TrackId
join genres g on g.genreId = t.genreId
WHERE t.TrackId not in (
    SELECT TrackId FROM Playlists
)
GROUP BY t.TrackId, t.Name, t.Milliseconds
HAVING count(t.TrackId)>3;

-- We want to understand customer behavior by comparing their current purchase to their own previous spending patterns.

-- Create a CTE that displays the customer's name, country, and invoice total for each invoice.

-- Use a Window Function (AVG() OVER) to calculate each customer's "Moving Average" for their previous 2 and current invoices.

-- Use a Subquery or CTE filtering to show only those invoices where the total is 50% higher than the customer's current moving average.

WITH CustomerProfile AS (
    SELECT c.FirstName as name, c.Country as Country, i.Total as InvoiceTotal, i.InvoiceDate,
    AVG(i.Total) OVER (PARTITION BY c.CustomerId ORDER BY i.InvoiceDate) AS MovingAverage
    FROM Customer c
    JOIN Invoice i ON i.CustomerId = c.CustomerId
)

SELECT 
    Name, Country, InvoiceTotal, MovingAverage
FROM CustomerProfile
WHERE InvoiceTotal > 1.5 * MovingAverage;