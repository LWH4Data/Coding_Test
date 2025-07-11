-- 코드를 입력하세요
SELECT 
    BOOK_ID, 
    DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") AS PUBLISHED_DATE
FROM BOOK
-- 2021년 출판된 데이터 필터링
WHERE YEAR(PUBLISHED_DATE) = '2021' AND
    -- 카테고리가 '인문'인 데이터 필터링
    CATEGORY = '인문'
-- 출판일 기준 오름차순 정렬
ORDER BY PUBLISHED_DATE ASC