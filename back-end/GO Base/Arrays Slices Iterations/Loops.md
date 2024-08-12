***
Special values:
 1. range - special keyword, we have to add it to make a for/of loop instead of regular one 
 2. while - we can make a while loop, or just add a ternary operator with condition and break keyword 

To know: 
 1. for loop without any parameters will be infinite
 2. continue - skips the loop when it reaches the condition.
 3. break - stops the loop immediately
 4. ==Returning== values with different data 
	1. Array/Slice - index is an int, value is a *value* 
	2. Maps - index in this point is a ==key-value== of the map  
	3. Strings - value in range loop is ==rune int==
	4. Channels - first is channel ==element== second is ==none== 

```go
func main(nums) {
	map := make(map[int]int)

	for _, v := range nums {
		map[v]++ 
		if (map[v] == 1){
		return v
		}		
	}
}
```