***
### Special values:
1. #garbage-collector 


### To know:

#### Concepts:
1. Not every values are managed by #garbage-collector. no #pointer values are not cleaned by #garbage-collector 
	- Compiler arrange the memory to the lexical scope in which the value is created. Then it is easy for compiler to predetermine when to free the memory and emit the machine instructions 
	- Such memory allocation called - "stack **allocation**"
	- Such memory allocation called "**stack allocation**", because space is stored on **`gorotine stack`**

##### Garbage collector:
1. 