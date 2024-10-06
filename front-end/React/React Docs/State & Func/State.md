### Special values:
1. #state - object which stores dynamic "snap-shots" of data
2. #globalState - is data that is similar to #state but doesn't depends on the changes from the interface and component's lifecycle. So every component could have access to that "global state" 
3. #props - data which we can pass throughout component tree, can be a state too 
### To know:

#### Concepts:
1. State is used for  of components look 
2. To update the UI, component should be re-rendered, to mount a render state should be updated.

#### State / Props diff:
- State is often mutable and inconsistent 
- Props are static and passed between the components 