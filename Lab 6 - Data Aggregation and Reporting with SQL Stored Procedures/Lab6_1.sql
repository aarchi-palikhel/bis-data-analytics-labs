CREATE PROCEDURE sp_GenerateMonthlyReports
AS
BEGIN
		--Provinces with More than 100 Branches
		INSERT INTO Prov_Branches_Summary
		SELECT Province, SUM(CAST(Total AS INT)) AS Total_Branches
		FROM Monthlystatistics
		GROUP BY Province
		HAVING SUM(CAST (Total AS INT)) > 100;
		--List Provinces and Districts with Type Labels
		INSERT INTO Prov_Dist_Type
		SELECT DISTINCT Province AS Name, Province AS Type 
		FROM Monthlystatistics
		UNION
		SELECT District AS Name, 'District' AS Type
		FROM Monthlystatistics;
		--Districts where Class A 10 OR Class_B > 15
		INSERT INTO High_Class_Branches
		SELECT District, Province, Class_A, Class_B
		FROM Monthlystatistics
		WHERE CAST (Class_A AS INT) > 10
		UNION
		SELECT District, Province, Class_A, Class_B
		FROM Monthlystatistics
		WHERE CAST(Class_B AS INT) > 15;
		--District with Highest Population in Each Province
		INSERT INTO MaxPop_District
		SELECT m.*
		FROM Monthlystatistics m
		JOIN (
			SELECT Province, MAX(CAST(Population AS BIGINT)) AS MaxPop
			FROM Monthlystatistics m
			GROUP BY Province
		)p ON m. Province = p. Province
		AND CAST(m.Population AS BIGINT) = p.MaxPop;
		--Top 3 Districts by Branches
		INSERT INTO Top3_Branches
		SELECT TOP 3 District, Province, CAST(Total AS INT) AS Total
		FROM Monthlystatistics
		ORDER BY CAST (Total AS INT) DESC;
		--Number of Districts & Average Population
		INSERT INTO Prov_Dist_Avg
		SELECT Province, COUNT (District) AS District_Count, 
			AVG(CAST (Population AS BIGINT)) AS Avg_Population
		FROM Monthlystatistics
		GROUP BY Province;
		--Provinces with Avg Branches 20
		INSERT INTO High_Avg_Branches
		SELECT Province, AVG(CAST(Total AS INT)) AS Avg_Branches
		FROM Monthlystatistics
		GROUP BY Province
		HAVING AVG(CAST(Total AS INT)) > 20
END;