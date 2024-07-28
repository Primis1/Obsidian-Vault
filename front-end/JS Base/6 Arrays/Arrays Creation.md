Special values:
1. . . . - #spread operator also works with arrays, in simple words it is just a shortcut.

To know: 
1. Every array creates by using a square brackets [ ] and elements within the array should be divided by coma
	1. Elements not necessary should be a static values, but also a dynamic expressions:
	```ts
	let base: number = 1024
	
	let arr: number[] = [base, base+1, base+2, base+3] 
	```
	3. Arrays could also contain an object literal: 
	```ts 
	let table = [[1, {x: 1, y: 2}], [2, {х: 3, у: 4}]]
	```
	4. Values within the array can be skipped([[Arrays and access]]), and attempt to access the values will cause the *undefined*
	```ts
	let count = [ 1, ,3];  // Элементы находятся по индексам 0 и 2.
	//По индексу 1 элемента нет
	let undefs =[,,];  // Массив, не содержащий элементов,
	//но имеющий длину 2
	```
2. #spread operator helps us to put literals of one array into another, it spreads every individual element inside of the "container" array.
	```ts 
	const a: number[] = [2,3,4]

	const b: number[] = [1, ...a, 5] //=> 1, 2, 3, 4, 5
	```
	1. Every iterated values can be counted as array(strings are arrays of letter btw), so spread operator can separate every element of the string into the letters
	```ts
	let digits = [..."0123456789ABCDEF"];
	digits  // => ["0",”1","2","3",”4","5”,"б",”7",”8”,"9",
	//  "А","В","С","D","Е", "F"]
	```
	2. 