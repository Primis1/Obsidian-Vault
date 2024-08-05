***
[[Asynchronous JS]]
Special values:
1. #promise - is and object that returns the value we expect to see after the function execution(we do not see this value rn, but want to do manipulations ahead)
	1. ==async operations are kind of operation that requires unknown/some time for it's execution.== 
		- When we do async operations, each time we have to wait a specific time, i.e if we not going to wait, our data can still be unresolved, but executions of the program will run despite that. Causing not-wanted behavior  
	2. sync operation are kind of operation that doesn't require "time" 
2. async/await - keywords are used to make a function return a promise and wait for it to be resolved or rejected  

To know: 
![[Pasted image 20240805175603.png]]
- Details:
1. Promise represents the eventual completion/failure of the async operation and its result value 
2. If ==promise== was fulfilled/rejected before the ==assignation== of the handler(==then==), promise won't be executed 

- Promise states:
1. ==Pending== - initial state, neither resolved nor rejected 
2. ==Fulfilled== - promise successfully ==resolved==, fulfilled state can contain ==value== which was requested  
3. ==Rejected== - asynchronous operation has failed, rejected state can contain the ==reason(error)==

- Promise handlers 
1. Handlers can react on a *settled* promise state, but not on pending  
2. Promises does ==not have== any protocols to ==terminate== the request process
3. then( ) - can store to callbacks for fulfill and reject cases, it stores these call

- Syntax: 
1. Object promise contains two ==functions as the parameter==: resolveFunc & rejectFunc.
2. Promise handlers are object methods that can process the promise state 
	1. then( )
	2. catch( )
3. 