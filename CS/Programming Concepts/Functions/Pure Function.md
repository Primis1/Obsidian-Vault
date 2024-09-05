***
### Special values:
1. #pure-function - is the function that doesn't have any side effects and is determined 
	1. #side-effects - actions that is going in the function, that does change a non-local state(interacts with outer environment)
	2. #deterministic  - giving the same input function will always give the same amount, what means that the output of the function is determined by its input 

### To Know:
1. #side-effects actions in the function could count as a side-effect:
	1. It change non-local
	2. it `console.log`'s something 
	3. `Triggering any external proces`s
