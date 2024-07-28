***
[[Types & Variables]]
Special values:
1. #generic - type, allows to manage multiple types, passing the "static" type system without actually breaking it 

To know:
1. We should declare a generic variable, ==before the argument==, and after that use where ==needed==
	1. `func Print[T string]`
2. We can set a ==union== of generic types   
3. "any" can be one of generic types
```go 
func Print[T int | any](items []T) []T {
	for _, item := range items {
		fmt.Println(item)
	}
}
```