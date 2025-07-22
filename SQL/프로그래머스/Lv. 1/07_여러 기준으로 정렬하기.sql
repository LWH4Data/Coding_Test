-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
-- 이름순으로 조회
-- 나중에 보호를 시작하는 순
--   - 나중 = 더 최근 보호 시작 = DESC 정렬.
ORDER BY NAME ASC, DATETIME DESC