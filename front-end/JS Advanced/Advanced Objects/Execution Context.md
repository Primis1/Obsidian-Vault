***
#### Special values:
1. Execution Context - is something that stores information about environment, (or the thing that #this keyword returns)

#### To know:
```ts
function show() {
    console.log(this); // logs a global object or undefined if in "use strict"
}

show() // logs global object 


const func = function() {
	console.log(this)
} 

func()

const obj = {
    show: () => console.log(this) // logs {}, i.e the inheritet/outside area context 
}
```