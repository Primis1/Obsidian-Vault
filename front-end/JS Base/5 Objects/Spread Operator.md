p.179
Special values:
[ . . . ] - #spread operator. Operator spreads or divides or parses the properties from the object

To know:

1. The spread operator *spreads* or *divides* or *parses* or giving an access to within properties and values of the object
	```ts
	let position = { x: 1 , y: 2}
	
	let size = { width: 100, heigh: 75}
	
	let rect = { …position, …size} 
	
	rect.x + rect.width  //=> 102 
	```
	1. There are another ways to use ... operator in in JS, but it works like in examples above only with objects literals
	2. . . . operator spreads only own properties of an object, and avoids the inherited one
	3.  If parsing object has the same name that some other values, interpreter will use the last of those as the right one
```ts
	let o = {x: 1}
	let z = {x: 2, ...o}
	z.x     //=> 1

	let q = {...o, x: 2}
	q.x     //=> 2
```


4. Lastly, . . . is slow as shit, and it iterates with linear effectivity of O(n)
