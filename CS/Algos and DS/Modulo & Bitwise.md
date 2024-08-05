***
Special values:
1. % - make a division of left operant over right operant, ==returns the remainder of from the dividing== 
2. ^ - bitwise operator 
3. << / >> - ==left-shift==, ==right-shift==. They used for shifting the bits of left operand on the number of right operand. ==Whether right left or right== 

To know:
1. Modulo:
	1. If ==x== can't be divided by *divider*, it returns ==x== 
	2. Can ==determine== does the number ==consists== from the ==divider== 
	3. Can ==determine== does the number is ==even== or ==odd==
	4. Every ==N==th operation, for something. Send a promo for discount, every 50 logins 
```js
1 % 5 = 1// 1 cannot be divided by 5, so the remainder is 1
4 % 5 = 4// 4 cannot be divided by 5, so the remainder is 4
7 % 5 = 2// 7 divided by 5 equals 1, with a remainder of 2
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

3. Shift:
	1. Can be used for more performance multiplication/division. Because of right bit access 
		1. Basically all it does is ==a * 2^b== or ==a / 2^b==
	2. Cases when shift returns undefined:
		1. b - ==bigger than the number we shifting== 
		2. a - should ==not== be a negative number 
		3. 
```go 
func main() {
	// of left shift  operator
    // a = 5(00000101), b = 9(00001001)
    a, b := 5, 9

	fmt.Printf("left shift %d, %v", (a  << 1), b << 1)
}

```