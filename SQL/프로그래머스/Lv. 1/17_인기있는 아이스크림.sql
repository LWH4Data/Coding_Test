-- 코드를 입력하세요
SELECT FLAVOR
FROM FIRST_HALF
-- 총주문량 기준 내림차순, 출하 번호 기준 오름차순 정렬.
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC