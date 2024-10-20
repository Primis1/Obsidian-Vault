***
Special values:
1. Regex - is a string sorting/manipulation technology(find and replace things), built in every PL (yea baby)
2. Symbols:
	1. set_of_character ==*== - informs computer that preceding symbol repeats 0 to infinite times 
	2. set_of_character ==+== - repeat the preceding character from one to infinite 
	3. set_of_character =={...}== - repeat the preceding character as many time, as mentioned in brackets 
	4. ==^== set_of_character - match any character except 
	5. character classes:
		1. \\\\d - match any digit 
		2. \\\\D -  match any non-digit 
		3. \\\\s - match any white-space character
		4. \\\\S - match any non-white-space character 
		5. \\\\==w== - match any "word" character
		6. \\\\==W== - match any non-word character 
		7. \\\\b - match any boundary character 
		8. [set of character] - match any single set of characters, by default it is *case sensitive*. ==Can be used as scope==
			1. [first-last] - from that to this character 
	6. \\\\ scope \\ - scope for searching 
	7. ( ) - create a local scope that forces the characters act as a block
	8. # - comment 
To know:
```ts
[\\] - will match any english character 
```