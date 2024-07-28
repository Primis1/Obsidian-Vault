***
Special values: 
1. Number - in go it has multiple kinds, like full, positive or negative, and narrowed one for specific amount memory, like 8, 16, 32, 64 bytes 
	1. uint - positive value 
	2. int - positive and negative value
	3. float - floating number after the dot 

2. Bytes classification 
	1. 8 = 255
	2. 16 = 65535
	3. 32 = a lot
	4. 64 = very a lot 

To know:
1. All those types were created not really for amount narrowing, but to program a software with better performance for different architectures
\
*Integers overflow and architecture structure is a huge topic of computer science, and i have to cover it in the separate note.*

2. If the number of integers is overflowing the type, which was given, it will cause the number to start from the beginning
```go 
package main 

import "fmt"

func main() {
	var maxUint uint8 = 255

	fmt.PrintIn(maxUint + 5)
}

result => 4 
```
*0 is also a starting value*

