***
[[Objects]]
p174
Special values:
==Serialization== -  is the process of translation from one data type to another
JSON - JavaScript Object Notation 
JSON.stringify( ) - creating strings from objects
JSON.parse( ) - creating objects from strings

To know:
1. Examples:
```ts
let о = {х:  у: {z: [false, null, ""]}};  // Определение тестового
// объекта
let s = JSON. stringify (о); s == ' {"х": 1, "у":{"z": [false,null,, , , f ]}}1
let p = JSON.parse(s);   p == {x: 1, y: {z: [false, null, ""])}
```
