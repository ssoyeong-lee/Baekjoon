SELECT YEAR(ED.DIFFERENTIATION_DATE) AS YEAR,
    YM.MAX_SIZE - ED.SIZE_OF_COLONY AS YEAR_DEV,
    ID
FROM ECOLI_DATA AS ED
    JOIN (
    SELECT YEAR(DIFFERENTIATION_DATE) AS Y, MAX(SIZE_OF_COLONY) AS MAX_SIZE
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)
    ) AS YM
    ON YEAR(ED.DIFFERENTIATION_DATE) = YM.Y
ORDER BY YEAR, YEAR_DEV
