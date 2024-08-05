***
[[Syntax Chapter]]
Page 44
To know: 
1. **Js has auto ";" because of the interpreter, which put a ";" automatically by specific rules.**

Examples of those operators before which ";" is preferred:
```ts
// in variable list:
a = 2; b = 3

// before operators which starts at (, [
let x = true; 

or

; [2, 3, 5].forEach
```

Exceptions after which there is always ";": 

```ts
return ";"

() => ";"

count++ ";"
```

