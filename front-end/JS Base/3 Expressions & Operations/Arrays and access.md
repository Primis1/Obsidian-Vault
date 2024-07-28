cc.90
Special values:
#array 
.length - it gets the number of index elements in the array. Every array has this property

```ts
const arr = [1, 2, 3]

arr length = 2 // remeber shit about 0
```

To know: 
1. Arrays nesting:
	
```ts
arr: nubmer[] = [1, [2, 3]]
```
	
2. We can create array without any values, but with the index for them: 
```ts
arr: number | void = [1,,3,,5]
```
	
3.  We have two ways of accesses to variables of objects and arrays. 
	1. First is "."
		```ts
		let o = {x: 1, y: [z: 3]}
		let a = [1, [2, 3]]
		
		о.х     => imagine it like cd command
		о.у.Z   => returns values of 3
		```
	2. Second is [ ]
	```ts
		let o = {x: 1, y: [z: 3]}
		let a = [о, 4, [5, 6]];
		
		о["х"]     => 1
		а[1]       => 4
		а[2]["1"]  => 6
		а[0].х     => 1
```
*Key difference*: "." can refer only on the name of the #object / #array, and is easier syntax, but when there isn't any names we can use [ ], because it allows us to get element by index number.
p.164
Also if we are using a [ ], the value within those brackets should be transformable into the strings .

4. .length if it is taken like the values of variable is equal to maximum number of the array. 
	1. ```
```ts
		for(let i = arr.length; i > 0; i--) {
		console.log(i - 1)
```
