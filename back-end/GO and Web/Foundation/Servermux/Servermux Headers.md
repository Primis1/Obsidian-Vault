***
[[Servermux & Routes]]
Special values:
2. #net/http function:
	1. `ResponseWriter( )` - used for write any interaction that bind to some request back to the client
	2. ==`ResponseWriter( ).Write([]byte("Hello"))`== - write a response in ==bytes==
	3. ==`ResponseWriter( ).WriteHeader(401)`== - set the response code on the next request 
	    - Usually we do ==NOT== write these functions directly, instead we invoke it under the hood in other utilities 
	4. `ResponseWriter( ).Header().Set("Allow", "POST")` - set what kind of HTTP method we can use on a route, for the incoming request in the headers 
	5. `http.Error(w, "Error description", 401)` - shortcut for errors. Under the hood invokes `Write()` and `WriteHeaders()`
3. #net/http constants(==basically constants==):
	1. `http.Method<Method>` 
4. #net/http header methods:
	1. `http.Header.Set( )` - add new header to response 
	2. `Add( )` - used to add additional headers, can be used multiple times 
	3. `Del("Cache-Control")` - used for deleting all values from the header 
	4. `Get.Values` - used for retrieving first or slice of values, set on header. Returns string or [ ]string

To know:
Implementation:
```go
func snippet(w http.ResponseWriter, r *http.Request) {
    if r.Method != http.MethodPost {
        w.Header().Set("Allow", http.MethodPost)
        http.Error(w, "Error description", http.StatusMethodNotAllowed)
        return 
    }
    w.Header().Set("Cache-Control", "public, max-age=31536000")
    w.Header().Add("Cache-Control", "public")
    w.Header().Del("Cache-Control")
    w.Header().Get("Cache-Control")
    w.Header().Values("Cache-Control")
    
    w.Write([]byte("Create snippet"))
}
```