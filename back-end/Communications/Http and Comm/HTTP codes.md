***
[[Http & Https]]
Special values:
1. Http response - has a code that describes the response(was it good or bad), could have different headers 

To know:
1. The HTTP verbs( they are similar to CRUD, but they aren't the same)
	1. GET - request data. 200 (OK)
	2. POST - creates data. 201 (CREATED)
	3. PUT - changes all existing data. 200 (OK)
	4. DELETE - deletes data. 204 (NO CONTENT)
	5. PATCH - changes only small amount of data. (OK)

3. The HTTP response from the server contains codes:
	
	==Good== ==one==:
	1. 200(ok) - general res for successful req
	2. 201(created) - general res for successfully created req
	
	==Bad== ==one==:
	1. 400(bad request) - The request cannot be processed because of bad request syntax, excessive size, or another client error
	2. 403(forbidden) - client doesn't have access to the data 
	3. 404(not found) - The resource could not be found at this time. It is possible it was deleted, or does not exist yet|
