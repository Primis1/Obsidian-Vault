***
[[Logging]]
### Special values:
1. #dependency-injection - DI pattern separates objects from its dependencies, by removing them from the object itself, and declaring them outside 

### To know:

#### Concepts: 
##### Components: 
1. Client:
	- Component that requires the service provided by other class
	- Object receives all `dependencies`(functionality from other files) from external Source

2. Service: 
	- Object or class that provides *`particular`* functionality that `client` can rely on 
	- Should be independent from the client. Only focuses on its `features`

3. Injector:
	- Creates and delivers instances of service to the client and `injects` them
	- Is aware of `client's` dependencies, add fulfills them during runtime 

4. Interface:
	- Struct of method that `client` refers to, provides independent of components