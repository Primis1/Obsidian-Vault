***
[[Data Structures]]
To know:
1. We declare three variables:
	1. next -  is first be ==initialed==, so it can always hold the next value of curr 
	2. curr.Next - is being ==shaved== from the next value, and points into the previous one (first prev value is ==nil==)
	3. prev - is storing the curr's current value
	4. curr - being assigned back to its next node, by ==next==  	
	`//  ->    p 	 
	`//  p     c   n
	`// nil <- 1   2 -> 3 -> nil 
`

Implementation:
```go
func (ll *LinkedList[T]) ReverseLinkedList() {	
	curr := ll.Head
	var prev *Node[T]
	var next *Node[T]
	for curr != nil {
		next = curr.Next
		curr.Next = prev
		prev = curr 
		curr = next
	}
	ll.Head = prev
}
```