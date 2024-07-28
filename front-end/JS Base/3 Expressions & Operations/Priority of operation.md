Special values:
ALL OPERATORS 
```ts
**  //  degree
%   // 
...
```

To know:
cc.96
1. Every operator, from "+" and "-" to "??" and ">>" have its own priory in compiling
2. We can set the priority of operations by covering them into **"( )".** Yes just like in Math
```ts
(x, y, z) =>  (x + y) / z
```
3. Access methods are above of all priority.
```ts
typeof my.functions[х](у)

// typeof will be used only after object "funtion" take access to the array
``` 
4. Associativity is being used if operator are equal in priority line, in this case compilor performs operation from left, to right, or from  right to the left:
   ```ts
   (x, y, z) =>  x && y && z
	
	У = а ** b ** с;
	х = — у;
	w = х = у = z;
	q = a?b:c?d:e?f:g;

// this is equal to 

	у = (а ** (Ь ** с));
	х = - (-у) ;
	w = (х = (у = z));
	q = a?b:(c?d:(e?f:g));
```
5. Understanding of priority operations is'nt that important btw
