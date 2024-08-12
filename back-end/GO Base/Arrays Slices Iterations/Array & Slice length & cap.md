***
Special values:
1. len( ) - shows the number that collection *actually* has 
2. con( ) - shows the number that collection *may* contain
3. #copy - build in function that allows to copy a slice, take 2 arguments, place TO where copy is contained, and the copy object

To know 
1. These are built in functions, we don't to import something to make it work
2. We can also create a subset(slice from JS) from the slice
```go
    var names = []string{"a", "b", "c", "d", "e"}

	names[1: 3] //=> b c
	names[ : 3] //=> a, b, c
```
3. Changes to the subset affect the original slice
4. When we make a subset of an array, we basically converting it into the slice:
```go
    names := [5]string{"a", "b", "c", "d", "e"}

	names[:] // it is a slice, lal
```