***
[[Objects]]
p.179
Special values:
1. .toString( ) - JS interpreter use it under the hood. Like concatenation with "+" operator

2. .toLocaleString( ) - it is actually the like .toString, but it works slightly different

3. valuesOf( ) - is a THIRD similar to .toString( ) method, it also works under the hood, and JS interpreter uses is to change the default type(usually from string to number) to the needed one.

4. sort( ) - used to sort an arrays. 

5. JSON.stringify( ) - could transfer object into the string, and does this in JSON format 

6. String( ) - transfers everything into literal string 

To know: 
1. Example of how .toLocaleString( ) works  

```ts
	let point = {
		х: 1,
		У: 2,
		toString: function() { return `(${this.x}, ${this.y})`; }
	};
	String (point)  // => "(1, 2)": toStringO применяется
	// для преобразований в строки
```

2. We also have to use a method after calling the parameter of an object to which we want use a .toLocaleString( )
```ts
	let point = {
		x: 1000,
		y: 2000,
		toString: function() { return '($ { th is .x ), $ { th is.y } )'; },
		toLocaleString: function() {
			return 4(${this.x.toLocaleString()), ${this.y.toLocaleString()})
		}
	};
		point .toString( )  // =>  "(1000, 2000)"
		point .toLocaleString( )  // =>  "(1,000, 2,000)":  обратите внимание
	//на наличие разделителей тысяч
```

3. JSON.stringify( ) & String( )
```ts
  const id = String(params); => [object object]
  const bla = JSON.stringify(params) => "params": {"bla"}

  const id = String(params.params["note-id"]); => id 
  const bla = JSON.stringify(params.params["note-id"]) => "id" 
```

4. sort( )
```ts
 const array: number[] = [2, 1, 4, 3]

 function sortArr(arr: number[]) {
	 return arr.sort(a-b)
 }

sortArr(array) = [1, 2, 3, 4]
```