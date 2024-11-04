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


```go
func QuickSort(arr []int) []int {
	if arr == nil {
		// TODO can be replaced for logging.Error
		// TODO after singleton refactor
		panic("\nArray in QUICKSORT is empty!\n")
	}

	return quickSortLauncher(arr, 0, len(arr)-1)
}

func quickSortLauncher(arr []int, low, high int) []int {
	if low < high {
		arr, p := partition(arr, low, high)
		// NOTE we simply divide into smaller
		// NOTE segments on left and right side
		quickSortLauncher(arr, low, p-1)
		quickSortLauncher(arr, p+1, high)
	}
	return arr
}

func partition(arr []int, low, high int) ([]int, int) {

	// NOTE  take the last number in the array
	pivot := arr[high]
	// NOTE  prepare value for next pivot, it is
	// NOTE  gonna be the last index before
	// NOTE  we found a bigger has occurred
	i := low

	for j := low; j < high; j++ {
		if arr[j] < pivot {
			// NOTE we also switch digits in case
			// NOTE when j is a faster pointer
			// NOTE so it keeps skipping the values which are bigger than
			// Note last index, but rotate the one who are smaller,
			// NOTE because it remembers the position of last "bigger" value which is
			// NOTE last element
			arr[j], arr[i] = arr[i], arr[j]
			i++
		}
	}

	arr[i], arr[high] = arr[high], arr[i]
	return arr, i
}

```