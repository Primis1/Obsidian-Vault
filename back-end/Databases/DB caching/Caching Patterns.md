***
[[Databases in general]]
Special values:
1. DB cache - is buffering technique, database stores frequently queried data in temporal memory
	- #cache is high-speed ==data==, ==separate==, ==storage== layer that stores data which is often ==read requested==    
To know:
1. Cache can be stored in database, application or stand alone access layer

2. Different caching strategies 
	1. Cache-aside 
		1. strategy involve the application being ==responsible== for ==reading== and ==writing== ==data== into the ==cache==. When some data is required, *it* first query the data. if data is present in cache==, it will be retrieved. If ==NOT==, data will be fetched from the ==main== ==memory==, and ==stored== in ==cache==, before being sent to the client  
	![[Pasted image 20240821023858.png]]
	
	2. Read-through 
		1. The cache will sit between application and database. The application ==will== ==look== for the ==data== in cache ==initially== If data is not present, application will query the data from main memory. The data will be hydrated, and by that send to the receiver 
	![[Pasted image 20240821023922.png]]
	3. Write-back 
		1. involves the application to write data in the cache, and the cache updating data in async way. When write operation occurs, data will be written to the cache. Cache will be updated in database, in later-time-selected, based on cache capability
	![[Pasted image 20240821023941.png]]
	
	4. Write-through
		1. involves the application to write data into the cache and and cache into DB simultaneously 
	![[Pasted image 20240821023931.png]]
	5. Write-around 
		1. involves the data to be written into the database. In this case, cache will be updated ONLY when data is read from it
	![[Pasted image 20240821023951.png]]]]