***
[[Computer Science]]
### Special values:

- Kinds of #design-patterns:
	1. Creational - focused towards how to instantiate an `object` or group of related `objects`
	2. Structural - focused on `object` composition, or how `entities` can use one another 
	3. Behavioral - focused on communication between `entities` or `object`. These kinds of patterns can also be applied towards other kinds

### To know:

#### Creational:
1. #simple-factory - *object for creating other objects*
	1. Function or method that return object `prototype` which assumed to be `new`

2. #factory-method - it provide a way to delegate the instantiation of `object/class ` to its `child`
	1. We have class `door` and do let the `child` specify what *kind* of door they want, or even allow such extendibility 