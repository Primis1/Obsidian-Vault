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
		- Graphical way to read data from tree 
		
		- [20, 10, 3, 15, 25, 23, 27]
		
2. **`In-Order`**:
		
	- Parent - $Left^n$ `if left == nil, read Left` -> Parent -> Right `if right == nil, read right` -> read Parent
		
	- We do read the number in it's logical order, from lowest to biggest

	- [3, 10, 15, 20, 23, 25, 27]  
	
3. **`Post-Order`**: 
		
	- Parent -> $Left^n$ `if left == nil, read Left` -> Parent -> Right `if right == nil, read Right` -> Parent -> Parent -> Right     
		
	- We do read the node only after we reach the leaf(==starting from last node==)
		
	- [3, 15, 10, 23, 27, 25, 20]
	![[Pasted image 20240919213102.png]]

- #### Insertion, deletion