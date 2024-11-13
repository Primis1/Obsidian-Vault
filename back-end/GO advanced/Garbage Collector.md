***
### Special values:
1. #garbage-collector 


### To know:

##### Where the values live:

1. Not every values are managed by #garbage-collector. no #pointer values are not cleaned by #garbage-collector 
	- Compiler arrange the memory to the lexical scope in which the value is created. Then it is easy for compiler to predetermine when to free the memory and emit the machine instructions 
	- Such memory allocation called "**stack allocation**", because space is stored on **`gorotine stack`**

2. Value who can't be stored in stack, so go-compiler cant determine its lifetime, are send to **`heap`**
	1. referenced like **`dynamic memory`** allocation
	- Can be send because - ` dynamic size` (slices, heaps)


- **`Object`** - is a dynamically allocated piece of memory that contains one or more values 
- **`Pointer`** - a memory address that references any value within an object. Like: `strings, slices, channels, maps, interfaces` all contain pointers which  #garbage-collector  traces 


- Object Graph - list of objects and pointers which create a graph of values, over which #garbage-collector  traverses. 
	- It starts from **roots** - values are guaranteed to be used in program (`local/global` variables)  
	
	- GC traverses all values in the program and **marks** these values as **alive**. Traverses it again, and those values who are not marked - being cleaned up 
	
	- Process called - **sweeping**
