-- 코드를 입력하세요
SELECT 
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
-- 장, 단기 케이스를 나누기 위해 CASE - WHEN - THEN 문 사용.
-- 날짜를 계산할 때에는 DATEDIFF를 사용.
-- `+1`을 하는 이유는 대여한 날도 1일로 치기 때문에 하루를 더해야한다.
    CASE 
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '장기 대여'
        ELSE '단기 대여' 
    END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
-- 2022년 9월에 속하는 대여 기록만 필터링
WHERE DATE_FORMAT(START_DATE, '%Y-%m') = '2022-09'
-- 대여기록 ID를 기준으로 내림차순 정렬
ORDER BY HISTORY_ID DESC