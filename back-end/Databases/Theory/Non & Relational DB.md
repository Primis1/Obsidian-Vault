***
[[Databases in general]]
Special values:
1. #relationalDB - consist from tables, and tables consist from rows(records) and columns(fields)
2. #non-relationaDB - or No-SQL. Such DB's does ==NOT== require any ==tables==, ==fields== nor ==records==. NoSQL deals with ==semi==-==structured== or ==unstructured== data. ==It consist from files within different folders==, instead of tables 

To know:
1. #relationalDB 
	Advantages:
	1. ==ACID compliance==(відповіність) . ACID principles stands for  
		- Atomicity - integrity of DB transactions. Transactions does not support partiality. ==So transaction happens on 100% or does NOT happen at all==
		
		- Consistency(консистентність/послідовність) - ensures(запевняє) that DB is ==consisted== ==before== and ==after== ==transaction== is ==made==. If transaction occurs and the result in DB ==does not match the settled rules, transaction will be *rolled back*== to the previous "state"
		
		- Isolation - refers to the ==concurrent== ==execution==(обробка) of ==transaction==, process in one, will not affect the other 
		
		- Durability - the updates of transactions is stored in the non-volatile(енергонезалежний)
	
	2. ==Normalization==
		- Dividing larger tables into smaller one
	
	3. ==Accuracy==
		- Existing of primary/foreign keys. Helps to avoid duplication of data among tables 
	
	4. High security
		- We can separate data among tables and it's "state"(public or confident)
	
	Disadvantages
	1. ==Loss of data== during transportation 
		- Some why, when we do transfer huge DB's from one platform to other, we can leak some data and loose it 
	2. ==Slow performance== 
		- Through layers of relations, it can get hard to get the value we need
	3. ==*High cost?*==

2. #non-relationaDB 
	Advantages:
	1. ==Unstructured data==
		- Can store structured as well as unstructured data
	2. ==High Scalability== 
		- Can be scaled to accommodate any type of data with low cost of money 
	3. ==Higher access speed==  
	
	Disadvantages
	1. ==Not really *ACID*== 
		- NoSQL's does not guarantee the *ACID* practices 
	
	2. ==No backups== 
	
	3. No standardization 
		- 