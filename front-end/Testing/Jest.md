***
[[Testing]]
Special values:
1. jest - library that provides environment for test/building running within the JS environment \
	1. `mock`(насмішка) - is the object that simulates the behavior of real function 
	2. spying - practice of monitoring the behavior of the functionality. Useful to track without changing the behavior  

To know:
1.  `describe(<name>, callback)` function used for tests grouping 
2. `test` or `it` used for identifying the individual test
3. `expect` - used for matchers used.   It creates an assertion for matchers that expect 
```ts 
expect(value/object/func).toBe(expected value)
```
4. `global` - object used to adjust the behavior of REAL GLOBAL OBJECT, like mock the behavior of `fetch` function within the test file  
5. `spyOn` - method used for monitoring over methods/functions of an object
```ts
const obj ={ 
  name: (name) => `${name}`
}

const spy = jest.spyOn(obj, "name")

obj.name("Olaf")

console.log(spy.mock.calls) //=> ["Olaf"]
```
