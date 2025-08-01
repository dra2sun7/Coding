-- 코드를 입력하세요
SELECT SQ.FLAVOR FROM (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS SUM_ORDER FROM JULY
    GROUP BY FLAVOR
) AS SQ
INNER JOIN FIRST_HALF FH ON SQ.FLAVOR = FH.FLAVOR
ORDER BY (SQ.SUM_ORDER + FH.TOTAL_ORDER) DESC
LIMIT 3;