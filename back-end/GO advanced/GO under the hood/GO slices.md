***
[[GO advanced]]
### Special values:
- ==*Parts of slice*==
1. Pointer - pointer to first element of the `array`, slice represents 
2. Length - amount of elements in `slice`, it can not be bigger than it's capacity 
3. Capacity - total amount of elements `slice` can contain before being extended

### To know:

#### Facts:
1. During `append()` operation, in case of `slice` overfilling, go ==creates== bigger array and transfers values from ==smaller== ==to== ==bigger== array. The ==bigger array== is generally ==x2== times bigger  
	- ==According to it, we should reduce the amount times when `new/bigger` arrays is created==

2. For ==empty== ==slice== comparison, compare its length  

#### Work with memory:
1. `Slices` does not contain any data, ==they do point into the arrays==. This means that two slices can reference to the same data
```go
slikce := []int{1, 2, 3, 4, 5}
slice[1:4] //=> 2,3,4

slice2 := slice[2:]
slice2[0] = 1 

slice //=> 1, 2, =1=, 4, 5
```