***
Special values:
	1. #redux - is a complex library and also an architectural style with its own environment tool, like RTK

To know: 
1. Redux is used for:
	1. ==Avoiding prompt drilling,== 
	![[Pasted image 20240605193242.png]]
	2. Creating a #globalState that will =="erase" my state from react==, that will allow each component immediately access it, from every part of the application
	
2. Redux Concepts:
	1. Redux ==store== is an object with methods(==from the JS perspective==) that is sort of container or wrapper for state, it also manipulates the wrapped state
		1. Reducer - is a #pure-function which is also #deterministic  that SETS the ways of how we can manipulate the *stored* #globalState in the ==store==. 
			1. To compare with regular react, setState function is a reducer too, but useState allows us to change and manipulate the state as ever we want to, but in Redux=>Store=>Reducer we set a rules of how we can manipulate the state
		2. ==Reducer - is a pure function that accepts an old that with some "action" and returns a new state==
		
	2. Actions - to allow the Reducer understand that some state needs update, component send an action. Action is a JS object 
		1. Dispatch - method is used to deliver the action to the store 
		
	3. After State was updated in the store by reducer. Component can read a ==new==-==state== by two methods:
		1. getState - is used to *get* a new state from the store 
		2. subscribe - is used to track the time when the data in the store was changed 
		
	4. ==So how it all works==:
		1. component creates an ==Action== 
		2. It uses a ==Dispatch== method to deliver ==Action== to the ==Store==
		3. In the ==Store== we have our ==Reducer== that describes in what way the ==new-state== should be changed according to ==old-state== and ==action== that was receive from the component
		4. ==Store== updates its state
		5. Components check its new values, and take this state to them 

![[ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26.gif]]

Details & Syntax:
1. From recent version, company recommends to create a ==Store== by using RTK
2. We should describe the structure of state and actions in the store:
	1. We use typescript "type" to that 
3.  When we first time call a reducer, we don't have an ==old-state==, so firstly reducer should have an initial value 
```ts
store.ts

type State = {
  count: number;
};

export type Inc = {
  type: "increment";
};

export type Dec = {
  type: "decrement";
};

const initState: State = {
  count: 0,
};
//type for action 
type Action = Inc | Dec;
//initial state added to that
const reducer = (state = initState, action: Action): State => {
  switch (action.type) {
    case "increment":
      return {
      //use of immutability to store the "old state"
        ...state,
        count: state.count + 1,
      };
    case "decrement":
      return {
        ...state,
        count: state.count - 1,
      };
    default:
      return state;
  }
};

export const store = configureStore({
  reducer: reducer,
});

```