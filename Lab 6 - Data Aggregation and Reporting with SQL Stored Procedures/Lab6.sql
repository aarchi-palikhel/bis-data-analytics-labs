/*SELECT 
	Province,
	SUM (CAST(Total AS INT)) AS TotalBranches
FROM MonthlyStatistics
GROUP BY Province;

SELECT 
	Province,
	AVG(TRY_CAST(NULLIF(Pop_Per_Branch, '-') AS FLOAT)) AS AvgPopPerBranch
FROM Monthlystatistics
GROUP BY Province;

SELECT Province, District, Class_A, Class_B, Class_C, Total
FROM Monthlystatistics
WHERE (Class_A + ISNULL(Class_B,0) + ISNULL(Class_C, 0)) <> Total;

SELECT
	Province,
	SUM(CAST(Total AS INT)) AS Total_Branches
FROM Monthlystatistics
GROUP BY Province
HAVING SUM(CAST(Total AS INT)) > 100;

SELECT Province AS Name, 'Province' AS Type
FROM Monthlystatistics
GROUP BY Province
UNION
SELECT District, 'District' AS Type
FROM Monthlystatistics;

SELECT District, Province, Class_A, Class_B
FROM Monthlystatistics
WHERE Class_A > 10
UNION
SELECT District, Province, Class_A, Class_B
FROM Monthlystatistics
WHERE Class_B > 15;

SELECT m.*
FROM Monthlystatistics m
JOIN (
	SELECT Province, MAX(Population) AS MaxPopulation
	FROM Monthlystatistics
	GROUP BY Province
) p ON m.Province = p.Province AND m.Population = p.MaxPopulation;

SELECT TOP 3 Province, District, Total
FROM Monthlystatistics
ORDER BY CAST(Total AS INT) DESC;

SELECT
	Province,
	COUNT (District) AS District_Count, AVG(CAST(Population AS BIGINT)) AS Avg_Population
FROM Monthlystatistics
GROUP BY Province;*/

SELECT
	Province,
	AVG(CAST(Total AS INT)) AS Avg_Branches
FROM Monthlystatistics
GROUP BY Province
HAVING AVG(CAST(Total AS INT)) > 20;