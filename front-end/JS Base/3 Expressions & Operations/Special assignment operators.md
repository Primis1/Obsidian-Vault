cc.115
Special values:
1. these operands used for simplifying reassigning: 
 ```ts
 -= 
 +=
 *=
 /=
 %=
```

To know:
1. All operators above are simple shortcuts for its regular operators:
```ts
cosnt x:number = 1
const y:number = 2

y += x     //=> 3 

//it's the same as:

y = y + x  //=> 3
```