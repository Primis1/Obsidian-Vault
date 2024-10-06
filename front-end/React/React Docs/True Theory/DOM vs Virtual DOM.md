### Special values:
1. DOM tree - **HTML DOM** model is constructed as a tree of **Objects**
	
2. Virtual DOM/React component tree - is lighter version of original DOM, it perhaps exist only within  the react environment 

### To know:
1. VDOM is lighter and faster than DOM tree.
2. VDOM has three different stages:
	1. We making a change to the VD
	2. React compares it to the previous VD, and re-renders *changed* parts, by using a reconciliation 
	3. Actual change to the render of classic DOM
![[Pasted image 20240423171605.png]]
