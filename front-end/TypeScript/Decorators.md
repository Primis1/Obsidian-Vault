***
[[TypeScript]]
#### Special values:
1. #decorator - is the `special function` that can be attached to class declaration
	- often used for adding a metadata to the class properties

#### To know:

##### Concepts:
1. #decorator can be declared before/to:
	1. Class as JS object and its `constructor` 
		1. replacement of `constructor` changes all properties of `class` 
	2. `Methods`, and its `parameters` 
	3. `Properties` and `access` methods 

2. They are ran in runtime, and executed before attached declaration 
3. *Arrow functions are not suited for decorators, they don't have their own context, but only `inheriting` surrounding context(`this`). Meanwhile regular anonymous `function()` do*
##### Implementation:
1. Class decorator:
```ts
// restricts extension and creating the new properties of the class
function sealed(constructor: Funtion) {
	Object.seal(constructor)
	Object.seal(constructor.prototype)
}

@sealed 
class MyClass {}
```
2. Constructor decorator:
```ts
// decorator extends the behavior of the Class (replaces print() method)
// we should create our own constructor, and accept all incomming parameters
function logger<T extends Function>(constructor: T): T {  
    let newConstructor: Function = function(...args: any[] ) {  
        let instance = new constructor(...args)  
        instance.age = 26  
        instance.print = function() {  
            console.log(this.name, this.age)  
        }  
        return instance  
    }  

// we assign to prototype chain to our constructor, and return it
    newConstructor.prototype = Object.create(constructor.prototype)  
    newConstructor.prototype.constructor = newConstructor;  
    return newConstructor  
}
```

2. 