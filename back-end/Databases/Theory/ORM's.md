***
[[Databases in general]]
### Special values: 
1. #ORM - Object-Rational-Mapper. Used for facilitating the process of DB queries, CRUDs, and any interactions with Database. 
- *Syntax sugar over raw SQL queries*

### To know:
1. Available in different PL. #ORM allow to write OOP language code, as SQL queries 

2. #ORM provide not really a regular data-fetching, but straight DB access in chosen environment. ==ORM can *not* be used API requests== 

3. #ORM's provide:
	1. Immediate access to the database 
	2. Security and types 
	3. Facilitation of SQL syntax and reducing the boiler-plate code 

#### ORM vs HTTP in Application:
1. #ORM:
	1. We can build SQL logic ONLY on a server-side
	2. If #ORM is used in `server environment`, we accomplish ==straight== access to the ==database==
		1. In case of usage on a client, we fall into `performance` && `security`. 
	3. ORM's does not used for any calls besides of DB
2. #HTTP: 
	1. HTTP should be used for calling an API's
	2. We create API endpoint, and do HTTP request to it from the `client-component`, this endpoint can use #ORM 