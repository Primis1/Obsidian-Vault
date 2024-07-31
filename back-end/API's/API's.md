***
[[Backend]]
Special values:

To know:
1. API can be written in almost any way we want, ==gRPC, REST, SOAP, GraphQL are just the ways, or more like architecture== with its ways to do things. Each has its advantages and disadvantages
2. API can be called an API if it servers its function - ==be a middle layer between application and data layer== 
3. Architectures and protocols exist just to make the process ==faster== or ==easier== 

4. API "required" components:
	1. ==Router== - something that handles incoming HTTP requests 
	
	2. ==Handler== - ==function== that process the received requests and returns response. Each handler corresponds to specific endpoint and HTTP method
	
	3. ==Model== - data structure that represents the entities in the entire API. Database tables
	
	4. ==Database Layer== - manages interactions with database columns and rows. ORM's can be used here 
	
	5. Middleware - function that intercepts HTTP requests/response to perform its validation. Can be used for auth, logging and rate limiting 
	
	6. Configuration - setting with behavior of an API, env, etc
	
	7. Response handling - ==functions== or ==utilities== to standardizes the format of API responses, handle errors and serialize data to JSON  
	
	8. Testing - for nerds 