***
[[Data Structures]]
### Special values:
1. #stack - is a linear data structure, that used for element execution. It uses a "last in, first out" approach.
	1. min/max #stack - the same, but keep track on the min/max value in the stack, provide $$
![[Pasted image 20240526000642.png]]
2. #queue - data-structure, which elements can be accessed by ONLY previous element. 
### To know:

#### Stack:
1. We can excess only the ==top== element of the stack(it consists from a vertical pointer).
2. Types of stack:
	1. ==Fixed Size Stack==:
		1. AS THE NAME DICTATED, the fixed stack can't shrink in size, or extend in any way possible, when the amount of requests in the the stack is full, and we are trying to add another element into the stack it throws our beloved ==Stack Overflow==  
	2. ==Dynamic Size Stack==:
		1. It can shrink dependently of amount of elements the stack. When it is full, stack growth to contain a new element, just like it compresses if the stack is empty. 
		2. It uses a [linked-list](obsidian://open?vault=Obsidian%20Vault&file=CS%2FMemory%20%26%20Data%2FData%20Types%20%26%20Structures%2FData%20Types) data structure to fast resize of stack 

Implementation 
```ts

```

#### Priority queue:
1. Same as queue, but each element has its ==priority level==. therefore, elements are inserted based on that level

2. Elements are re-ordered when changes

3. Priority queues - can be implemented through heaps:
