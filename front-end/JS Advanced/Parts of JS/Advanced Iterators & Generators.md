***
### Special values:
1. #for/of  - used as for/range loop, it access the the values of the sequence
2. #for/in - is used for iterating over keys of objects/anything 

### To know:

#### Concepts:
1. #for/of - can be be used over everything that got repeated sequence of values. It can be: `array, map, strings, etc`
	1. It cant be iterated over objects, because of their unstructured design and lack of itself values  
- It is basically a syntax sugar over regular #for loop, it facilitates the process, and adds some readability 
#### Practice:
```ts
let obj = "hello"

for( let v of obj) {
    console.log(v);
}

h
e
l
l
o
```

```ts
let obj = "hello"

for( let v of obj) {
    console.log(v);
}

0
1
2
3
4
```