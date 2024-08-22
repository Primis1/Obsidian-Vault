***
[[CPU]]
Special values:
1. process - is a program dispatched from the ready state and are scheduled in the CPU for the execution, process do NOT share the memory with other processes 
2. #thread - is the segment of the process, which means that process can have multiple threads and these threads are stored within the process 

To know:
1. States:
	1. Process 
		- new\
		- ready 
		- running 
		- waiting 
		- terminated 
		- suspended 
	
	2. Thread 
		- running
		- ready 
		- blocked 
		
2. Means 
	1. Process 
		- Process means any execution program 
		- Slower creation/termination time 
		- Less efficient in terms of communication 
		- It is isolated, and does NOT share data with others 
		- In case of lock of some processes, it won't affect any other 
		- Changes to parent process does NOT affect children 
	1. Thread 
		- Thread is a segment of process 
		- It is generally faster than process, in most means like creation/termination/switching 
		- They can actively share memory between each other 
		- If, example, one user's thread is blocked, all other user threads are going to get blocked()
![[Pasted image 20240817053209.png]]