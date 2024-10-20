***
[[GO advanced]]
### Special values:
1. #mutex - mechanism which ensures that one #goroutine will not allow shared resources in the same time 
	1. #mutex - is one kind of #lock defense mechanism, which manages the access to the resource within concurrent programming  
### To know:

#### Concepts:
1. #mutex are used to prevent `race-condition` between #goroutine 
	1. `race-condition` - process when two threads are trying to access and modify the same data in the memory 
2. #mutex restricts access to resource for multiple threads  
#### Implementation:

