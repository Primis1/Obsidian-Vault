***
[[Databases in general]]
Special values:
- kinds of relationships:
	1. ==one==-==to==-==one==(1 : 1) - it has one record(запись) on each side of the relationship. By accessing that key we will get single response. Like one country can has only one capital 
	2. ==one==-==to==-==many==(1: N) - it has one record on one side and can have multiple records on other. By accessing the key, we can get multiple response with the same identifier  
	3. ==many==-==to==-==many==(N : N) - it's primary key can be a foreign key for multiple items, and these items can have multiple primary keys 
		- *Best practice(optimal good solution) is to create a `linked table`, the table who will combine two primary keys, of multiple records from one, for multiple records for other*

- types of columns:
	1. Primary key - column whose value uniquely identifies a table record
	2. Foreign key - column whose values reference to the primary key of other table
	- ==We have person with `ID`, but we also have a student who has `StudentID`, this student id gonna be the foreign key of the `Student table `==

To know:

- *Database relations helps in DB normalization*. DB normalization is the fck decomposition which i see over and over and over and over again. We divide one big table into bunch of smaller and hope that the DB is going to work well and fast 
-  

1. OTO:
- one record can have only one foreign key somewhere
![[Pasted image 20240812184304.png]]
2. OTM:
- one record can be used in multiple tables. Customer can have many orders 
![[Pasted image 20240823221644.png]]

3. MTM:
- 