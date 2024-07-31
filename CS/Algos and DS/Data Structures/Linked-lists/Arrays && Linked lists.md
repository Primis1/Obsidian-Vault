***
[[Data Structures]]
Special values:

1. Array - is a collection of values. It is good for: static amount of “something”, if i want to jump from element to another. Arrays could only contain values of single type 
    
2. Linked-List -  is an element structure, linked between each other by orders of the next element. Is good for: dynamically changeable arrays, if i want to take data one after one.
    
3. Hybrid structure - array of lists


To know:

1. Arrays
    1. In case of decomposition, arrays are huge bricks in the memory that can change its size. So after it growth computer should look for another free block of memory that can contain the new-sized array. 

	2. Because of that, adding new elements into array could be slow

	3. Booking the memory

	4. Access to any element of the arrays is immediate

  
1. List
	1. Each element of the list contains the number of its next element, so they can be placed wherever we want in the memory.

	2. It is easy to add new elements to the list, however it is harder to read them and take them from the memory. Because to get element 3, we should take the address of element 2, from element 1, and from element 0.

  
3. Hybrid structure:
    1. Array of linked lists:
	    1. 
