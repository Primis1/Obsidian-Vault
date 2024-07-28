***
Special values:
1. #pointer - variable that points at location and access of other variable in the memory. In golang are used for ==building== a ==data structures==, which are relying on the ==direct== memory access and speed

2. * and & - are used initialing a pointer. * is used for ==types==, & used for ==values==

3. new( ) - used for allocation of initial value with pointing to its zero value 

To know:
1. Pointers are used for ==creating== a new variable with value AND memory ==socket== of another variable 
	1. POINTERS ARE USED FOR CREATING A POINTER TO SOMETHING(in our case memory sockets)
	2. The literal explanation is that pointer are "==pointing==" at ==exact place== of the memory, like *0x0002e0*

2. Dereferencing * and referencing & operators are used for accessing ==value== or ==memory== socket ==in pointer variable== 
	1. * used for ==types==, basically if we declaring a var with a pointer type, we creating a pointer, and after we can assign ONLY variables * or & signs
		1. Dereferencing ==nil==, will cause a ==crush== ==on== ==runtime==  
	2. & used for pointing at existing value, and for accessing the
```go
	a := 45

	var b *int = &a

	fmt.Printf("%v\n", *b) //=> 45
	fmt.Printf("%v\n", &b) //=> 0xc00005a028

	var c *int 

	fmt.Printf("%v\n", *c) //=> crush runtime
```

3. Pointers and types syntax:\
	1. We can assign the ==struct== to the pointer ==variable==, but we ==don=='t need to ==dereference== ==each value== 
	2. ==Map=='s values are pointed by default 
	3. Slice's values are pointed by default

4. ==Use cases==:
	1. ==Assign== to an ==error==. If we compare regular error's value, it is always the same. With pointer variable we can look where it is located in the memory
	
	2. Because we're working with the memory space itself, function scopes won't have an effect on the pointed value 
	
	3. Pointers are to ==directly== ==access== the value or memory sockets of wrapped variable, cause ==increase== in ==speed==
```go
var w = new(int)
var w *int
var bw = &w
```
![[Pasted image 20240711023619.png]]