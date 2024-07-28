***
Special values:
1. Zeros - in go lang, just like in TS there are true and false values: "", false, 0 
	1. Those zero could appear if we didn't assign the value to the variable

2. nil - zero values for interfaces, pointers and maps

To know:
1. We often see initialization of variable in ==if== statement with empty err
```go
if err := something, err != nil {
	log.Printfn("%v", err)
} 
```