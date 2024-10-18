***
[[JS object]]
### Special values:
1. #destructuring - taking returned properties/methods from an object, syntax sugar \
	1. we usually destruct return values from functions

### To know:

#### Concepts:
1. #destructuring is implemented by two methods of ECMA
	1. `ArrayAssignmentPattern` is at ==least== 3 times slower than `ObjectAssignmentPattern`, they produce different amount of bytecode, so it is logical 
```ts 
function arrayAssignmentPattern() {
	const [first, second] = [1, 2]
	return first, second
}

function objectAssignmentPattern() {
	const {0: first, 1: second} = [1, 2]
	return first, second`
}
```