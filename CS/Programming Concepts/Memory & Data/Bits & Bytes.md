***
[[Memory & Data]]
Special values:
1. bit - is a minimal value of the data that RAM can contain, one bit could 1 or 0, in one socket we can have at least 8 bits, relying on the process architecture  
2. byte - is a sets of bits that are divided by architecture, like 8 bits could be one byte
3. machine word - the biggest amount of data that processor can operate at the time, used for large numbers.   

To know:

1. Big endian - the enumeration of bytes in register from right to left
2. Little endian - the enumeration of bytes in register from ==left== to right 
3. Number data types in memory:
	1. byte - 1 byte
	2. short - 2 bytes
	3. int - 4 bytes
	4. long - 8 bytes 
4. With primitives, they coping by value, but not by the link. Meaning *that's fucking why we need pointers* [[Pointers]]: 
	```go
	byte x = 5 //=> 00000101 created a new memory 

	byte y = x //=> 00000101 created another memory socket 
```
5. Exceptions are arrays, when we assigning an array into the variable, we give an access to the same place in the memory   
6. ASCII - memory standard used where we have 8 sockets of bits, in one byte
