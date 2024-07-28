***
[[Types Chapter]]
Special values: 
1.  non-mutability - 
To know:
1.  #object and arrays are never equal true, even with comparison to themself: 
```ts
let array: number[] = [1, 2, 3]
let obj = {x: "hello"}

array === array  // => false

boj === obj      // => false
```
	
2. We can change the current #array && #object(remember that we can't modify the strings, but only create the new one by using methods like .toUpperCase).
	
```ts
obj.x = "good-bye"

obj.y = "hello, world"

array[0] = 2
```
	
	
comparison of an obj could be equal to **true** only if the **within** objects are the same
	
```ts
let а = []; // Переменная а ссылается на пустой массив
let b = а;  // Теперь на тот же самый массив ссылается переменная b
b[0] = 1;   // Изменить массив, на который ссылается переменная b
а[0]        // => 1: изменение также будет видимым через переменную а
а === b     // => true: а и b ссылаются на тот же самый объект, поэтому они равны
```

cc.78
2.  Empty #array is equal to 0
```ts
arr = []    // => 0
arr = [99]  // => 99
```