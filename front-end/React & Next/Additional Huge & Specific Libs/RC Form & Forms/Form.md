***
Special values:
1. Controlled Input - we put the value of the input into the State
2. tags of the form:
	1. input - IS A FCKN DISCOVERY, it has multiple, it has ALOT of attributes and look variations, besides for attr
	2. label - associate text with form input, textarea, checkbox or radio button
	3. textArea - allows user to write ==multirowed== paragraphs 
	4. select - mother tag for *option* tag. It creates a drop down list 
		1. ==option== - tag could be storage only withing the select(like ui/li), it should have value="" attribute
To know:
1. Components:
	1. ==Input==
		1. type="==text==" - make input from the input
		2. type="email" - validates form to email standard  
		3. type="==checkbox==" - make a selection of single or multiple topics
		4. type="==radio==" - make a selection of single topic
		5. type="button" - make a button from input
		6. type="hidden" - hides the input element 
		7. type="==range==" - creates a swiper from the input
		8. type="reset" - removes all the data from the input, its button
 
	2. ==label==
		1. it is generally semantic stuff, used as title 
	3. ==textArea==
		1. tag allows to control the size of rows in
	4. select
		1. ==name== attribute identifies the control over the selection on a server side 

2. General attributes:
	1. id - unique identifier for the element 
	2. value - string, set initial value to the input 
	3. disabled - bool, disables an element 
	4. required - bool, field must filled out before submission 
	5. placeholder - show some text on a background 
	6. readonly - bool make the field read only 
	7. autofocus - when page loads, focus the element 
	8. min/maxlenght - numbers, in {}

3. Submission
	1. We can send data from the on submission, by assigning the function to the onSubmit attribute 
	2. 