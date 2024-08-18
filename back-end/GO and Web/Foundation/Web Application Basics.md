***
[[GO WEB]]
Special values:
1. Three Parts: 
	1. Handler - responsible for execution a program logic
	2. Servemux/Router -  basically describe what to do with client when he entered specific route, can use the handler
	3. Web Server - a connection server that listens to TCP/IP requests 
		1. *Unlike with other langs, go doesn't need Nginx or Apache*

To know:
 1. Go servermux treats the "/" route as "catch-all", so if we assign something to "/", this data/functionality will transferred into every child route, aka `/bar/foo/etc`
![[Pasted image 20240811031540.png]]

Implementation:
```go 
package main

import (
	"log"
	"net/http"
) 

// handler that is going to run on some route 
func home(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("Hello my server"))
}

func main() {
// declaring a servermux 
    mux := http.NewServeMux()
// assiginng the handler to the route 
    mux.HandleFunc("/", home)

    log.Print("Starting server on :4000")

    err := http.ListenAndServe(":4000", mux)
    log.Fatal(err)
}
```