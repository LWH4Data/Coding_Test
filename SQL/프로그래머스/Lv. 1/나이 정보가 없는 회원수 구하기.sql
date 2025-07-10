-- 코드를 입력하세요
SELECT COUNT(*) AS USERS
FROM USER_INFO
-- 나이 정보가 없는 회원만 필터링
WHERE AGE IS NULL