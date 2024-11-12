***
### Special values:
1. #binary-search-tree - parent node is the checking point, from which we do comparison
- Each `branch` of binary tree is kinda separate binary tree, to which we apply follow rules:  
	- `left side is ALWAYS SMALLER than starting node`
	- `right side is ALWAYS BIGGER than starting node`  

### To know:

#### Concepts:

- #### Traversals(`обхід`):

-  To completely traverse a tree, we have to move forward and backward through each node, and its children


1. **`Pre-Order`**: 
	- Level by level
```go 
func traverse(root *TreeNode) {
	root.Val 
	traverse(root.Left)
	traverse(root.Right)
}
```
- [20, 10, 3, 15, 25, 23, 27]
	
2. **`In-Order`**:
	- We do read the number in it's logical order, from lowest to biggest
```go
func traverse(root *TreeNode) {
	traverse(root.Left)
	root.Val 
	traverse(root.Right)
}
```
- [3, 10, 15, 20, 23, 25, 27]  
	
3. **`Post-Order`**: 
	- We do read the node only after we reach the leaf(==starting from last node==)
```go
func traverse(root *TreeNode) {
	traverse(root.Left)
	traverse(root.Right)
	root.Val 
}
```
- [3, 15, 10, 23, 27, 25, 20]
	![[Pasted image 20240919213102.png]]

#### Morrison traversal

 - We attach the roots's right tree, to the the most right node of the left node. Then we re-assign right to left and delete left(because we already store the copy of it, in most right-left node). Iterate on until left node == nil, and stop the overall circle when root == nil 
	- Morrison traversal with creation of linked list 
```go
func() {
	curr := root 
	for curr != nil {
		if curr.Left != nil {
			temp := curr.Left
			for temp.Right != nil {
				 temp = temp.Right 
			}

			temp.Right = curr.Right 
			curr.Right = curr.Left 
			curr.Left = nil  
		}

		curr = curr.Right
	}
}
```