Special values: 
1. #ok - coma ok syntax is used for error handling. If we destruct two values from the function. ==first== is going to `value/index`, ==second== `bool` or `err`

To know:
1. errors in go returns as a last value of the function, if its value is 0, mean there is no errors. So basically if error != nil, the error exist
2. for second case, convention is `ok` keyword 
```go
// not a zero value, but something else
if write, err := net.Write("blala"); err != nil {
	log.Fatal("Error occured %v", err)
} 
```

```go
if write, ok := os.Write([]byte(arg)); !ok {
	log.Fatal("writing was not OKAY")
}
```