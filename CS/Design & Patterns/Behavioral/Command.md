***
### Special values:
1. #command - behavioral pattern which turns a request into a single gateway/object, which contains all information about request
	- Allows to pass a request as method `argument`, delay an execution, supports `undoable operations `

### To know:

#### Concepts:

- Problem - when we have a lot of instances which do similar logic. Regular `Button -> SubmitBtn -> CancelBtn -> SoOn`. We create a sub-class for each of those buttons, what messes up the code base 

- Solution: 
	- create a common interface for the logic
	- make object send pass an `object` as a trigger command for the common logic
	- Instead of creating separate, not-reusable object, we can create various logic interfaces 

*the elements related to the same operations will be linked to the same commands, preventing any code duplication*
![[Pasted image 20241103224545.png]]
##### Structure:
1. `Invoker` - class which creates a request to an interface. Class has a field to store a reference to a command object. **IT TRIGGERS THE COMMAND BUT NOT INVOKES DIRECTLY**
2. `Command` - interface that declares just a single method for executing the command 
3. `Concrete Command` - guider for received request which then sends it to the place where logic can be executed 
4. `Client` - creates/configures command objects. Then pass all parameters into the command constructor. 

##### Applicability:
1. Use when i want to parametrize objects with operations

![[Pasted image 20241103225036.png]]