***
### Special values:
1. 

### To know:

#### Concepts:



BFS (Breadth-First Search) and DFS (Depth-First Search) are two fundamental algorithms used to traverse or search through data structures like trees and graphs. They explore nodes (or vertices) in different ways, and each has distinct characteristics and use cases.
1. Breadth-First Search (BFS):

BFS explores a tree or graph level by level, starting from a root node (or an arbitrary node in a graph). It explores all neighbors (children in a tree) of the current node before moving on to the next level.
Characteristics of BFS:

    Queue-based: BFS uses a queue data structure (FIFO - First In First Out) to keep track of the nodes that need to be visited.
    Level-order traversal: In trees, it visits nodes level by level, making it useful for problems that require checking nodes in the same level or the shortest path in unweighted graphs.

BFS Process:

    Start from a root node (or any node in a graph).
    Visit all immediate neighbors (children) of the root.
    Move on to the next level and visit the neighbors of the previously visited nodes.
    Continue this process until all nodes have been visited or the target node is found.

Use Cases:

    Shortest path in unweighted graphs.
    Level-order traversal of a tree.
    Checking if two nodes are cousins (nodes at the same level but with different parents).

2. Depth-First Search (DFS):

DFS explores a tree or graph as deep as possible along a branch before backtracking to explore other branches. It goes down one path to the deepest node, then moves back and explores another path.
Characteristics of DFS:

    Stack-based: DFS can be implemented using an explicit stack (LIFO - Last In First Out) or recursively using the call stack.
    Deep exploration: DFS goes deep into the tree/graph before visiting other nodes at the same level.

DFS Process:

    Start at the root node (or any node in a graph).
    Visit a child node and continue visiting deeper child nodes until you reach a leaf (or a node with no unvisited neighbors).
    Backtrack to the last unvisited node and explore other branches.
    Repeat this process until all nodes have been visited or the target node is found.

Use Cases:

    Pathfinding in mazes or puzzles.
    Cycle detection in graphs.
    Topological sorting in Directed Acyclic Graphs (DAGs).
    Preorder, Inorder, and Postorder traversals in trees.

Key Differences:

    BFS explores neighbors first (breadth), while DFS explores one branch deeply (depth) before moving to another branch.
    BFS uses a queue, whereas DFS typically uses a stack (or recursion).
    BFS is better for finding the shortest path in an unweighted graph, while DFS is better for problems like finding all paths or deep exploration.

Example (Tree):

For a binary tree:

    BFS would visit nodes level by level: root, then its children, then their children, and so on.
    DFS would visit one child of the root, then go as deep as possible into that branch, and backtrack when necessary.