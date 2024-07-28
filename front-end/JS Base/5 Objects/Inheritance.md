***
[[Objects]]
p.173
Special values:
Object.assign( ) - global method that used for inheritance between an objects  

To know:
1. Method Object.assign( ) expects two(or more) objects in it's values.
2. Object.assign( ) modifies and returns the first object, but it *does* *not* changes the second argument, where are all objects 
```ts
о = Object.assign({}, defaults, о);
// we are creating a new object 
```
3. Object.assign( ) - copies only those properties which *aren't repeated in the new object.*  