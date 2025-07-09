-- 코드를 입력하세요
# 가장 최근 = 현재 날짜 = 가장 큰 값.
# 날짜만 출력하는 문제이기에 MAX()를 사용. O(N)
# ORDER BY는 정렬이 포함되어 조금 더 느리기 때문 O(NlogN)
SELECT MAX(DATETIME)
FROM ANIMAL_INS

# 만약 DATETIME이 가장 최근 날짜의 다른 컬럼값을 필요로 한다면
# MAX()의 경우 서브쿼리를 사용해야 한다.