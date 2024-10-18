***
[[Backend]]
### Special values:
1. #docker - technology for containerization of software, to isolate the runtime environment of the application by replicating & isolating its environment 
	1. docker-file - blue print with configuration 
	2. image - build docker file 
	3. container - running *instance* image 

### To know:

#### Concepts:
1. Docker can access the resources of the host 
2. Similar to #virtualized  machines, docker isolates software in it's own, settled, environment to enable multiple deployment of service, on a single server's unit
	- Containers can share or be based on other containers or images
	- They are not isolated that good 
```go 
container with file system 
	> 100+ containers who use it as default examplar 
```