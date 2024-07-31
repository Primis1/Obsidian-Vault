***
[[Data Structures]]
To know:

Implementation:
```go
func mergeTwoList(list1, list2 *Node) *Node {
    dummy := &Node{}
    current := dummy

    // Traverse through the first list and attach nodes to the new list
    for list1 != nil {
        current.Next = list1
        list1 = list1.Next
        current = current.Next
    }

    // Traverse through the second list and attach nodes to the new list
    for list2 != nil {
        current.Next = list2
        list2 = list2.Next
        current = current.Next
    }

    // Return the next node of dummy (the head of the new merged list)
    return dummy.Next
}
```