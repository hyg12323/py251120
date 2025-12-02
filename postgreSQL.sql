CREATE DATABASE study_db;

CREATE DATABASE  tb_test(
test1 VARCHAR
)

SELECT * FROM tb_test

DROP TABLE tb_test

--테이블 만들기
CREATE TABLE tb_test(
	name VARCHAR,
	AGE INT,
	birth timestamp
)
/*
조회 (read r)
select 컬럼명
from 테이블명
*/
SELECT NAME, AGE, birth FROM tb_test;
SELECT * FROM tb_test;
COMMIT

/*
추가
insert  (insert c)
*/
INSERT INTO tb_test(NAME,AGE,birth)
VALUES
('이름1',20,'2025-12-01'),
('이름2',21,'2025-12-02')

SELECT * FROM tb_test
WHERE NAME = '이름2'

SELECT * FROM tb_test
WHERE AGE = 20

/*
수정 (update u)
update 테이블명
set 컬럼명 = 값,컬럼명 = 값
where 조건 꼭 쓰기
*/

UPDATE tb_test
SET AGE = 30
WHERE NAME='이름2'

/*
삭제(delete d)
delete from 테이블명
where 조건 꼭 쓰기
*/
DELETE from tb_test
WHERE AGE = 30

SELECT * FROM tb_test


SELECT NOW()


-- 기본 테이블 DEPT
CREATE TABLE dept
(
    deptno INTEGER PRIMARY KEY,
    dname  VARCHAR(14),
    loc    VARCHAR(13)
);

-- EMP 테이블
CREATE TABLE emp
(
    empno    INTEGER PRIMARY KEY,
    ename    VARCHAR(10),
    job      VARCHAR(9),
    mgr      INTEGER,
    hiredate DATE,
    sal      NUMERIC(7,2),
    comm     NUMERIC(7,2),
    deptno   INTEGER REFERENCES dept(deptno)
);

-- DEPT 데이터
INSERT INTO dept VALUES (10,'ACCOUNTING','NEW YORK');
INSERT INTO dept VALUES (20,'RESEARCH','DALLAS');
INSERT INTO dept VALUES (30,'SALES','CHICAGO');
INSERT INTO dept VALUES (40,'OPERATIONS','BOSTON');

-- EMP 데이터
INSERT INTO emp VALUES
(7369,'SMITH','CLERK',7902,DATE '1980-12-17',800,NULL,20);

INSERT INTO emp VALUES
(7499,'ALLEN','SALESMAN',7698,DATE '1981-02-20',1600,300,30);

INSERT INTO emp VALUES
(7521,'WARD','SALESMAN',7698,DATE '1981-02-22',1250,500,30);

INSERT INTO emp VALUES
(7566,'JONES','MANAGER',7839,DATE '1981-04-02',2975,NULL,20);

INSERT INTO emp VALUES
(7654,'MARTIN','SALESMAN',7698,DATE '1981-09-28',1250,1400,30);

INSERT INTO emp VALUES
(7698,'BLAKE','MANAGER',7839,DATE '1981-05-01',2850,NULL,30);

INSERT INTO emp VALUES
(7782,'CLARK','MANAGER',7839,DATE '1981-06-09',2450,NULL,10);

INSERT INTO emp VALUES
(7788,'SCOTT','ANALYST',7566,DATE '1987-07-13',3000,NULL,20);

INSERT INTO emp VALUES
(7839,'KING','PRESIDENT',NULL,DATE '1981-11-17',5000,NULL,10);

INSERT INTO emp VALUES
(7844,'TURNER','SALESMAN',7698,DATE '1981-09-08',1500,0,30);

INSERT INTO emp VALUES
(7876,'ADAMS','CLERK',7788,DATE '1987-07-13',1100,NULL,20);

INSERT INTO emp VALUES
(7900,'JAMES','CLERK',7698,DATE '1981-12-03',950,NULL,30);

INSERT INTO emp VALUES
(7902,'FORD','ANALYST',7566,DATE '1981-12-03',3000,NULL,20);

