***
[[REST]]
Special values:
1. REST - REpresentational State Transfer, architectural style that allow the client to communicate with a server with recommended rules 
	1. Client sends a ==HTTP== ==req== to the RESTful API, that API process the data in the way we need, to access the ==data== ==layer== in the way we want 
2. Architecture - set of constraints and principles for communicating between client and server 
3. Protocol - specific set of rules for communicating between the client and the server 

To know:
1. REST APIs are ==stateless==, they don't memorize the requests, we have to write each request independently, but also API server should not store the data
2. Caching, rest can ==cache== some data after request was received
3. Layering, we can ==divide our API== into layers, each layer could its own responsibility  
