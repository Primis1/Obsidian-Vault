Special values: 
1. #slices - is a collection of values basically an array, but in Golang it is flexible in size
2. array - is a data structure, but it fixed in size 
3. append - function allows to add the elements to the end of slice, and slice only
4. make([]type, len/cap) - allows to set a length to slice and ==avoid nil accesses== 

To know: 
1. ==Arrays== 
	1. During the creation time, array should identify it's size, and after it ==can't be resized==, but if we declared it through var, we ==can change== the individual element
	2. Array will be garbage collected once it's no longer in use
	3. We can initialize the array, and fill later
		1. if we  leave it empty. array will fill itself with Zeros of the type it was signed 
	4. Arrays are tricky because of its fixed value, when we assigning data to the place in the array, it get ==memorized==, and changes only when we re-assign it again ==DIRECTLY==
	```go
	func main() {
    //this number of elements is a key syntax to set an array
        arr := [2]string{"Bla", "Bla1"}
        arrB := [2]string{}

        arrB = arr

        fmt.Println(arr)
        fmt.Println(arrB)

        arr[0] = "Bla3"

        fmt.Println(arr)
        fmt.Println(arrB)
    }
    
		[Bla Bla1]
		[Bla Bla1]
		[Bla3 Bla1] <=
		[Bla Bla1]
```
2. ==Slice== 
	1. They are not fixed in size, so more often used on a daily situation 
	2. append( ) methods takes a zero or more values in the slice, and returns a new slice with the appended values in the end
		1. to add another slice we can use iterator like loop, or (old-good) spread operator
		2. [ ]string's ==ARE NOT== string, so rule of ==single type== 
	4. we can also use a make( ) function, that will set an initial length to the slice, 

	```go
	func main() {
	    var names = []string{"Alan", "Oleh"}
	    var more = []string{"Alan", "Oleh"}
	
	    names = append(names, "Lora")
	    names = append(names, more...)
	
	    fmt.Println(names)

		slice := make([]string{}, 2/len, 3/cap)
	}
```

3. Common:
	1. Access is the same that in TS, via *dot*, [ ] and number of index
		```go
	func main() {
		arr := [4]string{"Bla", "Bla1", "Bla2", "Bla3"}
	
		fmt.PrintIn(arr[1]) //=> Bla2
	}
```
	2. Out of bound error - means that i tried to access the index, which does not exist 
	3. Go arrays and slices don't have any function nor methods to append or remove the values to them.
	```go
func main() {
	var names = []string{"Alan", "Oleh"}
	
}
```