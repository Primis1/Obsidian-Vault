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
	
	2. **Initialization** - #SHA-256 uses `8` 32-bit initials hash values (`H0`, `H7`) derived from the fractional parts of the square roots of the first `8` ==prime numbers==
	
	3. **Message Schedule** - the padded message is divided into 512-bit blocks, each split into `16` 32-bit words. A message scheduler is created for each block, which extends these 16 words to 64 words, using #bitwise operations
	
	4. **Compression** - for each 512-bit block, the algorithm iterates 64 times, updating hash values with a series of logical and #bitwise  operations (rotation, shifting, modular addition). They use constant derived from the cube roots of the first 64 prime numbers 
	
	5. **Final** - returned values of `H0`, `H7` are concatenated to produce 256-bit hash



```go
package main

import (
	"encoding/binary"
	"fmt"
)

// Constants as defined in the SHA-256 standard
var k = []uint32{
	0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
	0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
	0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
	// Additional constants would be added here
}

// Initial hash values as specified in SHA-256
var h0 = []uint32{
	0x6a09e667,
	0xbb67ae85,
	0x3c6ef372,
	0xa54ff53a,
	0x510e527f,
	0x9b05688c,
	0x1f83d9ab,
	0x5be0cd19,
}

// rotateRight performs a right rotation on a 32-bit integer
func rotateRight(x, n uint32) uint32 {
	return (x >> n) | (x << (32 - n))
}

// sha256Transform processes a 512-bit chunk of data
func sha256Transform(h []uint32, chunk []byte) {
	var w [64]uint32

	// Initialize the first 16 words in the array w
	for i := 0; i < 16; i++ {
		w[i] = binary.BigEndian.Uint32(chunk[i*4 : (i+1)*4])
	}

	// Extend the first 16 words into the remaining 48 words
	for i := 16; i < 64; i++ {
		s0 := rotateRight(w[i-15], 7) ^ rotateRight(w[i-15], 18) ^ (w[i-15] >> 3)
		s1 := rotateRight(w[i-2], 17) ^ rotateRight(w[i-2], 19) ^ (w[i-2] >> 10)
		w[i] = w[i-16] + s0 + w[i-7] + s1
	}

	// Initialize hash value for this chunk
	a, b, c, d, e, f, g, h := h[0], h[1], h[2], h[3], h[4], h[5], h[6], h[7]

	// Main loop
	for i := 0; i < 64; i++ {
		s1 := rotateRight(e, 6) ^ rotateRight(e, 11) ^ rotateRight(e, 25)
		ch := (e & f) ^ (^e & g)
		temp1 := h + s1 + ch + k[i] + w[i]
		s0 := rotateRight(a, 2) ^ rotateRight(a, 13) ^ rotateRight(a, 22)
		maj := (a & b) ^ (a & c) ^ (b & c)
		temp2 := s0 + maj

		h, g, f, e, d, c, b, a = g, f, e, d+temp1, c, b, a, temp1+temp2
	}

	// Add this chunk's hash to the result so far
	h[0] += a
	h[1] += b
	h[2] += c
	h[3] += d
	h[4] += e
	h[5] += f
	h[6] += g
	h[7] += h
}

// padMessage pads the message to fit the SHA-256 block size requirements
func padMessage(message []byte) []byte {
	length := uint64(len(message) * 8)
	message = append(message, 0x80)

	for len(message)%64 != 56 {
		message = append(message, 0)
	}

	lenBytes := make([]byte, 8)
	binary.BigEndian.PutUint64(lenBytes, length)
	return append(message, lenBytes...)
}

// ComputeHash calculates the SHA-256 hash of the input data without shared state
func ComputeHash(data string) string {
	hash := make([]uint32, len(h0))
	copy(hash, h0)

	paddedMessage := padMessage([]byte(data))

	for i := 0; i < len(paddedMessage); i += 64 {
		sha256Transform(hash, paddedMessage[i:i+64])
	}

	result := ""
	for _, val := range hash {
		result += fmt.Sprintf("%08x", val)
	}
	return result
}

func main() {
	// Example usage with concurrency
	data := []string{"hello", "world", "concurrency", "SHA-256"}

	results := make(chan string, len(data))

	for _, d := range data {
		go func(input string) {
			results <- ComputeHash(input)
		}(d)
	}

	// Collect results
	for i := 0; i < len(data); i++ {
		fmt.Println(<-results)
	}
}

```