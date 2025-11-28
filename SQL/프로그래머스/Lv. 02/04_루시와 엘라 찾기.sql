-- 코드를 입력하세요
SELECT 
  ANIMAL_ID,
  NAME,
  SEX_UPON_INTAKE
FROM ANIMAL_INS
-- 이름 목록과 매치되는 데이터만 필터링
WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty");