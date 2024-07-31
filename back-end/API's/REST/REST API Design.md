***
[[API's]]
Special values:
1. REST - REpresentational State Transfer, architectural style that allow the client to communicate with a server with recommended rules 
	1. Client sends a ==HTTP== ==req== to the RESTful API, that API process the data in the way we need, to access the ==data== ==layer== in the way we want 

- Architecture - set of constraints and principles for communicating between client and server 
- Protocol - specific set of rules for communicating between the client and the server 

To know:
1. RESTful API's should be:
	1. ==Client-Server== - communication model, our API is a server of the application, we making request ==TO THE API==   
	
	2. ==Layered System== - ==hierarchical== ==design==, used to create a nested layers, each with its own functionality   
	
	3. ==Stateless== - server should ==NOT== have any information about previous request. It mean that each request should contain full information about its desire 
	
	4. ==Uniform== ==Interface== - single design patterns for all parts of an API 
	
	5. ==Cacheable== - ==RESPONSE== from the server should explicitly indicate weather they are ==cacheable== or ==not== 

2. Common practices:
	1. Plural end of the URL - `api/user=s=` `api/project=s=` 
	2. With changes to routes we should ==NOT== modify the existing API, but just create a new version - `api/v1/something` `api/v2/something`