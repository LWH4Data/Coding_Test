-- 코드를 입력하세요
# 냉동시설 여부가 NULL인 경우 'N'으로 출력 설정.
SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    COALESCE(FREEZER_YN, "N") AS FREEZER_YN
FROM FOOD_WAREHOUSE
# 경기도에 위치한 데이터만 필터링
WHERE ADDRESS LIKE "%경기도%"
# 창고 ID를 기준으로 오름차순 정렬
ORDER BY WAREHOUSE_ID ASC

# CASE WHEN이 아닌 COALESCE 사용.
# 단순 NULL을 처리하는 경우에는 COALESCE가 더 간단하다.
# 단, NULL이 아닌 특정 값을 처리하는 경우 CASE WHEN을 사용한다.