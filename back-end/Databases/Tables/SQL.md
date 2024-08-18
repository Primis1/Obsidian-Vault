***
[[Database relations]]
Special values:
1. SQL - standard language for storing  
2. RDBMS - stands for `Relation DataBase Management System`,  are those kind which use columns and rows system. They are powered by SQL 

To know:
1. RDMBS is used in MySQL and Postgres

SQL Syntax:
1. All action in SQL begins with the action keyword: ==SELECT, INSERT, UPDATE, DELETE== and, usually, command to specify an action 
	- they are not case sensitive, ==it just a convention==
	- in case of literals ==SQL IS CASE SENSITIVE==  ==`"john" != "JOHN"`== 
1.  End of the action is represented with ==semicolon==(`;`)
2. Comments a `--` 
```sql 
SELECT 
	first_name, LAST_USER
FROM employee;
```

SQL key syntax:
1. ==DISTINCT==(different) - used with SELECT, to *select* only ==different== values from the ==column== 
2. To group operators we can use ( )
```sql
-- we create a column where we will the a single row with all counts of different countries 
SELECT Count(*) as AnyName FROM (SELECT DISTINCT Country FROM Customers);
```
