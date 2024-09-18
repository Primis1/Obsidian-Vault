***
[[Asynchronous]]
### Special values:
1. #generators - are used for #concurrency  operations in JS/TS
	1. `*functionName` - indicates declaration of generator 
	2. #yield - used for `indicating` pause place of the execution within the #generator   

### To know:
1. We use #generators for implementing concurrency, a.k.a ==do something, stop, finish later on==
2. #generators still keep the basic properties of function, it can implement I/O as regular function
```ts
function *foo(x: number, y: number) {
  return x*y
}

console.log(foo(2, 34).next())
```
#### Implementation:
1. We may not invoke #generator like a regular function, instead we do use `next()` method of #generator object
2. #yield identifies place where execution will be stopped 
```ts 
var x = 1;

function *foo() {
  x++;
  yield
  console.log("x:", x);
}

function bar() {
  x++;
}

const it = foo()
it.next() //=> stopped execution

bar() //=> do our stuff 

it.next() // continue execution 
```
3. #yield can be used for additional arguments
	1. only paused #yield can accept arguments 
```ts 
function *foo(x) {
  x * (yield)
  
  console.log("x:", x);
}

foo(4).next()
```