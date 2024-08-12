***
Special values:
1. #goroutine - function in go that enables multithreading or more like concurrency 
	- #goroutine is golang adaptation of `coroutines`, they are allow to pause and resume the flow within the thread 
- ==work sharing / work stealing== - go uses dual model for task managing within multiple goroutines 
To know:
1. Go's gorotine are NOT system threads nor processes, they are ==*light-weight*== threads   that are managed by ==GO== ==runtime== and ==queue== within it 
2. #goroutine have their own memory #call-stack (run time environment). Each gorotine starts from the small amount of memory and growth it during execution if needed 
	1. It is not uncommon to have hundreds, thousands or even million gorotine running at the same time 
3. Goroutines are created by code and then managed by ==GO run-time scheduler== 


Implementation:

```go
fo func someFunc() {

}
```