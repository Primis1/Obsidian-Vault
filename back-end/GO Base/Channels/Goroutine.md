***
Special values:
[[Channels in GO]]
1. #goroutine - function in go that enables multithreading, concurrency. When go-runtime encounter the goroutine, it does not wait for it be executed, and continues to read the file 
	- Scheduler opens a goroutine pool across available system-processes or CPU-cores, enabling goroutine run in ==parallelism== 
	- Similar to JS promises, it firstly "skips" the execution of goroutine
	- #goroutine is golang adaptation of `coroutines`, they are allow to pause and resume the flow within the thread 
- ==work sharing / work stealing== - go uses dual model for task managing within multiple goroutines 

2. *Generally, devs ==should not care much about inner process== of garbage collector or scheduler, because
	1. ==a)== GO team change it quiet often; 
	2. ==b)== GO does ==NOT== provide much utilities to adjust go-runtime*  

To know:
1. Go's goroutines are NOT system threads nor processes, they are ==*light-weight*== threads that are managed by ==GO== ==runtime== and ==queue's== within it 

2. #goroutine have their own memory #call-stack (run time environment). Each gorotine starts from the small amount of memory and growth it during execution if needed 
	1. It is not uncommon to have hundreds, thousands or even million gorotine running at the same time 

3. Goroutines are created by code and then managed by ==GO run-time scheduler== 

4. ==Work Sharing==: 
	1. Go scheduler tries to distribute the work to the available process, what makes more sense for multiple CPU or CPU's cores 
```RUBY
CPU1:  A B C D E
CPU2:  F G 
CPU3:  H I
// after work sharing 
CPU1:  A B C
CPU2:  D E F  
CPU3:  G H I
```
5. Work Stealing: 
	1. It "steals" the task from overwhelming #goroutine, and creates a new less weighted thread

Implementation:
1. goroutine can be assigned to ==ANY== function 
	- The below code will print ==nothing== because Go scheduler didn't got a chance to ==execute the function before program is exited  
```go
func main() {
	go fmt.Printf("hello wld)
}
```
2. `select` is similar to switch case
```go
func operator(line1, line2 chan string, quit chan struct{}) {
	for {
		select {
		case msg := <- line1:
			fmt.Printf("Listen on line 1: %s\n ", msg)

		case msg := <- line2:
			fmt.Printf("Listen on line 2: %s\n ", msg)
			
		case msg := <- quit:
			fmt.Printf("Listen on line 1: %s\n ", msg)
		}
	}
}
```