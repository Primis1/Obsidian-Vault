***
[[JS advanced]]
Special values:
1. object - is data structure, that represents collection of properties 


To know:
1. Each primitive type (function, number, string, Regex, etc) can be be crated by using a constructor #new. In this case their type will be equal to #object, but not really the type it refers to
	- can be useful, if we remember that ==strings are immutable==, so to make any manipulations with that 

2. Object, Array, Function, Regex - are ==object literals by default, and do not require any constructors== 
3. property access(through dot) and index access give the same result, but [ " " ] allows to use any UTF-8 character to access the value or index
```js
  let myObj = {
    name: "Olaf"
  }
  const value = "name"
  myObj[value] //=> access the value
```
4. Objects keys can be any type, but they serialize into string:
```js
myObject[true] = "foo";
myObject[3] = "bar";
myObject[myObject] = "baz";
myObject["true"]; // "foo"
myObject["3"]; // "bar"
myObject["[object Object]"]; // "baz"
```

Object destructing:
```ts 
	const {a, b} = c
// same like 
	const a = c.a 
// we also can destruct the return values from the function
	function getata() {
		return a, b

	const {a, b} = await getData()
```