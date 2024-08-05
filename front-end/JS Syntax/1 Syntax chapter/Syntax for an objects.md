p.177
[[Syntax Chapter]]
Special values:

To know:
1. In new versions of JS we can easily simplify the code for inheritance 
    
```ts

let  x = 1;  y = 2

let o = {x, y}

o.x + o.y              //=> 3

```

p.180
2. Shorter syntax for methods within the object:
```ts
let obj = {
	x = x
	area(): return this.x * this.x
	 
} 
```