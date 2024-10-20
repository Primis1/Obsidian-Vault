***
[[Types & Variables]]
### Special values:
1. type - key initialing the type
2. struct - keyword allows to create an "hash" like datatype 
	1. tags - it is a small piece of metadata attached, in structs we can use tags for encoding purpose
	2. anonymous structs- initialized inline within the variable 
3. methods - it uses ( ), where we can define an argument over which the *function* will iterate

### To know: 
1. Structs:
	1. tags has no effect on a data in the structure, but some libraries can read them and apply changes based on a provided tag  
```go
type User struct {
	ID int 
	Name string `json:"name"`
}

user := struct {
	ID int 
	Name string `json:"name"`
	} {
	ID:   32,
	Name: "Olaf"
}

func main() {
	u := User{
		Name: "Olaf"
	}

	u.ID = 1
}
```
2. Methods 
	1. Methods acts like any other function, with few exceptions bounded to types. Pretty much upside down in compare to regular function 
	2. Also it is kinda syntax sugar
```go 
func (u User) String() string {
	return fmt.Println(u.Name)
}

func main() {
	s := User {
		Name: "Polya"
	}
	s.String() 
}
```