-- 코드를 입력하세요
SELECT F.FLAVOR
-- INNER JOIN을 통해 두 테이블을 결합
FROM FIRST_HALF AS F
INNER JOIN ICECREAM_INFO AS I ON F.FLAVOR = I.FLAVOR
-- 총주문량이 3,000 보다 큰 데이터 필터링
WHERE F.TOTAL_ORDER > 3000 AND
    -- 주 성분이 과일인 데이터 필터링
    I.INGREDIENT_TYPE = 'fruit_based'
-- 총주문량이 큰 순서대로 정렬
ORDER BY F.TOTAL_ORDER DESC
    