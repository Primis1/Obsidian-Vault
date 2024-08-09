***
[[Promises & Asynchronous]]
Special values:
1. #async - makes the function return promise object 
2. #await - 

To know:
1. #async 
	- wraps function into the promise, function's ==return== value, becomes ==fulfilled== value of promise  
	- Async functions ==ALWAYS== returns promise, if the value is not a promise, function creates a wrapper 

2. #await 
	- can be used ==only within== the #async function, and only ==for promise-base objects==
	- #async function ==without== any #await statements, ==are going to run synchronously==.  
	- after each time #await is assigned to the promise object, the function *awaits* for this line of code to be resolved
		- `It works like then() handler, when it awaits to the initial promise being settled
		- When we assign awaits to the promise objects, we can act with like with sync one

```ts
const p = new Promise((res, rej) => {
  res(1);
});
// the same thing 
async function asyncReturn() {
  return p;
}
```