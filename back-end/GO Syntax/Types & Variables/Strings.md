***
[[Types & Variables]]
Special values: 
1. String types:
	1. interpreted sting literals - they exist within the "", and allow to use ==escape== characters
	2. raw string literals - they exist withing the '', anything withing those quotes will be transfer into the string

To know:
1. If we want to iterate over the string, like in for/range loop, we receive a ==runes==. Keep in mind and if so decode it back into string by ==string( )== function 
	2. rune is a Unicode point 
2. Escape characters:
	1. /n - start with next line 
	2. /t - x's tab 
	3. \\\\\\ - used for double back sla