-- 코드를 입력하세요
SELECT 
    ANIMAL_ID,
    NAME,
    -- CASE WHEN을 통한 조건 처리
    CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR
    SEX_UPON_INTAKE LIKE '%Spayed%' 
    THEN 'O'
    ELSE 'X' 
    END AS 중성화
FROM ANIMAL_INS
-- 정렬
ORDER BY ANIMAL_ID ASC