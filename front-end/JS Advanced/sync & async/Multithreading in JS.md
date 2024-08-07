***
[[JS advanced]]
Special values: 
1. Ways to implemetn multithreading in JS
	1. Web Worker - allow to divide logic into several threads by separating it into the different file. It should be fully incapsulated from the current thread, i.e do the job somewhere else or just in parallel 
	2. Asynchronous Programming - when the program does not wait for a process to be fully executed 
2. JS is single treaded language 
	- Single-threaded means one line of code run at once


To know:
- Two ways to do multithreading in JS 
1. Via ==Web Workers== 
	1. Through the separation, encapsulation and passing as logic *copy* of itself. Web workers can escape the single threaded environment, by creating its own thread
	2. Web Worker do ==NOT== interact with DOM elements, therefore they don't block the work of DOM tree

2. Via Asynchronous programming 
	1. Interpreter skips the asynchronous function block, until it settled. Only after JS add the function into the call-stack