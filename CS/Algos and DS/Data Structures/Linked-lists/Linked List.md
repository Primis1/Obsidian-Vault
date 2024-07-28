***
[[Computer Science]]
Special values:
1. Linked list - is a linear data structure that consists from nodes, each node has a pointer memory location of next node 
	1. [[Arrays && Linked lists]]

To know: Implementation
1. Head - is a pointer that points at the first node, entry point to the list 
2. Node:
	1. Data 
	2. Pointer to next node 
		1. If node is last, pointer will be equal null  
3. Current node represented by the ==value itself==
4. To find last node, we using a pointer to search over ==all== nodes, till we find the which doesn't has a pointer to next value, so after we can work with the last node 

Implementation:
```go 
type ListNode struct {
	data int
	next *Node
}

func (l *ListNode) EasyInsertList(data int) {
	newNode := &ListNode{data: data}
	if l == nil {
		*l = *newNode
	} else {
		for l.next != nil {
			l = l.next
		}
		l.next = newNode
	}
}
```