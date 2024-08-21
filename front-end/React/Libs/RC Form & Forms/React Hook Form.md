***
Special values:
1. RHF - library that automatize creation of new inputs, fields and so on within the form
2.  useForm() - function with methods such as:
	1. register() - used for registration of an input 
	2. handleSubmit() - function we put into onSubmit, and there we can add our real handler 
	3. formState: {loading, error} - one is a boolean second is object?
	4. reset() - function allows to remove all current values from the inputs 
	5. getValue() - get value of the input 

To know:
1. ...register: 
	1. ==name== - perhaps useState or value identifier  
	2. onChange 
	3. onBlur 

2. Validation:
	1. CS - browsers use JS, HTML, CSS to validate the form in some way 
	2. SS - server validates data after submission  
