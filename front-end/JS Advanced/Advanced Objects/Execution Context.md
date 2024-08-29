***
#### Special values:
1. Execution Context - is something that stores information about environment, (or the thing that #this keyword returns)

#### To know:
```ts
function show() {
    console.log(this); // returns a global object or undefined if in "use strict"
}

const obj= {
    show: () => console.log(this) // returns {} after invoking
}
```