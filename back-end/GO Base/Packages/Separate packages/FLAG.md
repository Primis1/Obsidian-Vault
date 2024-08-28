***
#### Special values:
1. #flag - used for customizing the behavior of the program via terminal. 
	- *We do add `suffixes` to `go or executable` terminal commands, to specify the program execution *
2. `functions`: 
	-  Initialize the flag 
	1. `.String(name, defaultValue, usage)`
	2. `.Int(name, defaultValue, usage)`
	3. `.Bool(name, defaultValue, usage)`
	
	4. `.Parse()` - parse the flag into terminal  
#### To know:
1. Usage:
```go
func main() {
	// Define flags
	name := flag.String("name", "World", "a name to say hello to")
	age := flag.Int("age", 0, "your age")
	debug := flag.Bool("debug", false, "enable debug mode")

	// Parse the flags
	flag.Parse()

	// Use the flag values
	fmt.Printf("Hello, %s!\n", *name)
	if *age > 0 {
		fmt.Printf("You are %d years old.\n", *age)
	}
	if *debug {
		fmt.Println("Debug mode is enabled.")
	}
}
```