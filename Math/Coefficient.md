***
[[Math]]
### Special value:
1. #coefficient - the number of multiplications of the variable `variable` 
	- *basically the `x` sign between the variable and the number* 
2. #GCD - greater common divisor/factor. Means the greatest common number two number can be divided onto `12 and 18 GCD = 6`. Sometimes referred as GCF or HCF  
3. #LCM - least common multiple. `4 and 5 LCM = 20` 

***

#### Decimals && Binary
1. $decimal/2 = next-value$ 
	- if there is a reminder we put 1

### To know: 

1. Examples #coefficient:
$$5x^2y - \frac{4}{3}z + 7$$
```ruby 
x = 3
y = 5
z = 5

(5 * 9)*5 - (4 * 7 / 7) + 7 = 241 
```

2. #GCD steps 
	1. $a/b$ , where ==a = greater number form pair==, ==b lower number from pair==
	2. $a=b*q+r$, where `q`  is the times $a/b$ equal to,  `r` is the remainder 
	```go
	   48÷18=2(quotient)
	   48=18×2+12(remainder)
	```
	1. $a/b$ , second iteration where `a` equal `b` from previous step, `b` equal the reminder 
	2. $a=b*q+r$, repeat the process 
	```go
	  18÷12=1(quotient)
	  18=12×1+6(remainder)
	```
	1. $a/b$ , second iteration where `a` equal `b` from previous step, `b` equal the reminder 
	2. $a=b*q+r$, repeat the process 
```go 
	  12÷6 
	  12=6×2+0 
```
- Basically we do repeat the process until the reminder is 0, the reminder before it is our #GCD 

### Code
```go
func gcd(a,b int) int {
    for b != 0 {
        r := a % b 
        a = b
        b = r
    }
    return a
}
```
