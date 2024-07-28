***
cc.60 
Special values:
```ts
s.split(", ") // => ["Hello", "world"]: разбивает по строке разделителя
s.slice (1,4) // => "ell": то же самое
s.slice(-3)   // => "rid": последние 3 символа

// Modifying of existing verstion of string 

s.replace ("Но", "уа")  // => "Heya, world"
s.toLowerCase( )        // => "hello, world"
s.toUpperCase( )        // => "HELLO, WORLD"

// Search within the string 

s.indexOf("1")// => 2: позиция первой буквы 1
s.indexOf("1", 3)    // => 3: позиция первой буквы 1,
					 // начиная с 3-й позиции
s.indexOf("zz")      // => -1: s не включает подстроку "zz"
s.lastlndexOf("1")   // => 10: позиция последней буквы 1

// Additional stuff

 '<>'.repeat(5)      // => '<><><><><>' conkationation
```


**To know:** 

1. Method that changes already existing string - **does not** **exist**. All tools returns NEW string with settled parameters
2. Operator .length can work with individual 16 bit values
3. If the datatype could be converted into the array, method could be applied. ==Basically all positive types in JS could have be an array at some point==. String are collection of symbols, numbers too, objects could contain an arrays, perhaps bool not, but 

```ts
let s = "Hello, world"
s[s.length-1]     => "Hello, worl" 
```