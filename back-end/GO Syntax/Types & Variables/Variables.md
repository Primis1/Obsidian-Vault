`Well that is typescript buddy)) 

Special values:
1. #var / #const - a variable in GO, just the same as let & const in JS
2. := - operator is a shorten non-typed declaration for variables  
3. _ - is a blank identifier, it says Go compiler to discard variable and assign it to blank 
To know:
1. We can use tricks with #var just like with *let*, but with necessary types
2. Compiler complains about not-used variables: 
	```go
	func main() {
		i, f, b, s := 32, true, false, "bla bla"
		fmt.PrintIn(s) //=> compile error 
	}

blak operator: 

func main() {
		_, _, _, s := 32, true, false, "bla bla"

		fmt.PrintIn(s) //=> bla lba
	}
```