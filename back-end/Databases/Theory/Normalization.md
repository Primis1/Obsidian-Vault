***
[[Databases in general]]
### Special values:
1. #normalization - process of optimizing existing database, from it's relations to tables

2. *anomaly* - issue with database that, perhaps, should not be there, or happen if DB is not normalized 

3. `normal forms` - we applied set of normalizing rules to the data set, this changed `DB` or `tables` are called `normalized forms`
	1. `first normal form`  : 
		1. Does the combination of columns make a unique row every single time 
		2. What filed can be used to uniquely identify the row 
	2. 

### To know:

#### Kinds of anomalies:
1. Insert anomaly - possibility of adding incomplete rows into the DB
![[Pasted image 20240825050108.png]]
2. Update anomaly - lack of single gateway for updates, like changing the `Biology` to `intro to biology` in every single columns instead of singleton
![[Pasted image 20240825050215.png]]
3. Delete anomaly - during delete operation we deleted *more* data than we wanted
	- *But, if we delete this row, we lose the record of the Biology 2 class, because it’s not stored anywhere else. The same can be said for the Medicine course.*
![[Pasted image 20240825050428.png]]
