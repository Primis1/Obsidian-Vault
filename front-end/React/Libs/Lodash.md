***
Special values:
1. Lodash - is a not a common NPM library, but stack of utility JS functions. It uses for exetuction of simple tasks

To know:
1. Used functions:
	1. compact([ ]) - used to remove all "false" values from the array, and returns a *new* one. 
```ts
const originalArray = [1, null, 0, '', undefined, 42, NaN];

const compactedArray = compact(originalArray); => [1, 42]
```
Best Practices:
1. All not used functions could/should be removed to lighter the bundle