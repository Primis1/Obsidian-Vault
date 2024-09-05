***
[[Computer Science]]
####  Special values:
1. Concurrency - is the ability of the program to execute its code in ==asynchronous== ==manner==. Blocks of code won't wait one for another to fully execute 

2. Parallelism - is the process of simultaneous execution of code in ==multiple threads==

#### To know:
##### Concurrency:
- ==Pros==
	1. Optimal resource allocation 
	2. Scalability - facilitating the execution of high-number of operations 
	3. Better average response time
- ==Cons==
	1. State and task coordination 
	2. Share of global resource 
	
	- ##### Disasters: 
	3. `Race-condition` - when actions are concurrent, raises the question "which task should go first"
	4. `Starvation` - process when ==lower== ==priority== tasks are ==prevented== to ==execute== by ==higher==-==priority== tasks
	5. `Deadlock` - situations where processes can't be executed because each is waiting for other to release its resources
##### Parallelism:
- ==Pros==
	1. It can significantly increase the speed up intensive tasks 
	2. *Non-Blocking* - operations does not block the main thread
	3. Non-local resource - parallelism can be launched from different place
	4. The error in one thread won't affect the paralleled 
	
- ==Cons==
	1. Managing of multiple separated threads can be problematic 
	2. Can be less productive because of the starting point for multiple paralleled process 
![[Pasted image 20240806033945.png]]