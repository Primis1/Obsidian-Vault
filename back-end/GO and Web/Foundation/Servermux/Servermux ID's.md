***
[[Servermux & Routes]]
Special values:
1. #strconv - used for converting from/to string between primitives  
2. `snippet/view?id={id}` -  route from which we gonna retrieve the id  
	1. untrusted user input - the value received from the client, that should be somehow verified 

To know:
1. For dynamic routes we do NOT need to specify `?id={id}` for development, it somehow manages it automatically 