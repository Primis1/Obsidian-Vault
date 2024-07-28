***
Special values:
1. type - key initialing the type, just like in TS
2. struct - keyword allows to create an "object" like datatype 
	1. tags - it is a small piece of metadata attached, in structs we can use tags for encoding purpose
4. methods - it uses (), where we can define an argument over which the *function* will iterate

To know: 
1. Structs:
```go
type User struct {
	ID int 
	Name string `json:"name"`
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