[[Design Patterns]]
***
### Special values:
1. #singleton - structural design pattern, used for creating a single gateway(`instance`),

### To know:

#### Concepts:
- ##### In GO, we create singleton instance when struct is first initialized 
	1. We define `getInstance` 
	2. Once created, we will receive the same instance each time when `getInstance`  is called 
	3. ``singleInstance`` struct is created within the `lock`

- ##### ==#singleton== is implemented wrong when several goroutines receive different instance of class  

- ##### Use cases:
	1. When we want to work with **reference** to some class
		1. DB object 
		2. **Logger** object 
	2. To restrict number of gateways to an object 
	3. To facilitate the work with that instance, by abstracting access to the actual object 

```go 
func GetInstance() *single {
	if singleInstance == nil {
		lock.Lock()

		defer lock.Unlock()

		// NOTE check for existence of
		// NOTE singleton instance
		if singleInstance == nil {
			fmt.Print("\nLogger created NOW!\n")
			singleInstance = &single{}
		} else {
			fmt.Print("\nInstance is already created\n")
		}
	} else {
		fmt.Print("\nInstance is already created\n")
	}

	return singleInstance
}
```

