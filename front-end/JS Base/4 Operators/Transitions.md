p.145
Special values:
#break - stop the process 
#continue - restarts the loop from the next iteration   
#return - returns the value. { } for object, ( ) for not 
#throw - connected to Error object in JS, go with try/catch/finally
#try, #catch  - are used for checking of exceptions.
#exception - it is a signal that report the appearance of weird condition or Error. Generation of     #exception is the warning about such unexpected condition or Error.

To know: 
1. #break operator is used to exit from the loop, and often used when there is no purpose to make a logic for stopping the *loop* (yea, only for loops or operator switch... fuck have to read about that too)
	1.  *break* value   
	```ts
	for(let i = 0; i < arr.length; i++) {
		if (arr[i] === target) break;
	}
```
	2. Also check this syntax a[i], here *i* is in brackets because it is used as value for the array.
	```ts
let matrix = getDataO ; // Получить откуда-то двумерный массив чисел
// Просуммировать все числа в матрице
let sum = 0, success = false;

// Начать с помеченного оператора, из которого можно выйти
// в случае возникновения ошибки
computeSum: if (matrix) {
	for (let x = 0; x < matrix, length; x++) {
			let row = matrix [x];
	if (!row) break computeSum;        // it stops the right object 
	for (let у = 0; у < row. length; y++) {
		let cell = row[y);
		if (isNaN(cell)) break computeSum;
		sum += cell;
	}
	success = true;
}
```

2. #continue operator is similar to #break, but instead of exit the loop, it restarts it right after the loop reach the operator. For different loops, this creates different consequences
	
	1. In cycle #while it gets back to *check* part, and if === true, the loop starts again 
	2. In cycle #for it calculates the increment part, and after that *check* expression, if === true, the loop starts again
	3. In cycle #for/of it returns to next iteration value or property.
```ts
for(let i = 0; i < arr.length; i++) {
	if(!arr[i]) continue;

	total += arr[i];
}
```

3. #return - remember that every function has a value, so operator #return returns the value of an expression inside of the function.
	1. can prevent the circle of for loop
	```ts
	function sqr(x: number) {return x*x}
	sqr(20)  //=> 40, but without return it will throw undefiend   

	function solution(strings: string) {
		let obj: string = '';
		for (const v of strings) {
			console.log(v); //?
			if (v === v.toUpperCase()) {
				// will stop iterating after first char
				return obj += ` ${v}`;
			} else {
				obj += v;
			}
		}
		console.log(obj); //?
	
		return obj.trim(); //?
	}

	solution('aBcDcD'); //?
```

4. #throw -  after call of the operator, JS interpretate the stops the work of the program and begin looking for #catch operator of function #try, it should be used with #try or within the function
	```ts
	function factorial(x: number) {
		if(x < 0) throw new Error("Значение х не должно быть отрицательным")
		
		let f;
		for(f = 1; x > 1; x *= f; x--)
		return f;
	}

factorial()
```

5. #try and #catch.  Part with #try is necessary and and can't be skipped. 
	1. Part with #catch could be activated only if block of code inside the try - produce exception. 
	2. Code inside of operator #finally is processing despite of the actions inside of #try
	3. The argument of catch could be skipped, if we don't need the value of an exception, but need to catch and stop those error in the whole code
	```ts 
	function parseJson<T>(s: T) {
		try {
			reuturn JSON.parse(s)
		} catch {
			return undefined 
		}
	}
```