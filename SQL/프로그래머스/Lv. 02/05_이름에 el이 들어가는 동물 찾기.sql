-- 코드를 입력하세요
SELECT 
  ANIMAL_ID,
  NAME
FROM ANIMAL_INS
WHERE 
  -- 개인 데이터만 필터링
  ANIMAL_TYPE = "Dog"
  -- NAME에 el이 포함된 데이터만 필터링
  AND NAME LIKE "%el%"
 
-- 이름 순으로 조회
ORDER BY NAME;