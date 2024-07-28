Special values: 
1. #err - usually the convention for naming the second variable, can be used as a boolean 

To know:
1. errors in go returns as a last value of the function, if its value is 0, mean there is no errors. So basically if error != nil, the error exist 
```go
// not a zero value, but something else
if write, err := net.Write("blala"); err != nil {
	log.Fatal("Error occured %v", err)
} 
```
