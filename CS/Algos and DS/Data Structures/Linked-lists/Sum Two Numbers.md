***
[[Computer Science]]
To know:
1. Moving the pointer here and there 

Implementation:
```go
func SumTWo(l1, l2 *LinkedList[int]) *LinkedList[int] {
	dummy := &Node[int]{}
	curr := dummy
	
	n1, n2 := l1.Head, l2.Head
	
	carry := 0
	for n1 != nil || n2 != nil || carry != 0 {
		x := 0
		y := 0
		x = n1.Data
		y = n2.Data

		sum := carry + x + y
		carry = sum / 10
		
		curr.Next = &Node[int]{Data: sum % 10}
		
		curr = curr.Next
		
		n1 = n1.Next
		n2 = n2.Next
	}
	
	return &LinkedList[int]{Head: dummy.Next}
}

```