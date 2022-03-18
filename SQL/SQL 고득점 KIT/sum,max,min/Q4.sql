/* distinct를 칼럼명 앞에 넣으면, 중복된 값 제거 해주는 역할과 동일 */

SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
WHERE NAME IS NOT NULL;