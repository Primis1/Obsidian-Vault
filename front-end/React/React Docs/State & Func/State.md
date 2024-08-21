Special values:
1. #state - object's specific memory/data, or value that has a lifecycle and can be modified through the whole app
2. #globalState - is data that is similar to #state but doesn't depends on the changes from the interface and component's lifecycle. So every component could have access to that "global state" 

To know:

1. I already know a lot about useState, but this is just for summarizing:
	1. The first value represents only the current state
	2. The second value is a state setter 
 
 2. State is usually used for automatisation of components look 
 3. To update the UI, component should be re-rendered, to mount a render state should be updated.

state