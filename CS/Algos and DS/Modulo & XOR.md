***
Special values:
1. % - returns a reminder after division is made 
2. ^ - bitwise operator 

To know:
1. Modulo:
	1. If ==x== can't be divided by *divider*, it returns ==x== 
	2. Can ==determine== does the number ==consists== from the ==divider== 
	3. Can ==determine== does the number is ==even== or ==odd==
	4. Every ==N==th operation, for something. Send a promo for discount, every 50 logins 
```js
1 % 5 = 1// 1 cannot be divided by 5, so the remainder is 1
4 % 5 = 4// 4 cannot be divided by 5, so the remainder is 4
7 %5 = 2// 7 divided by 5 equals 1, with a remainder of 2
25 % 5 = 0// 25 divided by 5 equals 5, with a remainder of 0
218 % 5 = 3// 218 divided by 5 equals 43, with a remainder of 3

let longList = 100;
let feedbackInterval = 10; // to be used as the modulus

// loop over the list to process each item
for(let i=1; i <= longList; i++ ) {
  if( i % feedbackInterval == 0 ) {
   let percentCompleted = ( i / longList ) * 100;
    console.log(percentCompleted );
  }
}
```
2. XOR: 
	1. 