***
Special values:
1. #axios - is a fetch replacement library that provides minimalistic syntax, similar to HTTP reqs and build-in features like caching and error handling
![[Pasted image 20240602133234.png]]

To know:
1. Keys features of axios is minimalistic syntax in compare to regular fetch and interceptors
	1. Interceptors are functions that called before each request or response was handled by my code. Jesus, interceptors are INDEPENDENT functions, for which we create a pattern for response and request, and after that, before ==ACTUAL== HTTP request this middleware will be executed.
2. It automatically converts a response into the JSON.
 
Advancing:
1. More about #interceptors:
	1. To wrap a req/res into the interceptor we use an interceptor object/keyword for axios logic
	2. axios.interseptors.request/response are connected to such methods like:
		1. create( ) - creates a new axios instance
		2. use( ) - use some logic that should be contained in the interceptor 
		3. eject( ) - removes the interceptor from the axios instance
	3. We can create as many interceptors as we want, but each of those inters should be connected to separate instance 
```ts
const instanceOne = axios.create({
    baseURL: `https://pokeapi.co/api/v2/`,
})

instanceOne.interceptors.request.use(() => {
    console.log("this interceptos is now default for those requests");
})

instanceOne.get("pokemon/ditto").then(responce => console.log(responce))
```
![[Pasted image 20240602225050.png]]