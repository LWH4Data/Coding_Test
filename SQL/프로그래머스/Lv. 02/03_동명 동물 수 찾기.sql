-- 코드를 입력하세요
SELECT 
  NAME,
  COUNT(*) AS COUNT
FROM ANIMAL_INS
-- 이름이 없는 경우 제외
WHERE NAME IS NOT NULL
-- NAME을 기준으로 그룹화
GROUP BY NAME
-- 집계를 통해 이름이 두 번 이상인 경우를 필터링
HAVING COUNT(*) >= 2
-- 이름순 조회
ORDER BY NAME;
