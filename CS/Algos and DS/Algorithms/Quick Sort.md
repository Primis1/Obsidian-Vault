***
### Special values:
1. #quick-sort - sorting algorithm, principle of `Divide and Conquer`. Quicksort, sorts the arrays around the pivot element, recursively puts elements to the right or left sides of from the ==pivot== 

### To know:

#### Concepts:
-  #quick-sort provides $Θ(n^2)$ TC in worst case, but its average speed is  $Θ(n * log^n)$, what is usually a desired time

##### Steps in Quicksort:
- Divide: 
	1. Select a pivot element (usually last element of passed-sub-array)
	2. Re-arrange the elements, so the pivot element is in the middle of array, so values are less/bigger than pivot goes to left, or right
- Conquer: 
	1. Recursively apply above steps  

- Base case:
	1. Size of sub-array == 0, array == `sorted`

##### Partitioning 
1. function which re-orders the elements in the array, around the pivot, and after returns a current pivot 
2. we send pointer for the array, it re-orders it, but returns only current location of pivot 
