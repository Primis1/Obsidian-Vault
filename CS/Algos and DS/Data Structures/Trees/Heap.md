***
[[Binary Search Tree]]
### Special values:
1. Heap - is based on a #binary-tree *like* data structure, that satisfies tree concept. The value of each ==node== is ==greater== or ==equal== to its ==children==. We should fill the heap from left to right
	1. min #heap - Root node contains the ==minimum== value  
	2. max #heap - Root node contains the ==maximum== value

2. Tree properties:
	1. *Complete binary tree*
	2. The value of EACH node must be ==no larger/less== than child node

- *Tree operations should always satisfies tree properties*
### To know:
#### Heap operations
1. Insert - ==adds== new elements to the heap 
2. Extract Min/Max - removes the ==minimum== or ==maximum== and returns it 
3. Heapify - convert a arbitrary list of elements into the heap 
4. Heap `arguments` heapifing:
	1. `array` - sequence of values for heapifing 
	2. `heap-size` - length of the heap(during ==heap-sorts== useful, because by decreasing the array we narrowing the sorting)
	3. index
#### Heap usage:
1. Priority #queue. Elements are retrieved by its importance/priority/value 
2. Heapsort. Sorting algorithm sorts an array in Min/Max order 
3. Graphs Algorithms. 

#### Formulas 
1. For accessing left side node $$left(i)=2*i$$
2. For accessing right side node $$right(i)=2*i+1$$
3. For accessing the parent node $$parent(i)=int(i/2)$$
4. For accessing the ==leaves== of the tree(==those nodes who don't have any children==), `n` is equal to amount of elements in the heap $$leaves = A[int(n/2)+1]  \to  A[n]$$
5. Find min/max numbers of elements in a heap, when we now its `height`: $$min  = height + 1$$ $$max = 2^{height+1}-1$$
- According to formulas, we can try to access the "arrays" which represents the values of binary tree
```go
right := 2 * i + 1 
slice := []int{21, 16, 15, 14, 9, 12, 13}
right(3) //=> 15 
```
### Implementation In Go:
1. We can convert the list of items into the heap by implementing the ==heap-interface== 
2. container/heap library 
```go

```