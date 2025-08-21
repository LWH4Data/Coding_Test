-- 코드를 입력하세요
SELECT 
    DR_NAME, 
    DR_ID, 
    MCDP_CD,
    -- 날짜 형식 맞추기.
    DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
-- 진료과가 흉부외과(CS)이거나 일반외과(GS)인 데이터 필터링
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
-- 고용일자 기준 내림차순, 이름 기준 오름차순
ORDER BY HIRE_YMD DESC, DR_NAME ASC