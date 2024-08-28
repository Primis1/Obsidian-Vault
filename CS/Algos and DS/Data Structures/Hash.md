***
[[Data Structures]]
#### Special values:
- ==Hashing==:
1. #hash-table - is assorted ==ABSTRACT== data structure that consist from key-value pairs    

2. #hash-function - used for identifying index where value should be stored. Its main purpose is to transfer any ==TYPE/LENGHT==, key into the index-*number* of the bind array, which later can be used to find our ==value==
	
	1. collision - term used for hash-table occurs when #hash-function gives the same value for different input (no- #deterministic cases)

#### To know:
1. How it works/Basics:
	1. To add data into the hash table we have to specify our key, and value that is attached 
		1. Key - after we define key we want to store, key goes through #hash-function
			1. From ==hash==-==function== we receives #hash,  after in ==translating function== we get ==free-index== of array where the ==value== is going to be stored
		2. Value - stored in the ==regular array==, that was created ==during initialization== of the hash table
	2. ==And again==: We store value somewhere in the arrays' memory, and hash-function maps the *==key==* to socket-index, value is going to be stored (Hash function should be #deterministic) 

	- ==So when we add a key-value pair, we take the key, pass it to the hash function, then take the resulting number, use it as an index, and store the value at that index. And when we want to get a value for a given key, we do the same, except we return the value at the end, not storing any. You got the idea.==

![[Pasted image 20240804004701.png]]
2. Details:
	1. To avoid collision, instead of storing values into the array socket, we contain the linked list in place of each socket. This methods calls ==chaining==
		1. ==Go== does not use a linked list for chaining, but regular array 
	2. Since all key and values in the hash-table can be any type(though any key is eventually compiled into the byte-number), for types we have to use #generic file
	3. We do need #hash-function to:
		1. convert something that is not a number into the *number* that can be applied as an index value of array 
		2. ==convert==-==function== is used to determine the free space in the arrays, and convert hash into idex
![[Pasted image 20240804013549.png]]
3. Implementation && Algorithms:

```go
//How it can look:
hash("name") = 3
hash("age") = 5
hash("gender") = 6

// The underlying array would be like
["", "", "", "Marwan", "", 30, "Male", ...]
```