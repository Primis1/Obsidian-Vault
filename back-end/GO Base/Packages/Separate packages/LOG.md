***
Special values:
1. #log - package is a used for simpler logging
2. log functions:
	1. log.Fatal() - besides message, exist the program via `os.Exit(1)`
	2. log.Println()

To know:
1. It is tiny package, designed to efficiently log/inform something, without messing up with multithreading 
```go 
import "log"

func() {
	if myVar, err = something(), err != nil {
		log.Printf(err)
	}
}()
```