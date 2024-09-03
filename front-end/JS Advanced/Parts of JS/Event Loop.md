***
[[JS Runtime's]]
Special values:
1. Event-Loop - a separated mechanism for I/O. It is a tool that manages functionality between the runtime's components  
	1. it can differ in different environments 

2. Event Loop parts
	- #call-stack - it applies first-in, last-out system, it can be overflowed  
	- #call-queue - it stores all asynchronous/delayed execution calls. After callback is fulfilled, queue sends it back into the #call-stack
	- #web-api - set of tools that provided by the environment to extend JS functionality 

To know:
1. Parts purpose
	1. Call-Stack:
		1. Stack executes all ==synchronous== blocks ==first== 
		
		2. ==Micro==-tasks have ==higher== priority than 
		
		3. ==Macro== tasks are laying at the bottom of the call stack. if it contain any other micro-tasks, they are "==unpacked==" and ==processed== one-by-one, after they're ==done== call stack ==removes== ==macro==-==task== from the ==call==-==stack==
		
	1. Call-Queue:
		1. New tasks from the queue can be passed into the ==stack== only when it is ==empty==

		2. Queue divides into ==Macro and Micro tasks queues== 
	
		- ==Macro== task:
			- Timers 
			- Events - mouse, keyboard, form, etc actions
		
		- ==Micro== tasks are created by:
			- Promises 
			- queueMicrotask - special method 
			- mutationObserver - 
	
	1. Web API:
		1. Used for "registration" of events, and it's implementation. Do the work and send task into the queue 

2. General flow:
![[Pasted image 20240902200427.png]]