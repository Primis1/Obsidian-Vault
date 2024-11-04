***
[[GO advanced]]
### Special values:
1. #mutex - mechanism which ensures that one #goroutine two goroutines access to same data in simultaneously 
	1. #mutex - is one kind of #lock defense mechanism, which manages the access to the resource within concurrent programming  
### To know:

#### Concepts:
1. #mutex are used to prevent `race-condition` between #goroutine 
	1. `race-condition` - process when two threads are trying to access and modify the same data in the memory 
2. #mutex restricts access to resource for multiple threads/goroutines

#### Implementation:
```go
func (u *User) deposit(wg *sync.WaitGroup, mx *sync.Mutex) {
	fmt.Printf("%s is depositing  USD %f \n", u.name, u.depositAmount)

	// NOTE it is that simple
	mx.Lock()

	BALANCE += u.depositAmount
	defer mx.Unlock()
	wg.Done()
}

// NOTE when we pass WaitGroup as an argument we ensure that each method
// NOTE waits for the other to complete executing using wg.Done()
func (u *User) withdraw(wg *sync.WaitGroup, mx *sync.Mutex) {
	fmt.Printf("%s is depositing  USD %f \n", u.name, u.withdrawAmount)

	mx.Lock()
	BALANCE -= u.withdrawAmount
	defer mx.Unlock()

	wg.Done()
}

func Bank() {
	// NOTE by initializing, main thread will for
	// NOTE all goroutines to finish their executions
	var wg sync.WaitGroup
	var mx sync.Mutex

	users := []User{
		{name: "Marco Lazerri", withdrawAmount: 1300, depositAmount: 1000},
		{name: "Paige Wilunda", withdrawAmount: 1400, depositAmount: 123},
		{name: "Gerry Riveres", withdrawAmount: 900, depositAmount: 25},
		{name: "Sean Bold", withdrawAmount: 200, depositAmount: 5432},
		{name: "Mike Wegner", withdrawAmount: 5600, depositAmount: 2344},
	}

	// each iteration sleeps for a second
	rand.Seed(time.Now().UnixNano())

	for i := range users {
		wg.Add(2)
		i = rand.Intn(len(users))
		go users[i].deposit(&wg, &mx)
		go users[i].withdraw(&wg, &mx)

		time.Sleep(time.Second)
	}

	// NOTE we run our program with go run -race main.go
	wg.Wait()

	fmt.Printf("New account BALANCE is %f \n", BALANCE)
}
```
- We lock and unlock critical section of program so *no two goroutines can access the data in the same time*

- ##### Mutex in structs - we should store mutexes close to the data they restrict. It make possible for mutex to control the access to ==fields== in the `struct`
```go
var BALANCE float32 = 12000

type User struct {
	depositAmount float32
	sync.Mutex
}

var Balance float32 = 12000

func (u *User) deposit(wg *sync.WaitGroup) {
	// NOTE it counts like a good and simple pattern, which organize our mutexes 
	u.Lock()
	
	Balance += u.depositAmount
	defer u.Unlock()
	
	wg.Done()
}

```