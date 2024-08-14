***
[[JS object]]
Special values:
1. `constructor( )` - method where we can manipulate arguments of the class itself, which are passed during initialization `const obj = new Class(2, 3)`
2. `this` - used for referencing to environment variable    
To know:
1. `constructor()` - is called when the object is initialized 
```ts
class FetcClass {
  constructor() {
    console.log("constructor")
  }
}

const obj = new FetcClass

// constructor 
```
2. With use of this, we can access the environment variables, `if they are declared`, otherwise this returns and empty string 