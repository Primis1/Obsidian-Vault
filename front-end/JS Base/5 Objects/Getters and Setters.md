p.183
Special values:  
#get - allows us to have access to the values of the method
#set - allows us modify parameters of the method in the object
1. Formal parameters - doesn’t have an actual value, or doesn’t have a default value  
2. Actual parameters - has its own values

To know:

1. #get allows us to take the process of the method or values of the method.
	1. Getter should *not* have any formal parameters
	2. After the access method, I should put a coma
```ts
const obj = {
	x: 2,
	
	get method() {
		return this.x++
	}
}
obj.method   //=> 4; if we didn't use get before the method, as the result we would get a name of the method   
```
2. #set 
```ts 
const obj = {
...

	set method({x, y}: Number) {
		x * this.x 
	}
}

obj.method = 2  //=> 4

obj.method      //=> 6 it contains the number 2 that we handed in earlier
```