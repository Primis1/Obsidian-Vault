***
[[GO WEB]]
### Special values:
#### Env setup
1. `os.Getenv("MYENVVARIABLE")` - returns the string of assigned env variable 
	- `go env -w MYENVVARIABLE=/somwhere/else/bin` - create a environment variable 
2. `go run main.go -addr=$MYENVVARIABLE` - another way to set up env variable 

#### Leveled logging 
1. Logging streams, we generally use terminal, but we also can send our logging flow anywhere we wish: file, logging server, other application
	1. `stdout` - standard out, regular output of program execution, usually terminal
	2. `stderr` - standard err, the same thing but for errors 
### To know:

#### Concepts:
-  There are two kinds of `logging`:
	1. *information message* - first level
	2. *error message* - second level

- *We should not use `log.Panic` or `log.Fatal"` outside of main function, we can return the error messages instead, thanks to `logging`*

- `log.New()` are concurrency safe. We can use single logger across several goroutines, without any `race-conditions`

#### Implementation:

1. `flags`
```ruby
	addr := flag.String("addr", ":4000", "address of server")

	flag.Parse()

    err := http.ListenAndServe(*addr, mux)
```

2. leveled logging 
```ruby
	infoLog := log.New(os.Stdout, "INFO\t", log.Ldate|log.Ltime)
	infoErr := log.New(os.Stderr, "ERROR\t", log.Ldate|log.Ltime|log.Lshortfile)

	infoLog.Printf("Starting server on %s", *addr)
	
	srv := &http.Server{
		Addr: *addr,
		ErrorLog: errorLog,
		Handler: mux,
	}

	err := srv.ListenAndServe()
	errorLog.Fatal(err)
```