-- 코드를 입력하세요
SELECT * 
FROM CAR_RENTAL_COMPANY_CAR
-- OPTIONS에 네비게이션이 포함된 데이터만 필터링
WHERE OPTIONS LIKE "%네비게이션%"
-- 자동차 ID를 기준으로 내림차순 정렬
ORDER BY CAR_ID DESC