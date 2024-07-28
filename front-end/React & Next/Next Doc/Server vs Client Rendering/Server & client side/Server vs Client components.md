Special values:
"use client" -  make a component render on a client
#server - server 
#client  - is the browser or user's device 

To know:

***

1. The difference between SC and CC is HUGE, in general there are a bunch rules that could, that make a difference in code writing on server and client.
	1. Client Components:
		1. If we are on a client part, we should import function, hooks, and methods of the library from the server part
		2. CC are working slower due place where they are rendering.
		3. We can use async functions, but the component itself can't be asynchronous functions(maybe even promises) there
	2. Server Component:  
		1. We can't use any react hooks, but we can use some NJS stuff that connected URL(or even more specific methods, idk yet)

![[Pasted image 20240425185103.png]]