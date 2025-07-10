-- 코드를 입력하세요
SELECT 
    PT_NAME,
    PT_NO,
    GEND_CD,
    AGE,
    -- 전화번호 처리
    COALESCE(TLNO, 'NONE') AS TLNO
FROM PATIENT
-- 12세 이하.
WHERE AGE <= 12 AND
    -- 여성.
    GEND_CD = 'W'
-- 나이를 기준으로 내림차순 정렬, 환자이름 기준 오름차순 정렬
ORDER BY AGE DESC, PT_NAME ASC