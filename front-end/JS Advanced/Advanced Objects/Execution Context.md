***
### Special values:
1. Execution Context - is something that stores information about environment, (or the thing that #this keyword returns)

### To know:
- #this when called in function refers to `global-bject` 
```ts
function show() {
    return this // logs a global object or undefined if in "use strict"
}
```
- #this when called in `arrow function`, refers to context scope it is executed in, i.e because `arrow functions` does not have its own `this`
```ts
const func = {
	name: "Olaf",
	age: 12
	that: () => {
		return this
	}
} 
```
- #this when called in object refers to `object
```ts
const obj = {
    return this // logs {}, i.e the inheritet/outside area context 
}
```
