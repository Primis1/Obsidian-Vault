***
[[Multithreading in JS]]
Special values:
1. Web-worker - incapsulated functionality existing outside of application. Used to create additional thread  

To know:
1. ==Web Workers== are used to escape the single threaded environment. Key feature of Web-workers is that, they ==don't== ==block== DOM, unlike ==async== code
	2. ==Requirements== for being a web-worker:
		1. Live in its own file - process should ==NOT== interact with user interface 
		2. Function is passed by copy 
		3. No global states nor variables 
	
2. ==Web-Workers=: 
	1. Should not contain nor interact with:
		1. The ==parent== objects
		2. The ==window== objects 
		3. The ==document== objects 
		4. The ==DOM== 
	
	2.  ==Can have access to:==
		1. The ==local== objects
		2. The ==navigation== objects 
		3. ==XMLHttpRequests==
		4. The ==Application== ==cache== 
		5. Spawning other web-worker 
		6. Importing external script 

3. Implementation:
```ts 

```