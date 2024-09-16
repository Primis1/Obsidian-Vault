***
[[JS object]]
### Special values:
1. #prototype - is an object from which every `object in JS` inherits properties. It is also a wrapper therefore "*==In JS everything is an== object*" exist 

### To know:

- #### Concepts:
1. `EVERY OBJECT IN JS HAS [[Prototype]]` attribute which contains a reference to its `prototype`. It means that every created/initialized `object` contains properties of `[[Prototype]]`

2. Every prototype in JS is an object by itself, so the ==prototype will have its own prototypes==, producing the prototype chain 

3. *In TS we can not use `__proto__` directly via its stricter type checker, we also wont inherit `object` `properties` automatically*
	- `TS` encourage to use typed methods like `Object`, `String`, `Array`.

4. In `TS` `objects/prototypes` are implemented via interfaces, these interfaces can be `merged` with our own, hence, prototypes can be extend by new `methods`. 
	1. *SO WE CAN EXTENDS FUNCTIONALITY OF BUILD IN TS OBJECTS*
#### Practice:
```ts
interface String {
  prefix(reo: string): string;
}

const a = (String.prototype.prefix = function (pre: string) {
  console.log("something");
  return pre + this;
});

"string".prefix("new property")
```