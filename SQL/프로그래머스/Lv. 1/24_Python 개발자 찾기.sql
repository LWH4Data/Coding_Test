-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
-- 파이썬이 있나 확인
-- OR을 통한 연결보다 각 속성에 'Python' 포함여부를 'IN'으로 확인.
WHERE 'Python' IN (SKILL_1, SKILL_2, SKILL_3)
-- ID 기준 오름차순 정렬
ORDER BY ID ASC