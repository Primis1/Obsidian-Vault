***
Special values:
 1. #package is a collection of go files, a name of the package should declared at the top of each .go files
 2. Importing - it is possible to import third party packages, packs from native library, and our hand-made
 1. #aliases - the go imports allow us to do aliases for every package

To know:
 1. Package naming is just like variable naming, but should be created within one word 

 2. We are creating an ==ACTUAL== packages, just like the custom one, that we import(like fmt) 
	1. Before using a third party package, we should add it into dependency, by ==go get== command 
 
 4. Name of the folder and name of the package are same
	 1. #aliases could help to resolve naming collision 
	```go
package main 

Import (
	db “database/sql”
	“sql”
)

func main() {
	var _ db.DB
	var _ sql.SQL	 
}
```

Best Practices:
1. Divide and conquer: single responsibility for every package and its module 