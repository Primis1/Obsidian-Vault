***
#### Special values:
1. #higher-order-function - function that take another function as argument or returns it 
2. #closure - `замикания`, ability of function to remember its surrounding 
3. [ [ Scope ] ] - in de `devtools`, everything that is wrapped in two brackets is 

#### To know:

##### Concepts:
1. #closure, used for inner function to access the objects of outer scope. We can accomplish it by 
2. Compiler determines the environment accessibility to given `function` based on its definition, when compiling it 
3. Lexical environment is determined once and keeps through entire program execution. *JS is statically scoped*
4. function inside of `scope` do share the same environment 
5. Patterns:
	1. module design pattern - group our code into  
	2. #higher-order-function 
##### Implementation:
- #closure 
```js
var a = 'static';

function f1() {
   console.log(a);
}

function f2() {
   var a = 'dynamic';
   f1();
}

f2(); // "static"


// example 2
var a = 'easy';

(function() {
   var b = 'easy';

   function f1() {
      console.log(a, b);
   }

   function f2() {
      var a = 'difficult';
      var b = 'difficult';
      f1();
   }

   f2(); // easy easy 
})();

```

- #higher-order-function 
```go
func Spere(vol func(radius float32) float32) {
	fmt.Printf("volume %v", vol(5))
}

func main() {
	volume := func(radius float32) float32{
		result := 4/3 * math.Pi * radius * radius * radius
		return result
	}

	Spere(volume)
}
```