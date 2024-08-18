***
[Threads]([Single-Threaded vs Multi-Threaded Servers: An Experiment with Node.js and Java - DEV Community](https://dev.to/michinoins/single-threaded-vs-multi-threaded-servers-an-experiment-with-nodejs-and-java-3183#:~:text=A%20multi-threaded%20server%20can,one%20task%20at%20a%20time))
[[CPU]]
Special values:
1. #thread - *is a single sequential controlled process/data flow within a program*
	1. single-thread - it can process only one task at the time   
	2. multi-thread - it can execute process concurrently, by creating *multiple* threads in different CPU cores

To know:
1. #thread - ==in terms of computer processing, is the channel that goes within a single CPU core.== 
	1. Single threaded app can use advantage of only main-thread(single core of CPU)
	2. Multi-threaded app on the other hand can use ==multiple== ==cores== 

2. *==C10k problem==* - known to single page web-servers, when it getting hard for a server to manage 10 thousands concurrent connections  

3. ==Single==-thread applications:
	1. ==Pros==: 
		1. easier development, because we don't have to manage multiple threads
		2. ==less== memory usage
		3. Better for I/O operations 
	2. ==Cons==: 
		1. with tons of connections it ==becomes== ==slow==
		2. unable to execute ==tasks== ==in parallel== 

4. ==Multi==-tread applications:
	1. ==Pros==: 
		1. ==faster== ==approach== for multiple CPU-intensives
		2. lead to ==better== ==performance== because of parallel task execution
	2. ==Cons==:
		1. can reduce its speed if quantity of intensive tasks becomes abnormal 

![[Pasted image 20240726213950.png]]