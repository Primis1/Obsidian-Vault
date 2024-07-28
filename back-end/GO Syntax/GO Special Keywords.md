***
#keyword
Special values:
1. defer - allow to delay the function call, until the return of surrounded functions are executed
2. iota - is a mathematical keyword, used for enumerations, when assigning multiple constants in the same time
3. string( ) - object, contain bunch of string methods 
4. int( ) - can convert number into pure integer 

To know:
1. iota:
```ts
const (
	west = iota + 1 //=> 1  
	east,   //=> 2
	north,  //=> 3
	south   //=> 4
)

const someString = string.ToUpper("sodhfsuiodfisdg")
```
2. With multiple defer keywords, we have LIFO system
	1. defer: 
```go 
func main() {
	defer fmt.Pringln("good bye")
	fmt.Pringln("Hello")
}
```