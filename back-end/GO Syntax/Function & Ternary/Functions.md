***
Special values:
1. *anonymous function* - just like arrow function, it declares without a name and to be invoked it has to have a () on its end  
2. spread arguments - we can add ... ==before== the datatype and and use a spread operator when ==parsing== an argument into the func 
To know:
1. Props and returns:
	1. Go have multiple shortcuts for type declaration withing the arguments and returns of the function 
```go 
func main() {
	myFunc("sdfsd", "sdfsdf", 1.1)
}

myFunc := func(smString, bgString string, num float64) {
	toUpper := strings.ToUpper(bgString)
	toSmall := strings.ToLower(smString)
	toFullNum := int(num)
	
	fmt.Printf("%v\n%v\n%v\n",toUpper,toSmall,toFullNum )
}
```
2. Function could assigned to the ==variable==, and be used as regular function after that 
3. We use another function as an argument for another function
```go 
func sayHello(f func() datatype, other argument) {
	// call the function and print the result
	fmt.Printf(f())
} 
sayHello(myFunc)
```
