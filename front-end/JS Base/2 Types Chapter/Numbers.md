cc.52
**Special values of section:**
**NaN** - data type is not a number or: 
1. inf / inf
2. sqrt from negative value
3. 0 / 0 
	
**Infinity** - number is over 9 007 199 254 740 992
	
**"-0"** - appears when... just not often used shit, which is almost equal to regular 0 
	
**BigInt** - huge value. Can create a BigInt by adding "n" to the number  ``1n``


**To know:**

1. NaN don't return true even if  ``NaN === NaN``, 

	The right way check the NaN type: 
	
```ts
	value !== value; // returns true if the value is NaN
```


2. -0 is equal to 0 in comparing operators
	
```ts
const y = -0; const x = 0

y === x => true
```


3. BigInt - can't be used cryptography, because it doesn't try to avoid a the time attacks 