***
[[Asynchronous JS]]
Special values:
1. #promise - is and object that can be accessed by callback function after promise if settled(we do not see this value rn, but want to do manipulations in the future)
	1. ==async operations are kind of operation that requires unknown/some time for it's execution.== 
		- When we do async operations, each ==time== we have to wait. Unlike sync programs, if we do implement async. The program won't wait a second to go after the executing async statement
	2. sync programming means executing of next block of code, starts only after previous finishes completely
2. async/await - keywords are used to make a function return a promise and wait for it to be settled 

To know: 
![[Pasted image 20240805175603.png]]
- Details:
1. Promise represents the eventual completion/failure of the async operation and its result value 
2. If ==promise== was fulfilled/rejected before the ==assignation== of the handler      (==then==), promise be executed in the callback ==anyways== 

- Promise states:
1. ==Pending== - initial state, neither resolved nor rejected 
2. ==Fulfilled== - promise successfully ==resolved==, fulfilled state can contain ==value== which was requested  
3. ==Rejected== - asynchronous operation has failed, rejected state can contain the ==reason(error)==

- Promise handlers 
1. Handlers can react on a *settled* promise state, but not on pending  
2. Promises does ==not have== any protocols to ==terminate== the request process

3. ==then( )== - *returns the promise object immediately after the promise object become settled*. `then( )` has ==two== ==callback== functions as arguments: 
	1. ==onFulfilled== - async function executes when promise becomes fulfill. Its fulfill argument, `value`, is being assigned as the ==fulfill== value of the Promise then( ) is attached to
	2. ==onRejected== - async function executes when the promise becomes *==rejected==*. Its fulfill argument, `reason`, is being assigned as the ==reject== of the Promise then( ) is attached to
4. ==catch( )== - *returns the promise object immediately after the promise object become settled*. Method used for promise error handling. Can accept one argument. `catch( )` has an an argument `onRejected`, it work in the same way as in `then( )`
5. ==finally( )== - *returns the promise object immediately after the promise object become settled*. Method used when we want to do something with the promise, regardless of the promise state. ==Doesn't provide any arguments== ; )

- Syntax: 
1. Object promise contains two ==functions as the parameter==: resolveFunc & rejectFunc.
2. Promise handlers are object methods that can process the promise state 
	1. then( ) - Promise.prototype.then(response => { })  
	2. catch( ) - Promise.prototype.catch( ) 
	3. finally( ) - Promise.prototype.finally( )
```js
let isLoading = true 

// fetch returns promise 
fetch("https://some-path.com").then(resolved => {
    const content = resolved.headers.get("content-type")
    if(content && content.includes("application/json")) {
        return resolved.json
    }
}).catch(e => {
    console.error("Opps, response is not JSON! \n", e)
}).finally(()=> {
    isLoading = false
})
```