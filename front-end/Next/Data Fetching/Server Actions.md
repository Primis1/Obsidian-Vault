***

Special values:
1. Server Action - from the name it is an event that happens on a server side, and could be send to the client. They are asynchronous function that are executed on a server. They are used to to handle form submission and mutations of data.  


To know:
1. Server action should be declared in a directive "*use server*"
	1. Files marked "use server" aren't server component, this tag was made especially for SA
	
2. SA - are integrated with next cache environment, so when action was invoked, it can contain an updated UI as well as new data in a single response 
3. Under the hood actions use POST HTTP method, this is only one type of CRUD that can invokes them. 
4. Server action aren't bind to <*form*>, but can be invoked in buttons, handlers and third party libraries.

Best Practice:  
1. There are tons of types for fetching data and solutions:
	1. 