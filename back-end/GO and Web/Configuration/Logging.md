***
[[GO WEB]]
#### Special values:
- ==env setup==
1. `os.Getenv("MYENVVARIABLE")` - returns the string of assigned env variable 
	- `go env -w MYENVVARIABLE=/somwhere/else/bin`  - create a environment variable 
2. `go run main.go -addr=$MYENVVARIABLE` - another way to set up env variable 

- ==leveled logging== 
1. Logging streams, we generally use terminal, but we also can send our logging flow anywhere we wish: file, logging server, other application
	1. `stdout` - standard out, regular output of program execution, usually terminal
	2. `stderr` - standard err, the same thing but for errors 
#### To know:

##### Concepts:
1. There are two kinds of `logging`:
	1. *information message* - first level
	2. *error message* - second level
2. To force logs show the path to the file with error, we can use `log.Llongfile`
```go
	infoErr := log.New(os.Stderr, "ERROR\t", log.Ldate|log.Ltime|log.Llongfile)
```
##### Implementation:
1. `flags`
```go 
	addr := flag.String("addr", ":4000", "address of server")

	flag.Parse()

    err := http.ListenAndServe(*addr, mux)
```
2. leveled logging 

```go
	infoLog := log.New(os.Stdout, "INFO\t", log.Ldate|log.Ltime)
	infoErr := log.New(os.Stderr, "ERROR\t", log.Ldate|log.Ltime|log.Lshortfile)
```