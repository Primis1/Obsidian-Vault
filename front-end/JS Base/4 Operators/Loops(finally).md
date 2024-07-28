Special values:
1. #while 
2. #for  
3. #for/of 
```ts
	Object.key( ) || Object.values( )
```
4. #for/in - the same like #for/of but iterates for every parameter of an object
5. #for/await  
6. #do/while

To know: 
1. *While* - if the expression is === false, interpreter *skips* the operator while  
	
```ts
while(expression/condition) {
	operator/code that should be repeated 
}

let count = 0 

while(count < 10) {
	console.log(count)  //=> operator
	count++             //=> incementetion 
}
```
	
2. #for - we are initialize the variable, set the condition, and give a side effect for every loop cycle for this variable, instead of writing that in the operator.     
	```ts 
	for(initialization; check; side effect){
		operator/code that should be repeated 
	}
	```
		
	1. We can skip every part of the for loop, but there must be two *semicolons*, but if I'll skip checking, the loop will be infinite(just like *while(true)* ) 
	```ts
	for(initialization; ; side effect) {
	
	}
	```
		
	2. *Initialized variable will render at least one time*
	3. The process is going in this order:
	```ts
	for(1; 2; 4) {
		3
	}
	
	// but after the first run the order is changed a lil
	
	for(skip because it was already created; 1; 3) {
		2
	}
	```
	4. Confining the number of iterated values and map alternative:
	   ```ts
	   let map1 = new Map<string, string | number>([
		  ['name', 'Bobby Hadz'],
		  ['country', 'Germany'],
		  ['age', 30],
		]);
		
		let counter = 0;
		let limit = 2; // Set your limit
		
		// Using for...of loop
		for (let [key, value] of map1) {
		  if (counter === limit) {
		    break;
		  }
		  console.log(key, value);
		  counter++;
		}
		
		// Resetting counter
		counter = 0;
		
		// Using forEach method
		map1.forEach((value, key) => {
		  if (counter === limit) {
		    return;
		  }
		  console.log(key, value);
		  counter++;
		});   
``` 
	
3. #for/of - is alternative to *for in*, and it is completely different from *for* loop, because it can work only with iterated objects  
	1. We don't do any conditions and side effects 
	2. The loop continuous until it reach the last element of the array
```ts
		let data = [1, 2, 3, 4, 5, 6, 7, 8, 9], sum = 0; 
		for(let elements of data ) {
			sum += data
		}
		sum  //=> 45
``` 

4. #for/of - can also work with an objects in this way (but better just use #for/in) :
```ts
let o = {x: 1, y; 1}, sum = 0

for(let count of Object.values(o)) {
	sum += count
}

sum      //=> 2
```

