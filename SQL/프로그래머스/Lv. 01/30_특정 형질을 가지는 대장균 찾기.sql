-- 코드를 작성해주세요
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
-- 각 형질에 맞는 비트연산자를 비교
-- 1번 형질: 0001, 2번 형질: 0010, 3번 형질: 0100, 4번 형질: 1000
-- 2번 형질이 아닌 경우는 2와의 비트연산
-- 1, 3번 아닌 경우는 0101을 의미한다.
WHERE
  (GENOTYPE & 2 = 0) AND
  (GENOTYPE & 5 != 0)