INSERT INTO emp VALUES
(7934,'MILLER','CLERK',7782,DATE '1982-01-23',1300,NULL,10);

-- BONUS
CREATE TABLE bonus
(
    ename VARCHAR(10),
    job   VARCHAR(9),
    sal   NUMERIC,
    comm  NUMERIC
);

-- SALGRADE
CREATE TABLE salgrade
(
    grade INTEGER,
    losal INTEGER,
    hisal INTEGER
);

INSERT INTO salgrade VALUES (1,700,1200);
INSERT INTO salgrade VALUES (2,1201,1400);
INSERT INTO salgrade VALUES (3,1401,2000);
INSERT INTO salgrade VALUES (4,2001,3000);
INSERT INTO salgrade VALUES (5,3001,9999);

COMMIT;


SELECT * FROM emp
LIMIT 4;
SELECT * FROM dept;

SELECT * FROM emp
OFFSET 5
LIMIT 4;
SELECT * FROM dept;



-- 문제: emp에서 deptno가 10인 사람만 선택
SELECT * FROM emp
WHERE deptno = 10


SELECT * FROM emp


--문제1 
-- 월급이 2000 이상인 사람 
SELECT * FROM emp 
WHERE sal >= 2000


--문제2
-- 월급이 2000초과 3000이하인사람

SELECT * FROM emp
WHERE sal >2000 and sal <= 3000

--문제 3
-- 사원번호로 smith만 조회

SELECT * FROM emp
WHERE empno = 7369

SELECT ename,sal FROM emp
WHERE ename = 'SMITH'



-- null 은 계산하지 않는다
SELECT * FROM emp
WHERE comm < 400


-- is null은 null까지 계산해준다
SELECT * FROM emp
WHERE comm IS NULL
OR comm <= 400 

SELECT * FROM emp
WHERE 
    job = 'CLERK' OR job = 'SALESMAN'

-- IN도 사용가능
SELECT * FROM emp
WHERE job IN ('CLERK','SALESMAN')



SELECT * FROM emp
WHERE job NOT IN ('CLERK','SALESMAN')


-- A를 포함한 전부 LIKE
SELECT * FROM emp
WHERE ename LIKE '%A%'


-- 소문자로 바꿔주는거 결과를
SELECT ename FROM emp
SELECT LOWER(ename) FROM emp

-- 대문자로 바꿔주는 결과물
SELECT ename FROM emp
SELECT UPPER('Allen')


SELECT * FROM emp
WHERE LOWER(ename) LIKE LOWER('%aM%')

--맨위에 하나만 나오게
SELECT * FROM emp
ORDER BY sal LIMIT 1

-- 반대로 정렬
SELECT * FROM emp
ORDER BY sal DESC


-- 오름차순 생략가능 ASC
-- 여러개 적는 경우
-- 앞에서 부터 정렬후 중복되는 값이 있으면 다음 기준으로 적용
SELECT * FROM emp
ORDER BY sal DESC, empno ASC, empno

SELECT job,deptno FROM emp 
GROUP BY job, deptno

SELECT job, deptno,COUNT(*) FROM emp
GROUP BY job,deptno

SELECT job, COUNT(*), MAX(sal) FROM emp
GROUP BY job

--4번
SELECT job,COUNT(*) AS cnt
--1번
FROM emp
--2번
WHERE sal > 1000
--3번
GROUP BY job
--5번
ORDER BY cnt


SELECT comm FROM emp e

SELECT 'N/A' FROM emp
WHERE comm IS NULL


SELECT 
	sal,
	case
	 	WHEN sal>3000 THEN '고액'
	 	WHEN sal <= 3000 and sal > 1000 THEN '적당'
	 	ELSE '소액'
	end
from emp;

SELECT * FROM emp
WHERE deptno = 10
UNION ALL
SELECT * FROM emp
WHERE sal >= 2000


SELECT * FROM emp
SELECT * FROM dept


SELECT empno,ename,job FROM emp e, dept d
WHERE e.deptno = d.deptno


