***
#### Special values:
1. `http.Handler` - is an interface that has a `ServerHTTP( )` *function*
```go
type Handler interface {
	ServeHTTP(ResponseWriter, *Request)
}
```
- object can be called a handler if it has `ServerHTTP( )` function, i.e satisfies Handler interface

2. `http.ListenAndServe("port", handler)` - can work with servermux because, servermux also has `http.Handler` method 

3. *All HTTP requests are handled in their own #goroutine (handled concurrently)*. Code in high-loaded servers is going to run concurrently ==within== or ==by== my `handlers`  
#### To know:
1. The simples handler, we can make. This handler takes and object, it can be anything, and implement the method ==Server( )== on it:
```go 
type Home struct {}

func (h *Home) Server(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("hello, wrld"))
}
```
- Creating a method instead of function is not really a common practice, or it is just long-winded, *so in ==GO== we can create a handler as regular function, and later use the `http.HandlerFunc()` adapter instead. It add `ServerHTTP()` method for the passed function*. 
```go
func Home(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("hello, wrld"))
}

func Something() {
    mux := http.NewServeMux()
    mux.HandleFunc("/", http.HandlerFunc(Home))
}
```