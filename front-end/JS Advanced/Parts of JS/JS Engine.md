***
[[Flow of JS]]
Special values:
1. JS engine - is a program that compiles JS code into ==machine code==, that can be executed later 
2. ==V8== - is most popular JS engine used in most of popular browsers 

To know:
1. JIT - just in time compilation used by JS engines.
	1. It works just like normal compilation process. `code -> byte code -> execution`. But still got one issue: 
		- In JIT compilation, code should be executed right after translation is finished, because it does ==not== have any execution files 

2. Steps within the engine:
	1. Code ==send into the engine==
	2. ==Parser== crops the code into ==tokens==
	3. These chunks are converted into ==Abstract Syntax Tree==(AST). ==Syntax checking is here==
		- ==AST== is tree-like data structure that represent functions, conditions, scopes, etc
	4. AST passed into interpreter which converts the AST into the ==byte code== 
	5. Byte code goes into optimizing compiler 
	6. The ==bytecode== should be ==immediately== run by the program

3. Engines are typically contain a #call-stack and heap
	1. ==Call== ==Stack== - is stack data structure, where the tasks are being organized in the order to execute properly 
	2. ==Heap== - represents the unstructured memory, that stores all the object needed by the program 

4. Engine responsibilities:
	1. Memory management 
	2. Memory allocation 
	3. Garbage deleting 

![[Pasted image 20240807171733.png]]