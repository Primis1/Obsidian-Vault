cc.111
Special values:
#In - is used for properties checking of objects
#instanceof - checks does the exemplar (it is simple as shit)

To know: 

1. From the left side of "in" should be a the *property* 

2. At the left side there should be a value that can be transformed into the string, and on the right side there should be an object:
```ts
let obj = {x: 1, y: 2}

"x" in obj             // => true 


let data = [7,8,9];
"0" in data            // => true, 7  
1 in data              // => true, 8
3 in data              // => fasle, element 3 does not exist 
```

3. From the left side of the #instanceof should be an inherited property
```ts
let d = new Object()

d instanceof Object()
d instanceof Date   // => true: объект d был создан с помощью Dated
d instanceof Object // => true: все объекты являются экземплярами Object
d instanceof Number // => false: d is not an object of Number
```
