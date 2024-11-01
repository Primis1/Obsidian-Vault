***
[[Computer Science]]
### Special values:
1. #SHA-256 - hash function, which always returns 256-bit hash. 
	1. hashing algorithm used in bitcoin

### To know:

1. #SHA-256  is a part of SHA-2 hashing family designed by NASA
#### Concepts:
1. Algorithms operates over blocks of 512 bits / 64 bytes and processes them iteratively through sequence of transformations:
	1. **Padding** - message is padded to ensure it's a multiple of 512 bits. it involves appending "1" bit, followed by "0" bits, and finally appending the length of the original message (in bits) as a 64-bit value 
	
	2. **Initialisation** - #SHA-256 uses `8` 32-bit initials hash values (`H0`, `H7`) derived from the fractional parts of the square roots of the first `8` ==prime numbers==
	
	3. **Message Schedule** - the padded message is divided into 512-bit blocks, each split into `16` 32-bit words. A message scheduler is created for each block, which extends these 16 words to 64 words, using #bitwise operations
	
	4. **Compression** - for each 512-bit block, the algorithm iterates 64 times, updating hash values with a series of logical and #bitwise  operations (rotation, shifting, modular addition). They use constant derived from the cube roots of the first 64 prime numbers 
	
	5. **Final** - returned values of `H0`, `H7` are concatenated to produce 256-bit hash
