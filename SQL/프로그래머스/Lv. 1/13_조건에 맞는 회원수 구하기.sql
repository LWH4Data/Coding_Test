-- 코드를 입력하세요
SELECT COUNT(*) AS USERS
FROM USER_INFO
-- YEAR(날짜) 문법을 통해 2021에 해당하는 데이터만 필터링
WHERE YEAR(joined) = 2021 AND
    -- 범위 조건이기에 BETWEEN을 통해 필터링
    -- BETWEEN의 이상, 이하의 범위를 갖는다.
    AGE BETWEEN 20 AND 29