***
[[Communication]]
Special values:
1. Rest - architecture with not strict set of rules, for requests to the server. Is *based* on #HTTP protocol
2. gRPC - protocol is a high-performance way for requests to the server, it should be written in its own language, or in of supported; like GO 
3. GraphQL - an API query language for backend and front end
To know:
1. REST - uses individual route for any single request to the API
	1. REST - can use GET, POST, PUT, DELETE http methods, via URL
	2. Mostly uses JSON and XML
![[Pasted image 20240523102645.png]]

2. gRPC - is not working with web out of the box, however there is an extension call *gRPC*-*Web*, that is based on HTTP 1.1 but doesn't have some features 
	1. Made for easier microservice integrations

3. GraphQL - use one route for all requests to the API 
	1. Front-end describes what data they want, when back-end write code to resolve the request
![[Pasted image 20240523102718.png]]



***
Overall:
![[Pasted image 20240523104244.png]]