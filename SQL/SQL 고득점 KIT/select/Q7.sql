SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;

--MAX(속성이름) 를 사용해서도 풀이 가능
SELECT MAX(DATETIME) FROM ANIMAL_INS;