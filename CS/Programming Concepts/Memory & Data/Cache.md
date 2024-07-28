***
Special values:

1. #cache - it is server data which is stored on a client side, in the local memory.

To know:

1. In #cache server stores a usually repetitive value/data, that should be in fast access to the client, and perhaps doesn't change often(remember all the shit with favicon)\

	1. Cache allows to has an immediate access to the data, because it doesn't need to request, validate, sent back data from the server, because it’s already there
	
	2. Just to keep in mind - if a client tries to request the cached data from the server, it will give a ```305``` status code. It practically means: “You already have a data in your cache, so i won't send it again”
