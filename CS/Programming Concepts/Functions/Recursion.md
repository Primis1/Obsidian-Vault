***
Special values:
1. #recursion - is a function that calla itself. This technique is ==not== used for performance, but for readability and over all shorter syntax
	1. ==base==-==case== - the case of function that doesn't use any recursions, i.e a termination case 
	2. ==recursive==-==relations/steps== - a recursive set of rules that narrows all other cases into the ==base==-==case== 
To know:
1. The way to think:
	1. We should narrow any task to the most simple parts
	2. from this simple part we should create a base case 
	3. 
2. When we implement a recursion, we basically create another ==copy== ==of== ==the== ==function== but ==NOT== calling the function itself, it allows to create a ==loop== of ==nested== ==functions==  
3. If we really want, we can ==return== a recursive ==function==, instead of hassling with typing   

4. Algorithms with recursions, swapping nodes in linked list
```go
	// Base case: if the list is empty or has only one node, return the head
	if head == nil || head.Next == nil {
		return head
	}

	// Initialize pointers
	curr := head
	next := curr.Next

	// Swap the first two nodes
	curr.Next = next.Next
	next.Next = curr

	// Recursively swap the remaining pairs and connect the list
	curr.Next = swapPairs(curr.Next)

	// Return the new head (which is 'next' after swapping the first two nodes)
	return next
}
```