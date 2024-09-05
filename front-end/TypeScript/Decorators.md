***
[[TypeScript]]
### Special values:
1. #decorator - is the `special function` that can be attached to any class declaration`
	- often used for adding a metadata to the class properties
2. #decorator factories - are function that returns another functions, which is being a decorator 

### To know:

#### Concepts:
1. #decorator are function that accepts and then modifies the `prototype` of any class declaration, used for #decorator's flexibility 
2. #decorator can be declared before/to:
	1. `Class` as JS object and its `constructor` 
		1. replacement of `constructor` changes all properties of `class` 
	2. `Methods`, and its `parameters` 
	3. `Properties` and `access` methods 


3. They are ran in runtime, and executed before attached declaration 

4. *Arrow functions are not suited for decorators, they don't have their own context, but only `inheriting` surrounding context(`this`). Meanwhile regular anonymous `function()` do refers to context its being executed*
#### Implementation:
1. Class #decorator:
	- `Arguments`:
	- `class constructor method`  
```ts
// restricts extension and creating the new properties of the class
function sealed(constructor: Funtion) {
	Object.seal(constructor)
	Object.seal(constructor.prototype)
}

@sealed 
class MyClass {}
```

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

2. Methods #decorator:
	- Arguments:
	1.  
```ts

```
3. Property #decorator:
	- Arguments:
		1. `target`: refers to `class prototype` of property instances
		2. `memberName`: name of decorated property 
```ts
const allowlist = ["Jon", "Olaf"];

// decorators does not provide way to modify the property by itself, but we're smart so we just do that through object prototype. Ohh and it is a factory
function allow(allowlist: string[]) {
  return (target: any, memberName: string) => {
    let currentData = target[memberName];
    Object.defineProperty(target, memberName, {
      set: (newValue: any) => {
        if (!allowlist.includes(newValue)) {
          return;
        }
        currentData = newValue;
      },
      get: () => currentData,
    });
  };
}
class Example {
  @allow(allowed)
  name = "Olaf";
}

const example = new Example();

example.name = "Jane"
console.table(example.name) // Olaf

example.name = "Jon"
console.table(example.name) // Jon
```
4. #decorator factory:
```ts 

```