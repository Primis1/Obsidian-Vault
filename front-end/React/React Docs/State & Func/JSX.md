***
Special value:
1. JSX - is JS-syntax-extension, used for easier VDOM manipulation using JS 
2. React.craeteElement() - used for creating react/html elements.

To know:

1. Under the hood JSX use method `React.craeteElement()`
	1. That is abstraction over the plain JS HTML creation 

2. React.craeteElement() has three arguments:
	1. type - html element we want to create. Defined from `keyof` from the arrays of HTML elements 
	2. props - tag attributes, `className`, `href`, etc 
	3. children - something that is going to stored within the created tag