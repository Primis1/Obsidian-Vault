***
[[Types Chapter]]
cc.80
Special values: 
1. variable - ==is named place of memory== where the actual data is stored 
2. Global and local field of view
3. #this - Jesus Christ, i fully got it, why the heck no-one explain it like
	"by using a .this keyword you can get an access the variables in locked/local fields of view" 


To Know: 
1. If variable is defied inside of curvy brackets, it will be like cage for this variable.

2. We can set the same to the variable inside of the curved brackets or inside of any other packable block-code
	but we SHOULD NOT do that.
	```ts
	const x: number = 1   
	if(x === 1) {
		let x: number = 2      //
		console.log(x) // => 2/ it is local field of view
	}
		console.log(x) // => 1 / look at the const / we're in global field of view  
	++x                // => ERROR
```