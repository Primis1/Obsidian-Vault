***
Special values:
1. #pure-function - is the function that doesn't have any side effects and is determined 
	1. #side-effects - actions that is going on in the function, that does change a non-local state
	2. #deterministic  - giving the same input function will always give the same amount, what means that the output of the function is determined by its input 

To Know:
1. #side-effects actions in the function could count as a side-effect:
	1. It change non-local(ihni is it a #globalState or not)
	2. it console.log's something 
	3. Triggering any external process