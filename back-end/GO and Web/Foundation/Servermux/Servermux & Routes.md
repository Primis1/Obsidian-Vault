***
[[Routes && Routers]]
Special values: 
1. Servermux - aka router, it provide light weight(it does ==not== support ==method-based== routing that used in REST, but we somehow use that ) routing
	1. subtree route - ends wit "/"
	2. fixed route - end with an empty space 

-  Go servermux is based on #net/http, which is part of stnd.lib
- #servermux - are kind of handlers which instead of providing the response itself, passes the request right to the second handler 
To know:
1. subtree by default work like "==catch-all=="
	- To remove this behavior we can modify it in route handlers, we should do that because we can ==not modify servermux== 
```go
func home(w http.ResponseWriter, r *http.Request) {
    if r.URL.Path == "/" {
        http.NotFound(w, r)
        return 
    }
    w.Write([]byte("Hello my server"))
}

func main() {
	mux := http.NewServerMux
//activating/establishing the connection 
	http.ListerAndServe(":4000", home)
}
```
- Now router is going to show home page, ==only and only when it is "/home"==

2. Additional information:
	- ==Longer priority== -  In GO servermux the ==prioritize== the ==LONGER== pattern, that mean if we declared multiple patterns, GO will apply handlers in order of their length 

	- ==Dirt to Clean redirect== - if user *used* multiple / or . in the path, he will be automatically receive 301 and will be permanently redirected to the clean route  `/foo/bar/..//baz` => `/foo/baz`
	
	- ==Fixed => Subtree redirect== - if user went to ==/foo== but we registered it as subtree, he will be automatically redirected to right one 

	- ==Status codes== -  `.WriteHeader( ) ` used for writing HTTP status code, if we didn't settled the code we want, net/http will send nothing but ==200 OK== 
		- `w.WriteHeader()` ==is possible to write once per response== 