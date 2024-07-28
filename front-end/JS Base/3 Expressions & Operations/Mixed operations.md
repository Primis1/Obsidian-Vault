p.120

Special values:
delete - remove the values or method from object or array.
?? - 
?:  - ternary operator 

To know:
1. After deleting a property, and trying to get access to that property, we gets undefined
```ts
let o = {x: 1, y: 2} 

delete o.x

'x' in o     //=> false, porperty does not exist 
```