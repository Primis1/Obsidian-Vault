***
### Special values:

##### #hook - are created for "connecting" to life cycle of `react-component` from functional components 

- #useState - adds the state to the component
- #useEffect - adds the life cycle to the component with state, re-render it, give side effects like: API calls, subscriptions to something
- #useContext - state manager, facilitates data access one of `react` build it `state-managment` things 
- #useReducer - advanced version of #useContext , implemented by #reducer pattern

### To know: 
1. #useState:
	1. add state to the component, aka data and possibility to be re-rendered(`lifecycle`)

2. #useEffect: 
	1. do side effects, or external actions 
	2. scope can be invoked through triggering the dependency state

3. #useContext 
	1. Reacts' native state manager. allows to efficiently pass the state in the component tree    

4. #useRef
	1. Used for adding initial state to and prevent future renders 