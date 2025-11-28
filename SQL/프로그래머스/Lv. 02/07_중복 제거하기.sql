-- 코드를 입력하세요
SELECT 
  -- 고유이름 수를 count
  COUNT(DISTINCT(NAME)) AS count
FROM ANIMAL_INS
-- 이름이 NULL인 경우는 제외
WHERE NAME IS NOT NULL