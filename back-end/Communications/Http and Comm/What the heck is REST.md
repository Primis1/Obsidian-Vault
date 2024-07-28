***
[[Http & Https]]
Special values:
1. REST - REpresentational State Transfer, architectural style that allow the client to communicate with a server with recommended rules 
	1. Client sends a req by REST to the Server, and after that server give a res back to client through the REST 
2. Architecture - set of constraints and principles for communicating between client and server 
3. Protocol - specific set of rules for communicating between the client and the server 


To know:
1. REST APIs are ==stateless==, they don't memorize the requests, we have to write each request independently, but also API server should not store the data
2. Caching, rest can ==cache== some data after request was received
3. Layering, we can ==divide our API== into layers, each layer could its own responsibility  

Details:
1. A structure of ==client== req:
	- an HTTP verb, defines what kind of operation to perform/What type of CRUP method
	- a _header_, which allows the client to pass along information about the request
	- a path to a resource
	- an optional message body containing data

2. The HTTP verbs( they are similar to CRUD, but they aren't the same)
	1. GET - request data
	2. POST - creates data 
	3. PUT - changes all existing data
	4. DELETE - deletes data
	5. PATCH - changes only small amount of data

3. The response from the server contains codes:
	Good one:
	1. 200(ok) - general res for successful req
	2. 201(created) - general res for successfully created req
	
	Bad one:
	1. 400(bad request) - The request cannot be processed because of bad request syntax, excessive size, or another client error
	2. 403(forbidden) - client doesn't have access to the data 
	3. 404(not found) - The resource could not be found at this time. It is possible it was deleted, or does not exist yet|
	
	4. Codes for CRUD  
		- GET — return 200 (OK)
		- POST — return 201 (CREATED)
		- PUT — return 200 (OK)
		- DELETE — return 204 (NO CONTENT) If the operation fails, return the most specific status code possible corresponding to the problem that was encountered.