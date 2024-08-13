***
[[Multithreading in JS]]
Special values:
1. Web-worker - incapsulated functionality existing outside of application. Used to create additional thread  
2. WW functions:
	1. `.postMessage( value )` - used for post data into the worker 
	2. `.onmessage = ( callback )` - used for invoking a handler in the worker, and retrieve send data  `

To know:

Structure & implementation:
1. We communicate with WW through message-like system
	- it means that we post some data as a "message" to the handler in web worker, and after we should extract the data, which was processed in worker 
- Workers should be a JS files 
Implementation:
```ts
const a = 43;
const b = 22;
// copy the existing worker 
const worker = new Worker("worker.js");
// send some data into the worker 
worker.postMessage([a, b]);
console.log("message posted into Worker");

let result = 0;
// the data back 
worker.onmessage = (e) => {
// assign it to needed variable, object etc. 
  result = e.data;
  console.log("message received from worker");
  console.log(result);
};
```

```ts
// we declare the handler for messages received from the application 
onmessage = (e) => {
//logic of web worker 
    console.log("Data was received into the best WW");
    let result = 2;
    for (let i = 0; i < e.data.length; i++) {
      result = e.data[0] * e.data[1];
    }
    const finalResult = "Result is: " + result;
// assign the result of execution 
    postMessage(finalResult);
  };
  
```
Theory:
1. ==The quantity of web-workers is depending on the number of CPU cores== 1 core = 1 web-worker = 1 thread 

2. ==Web Workers== are used to escape the single threaded environment. Key feature of Web-workers is that, they ==don't== ==block== DOM, unlike ==async== code
	1. ==Requirements== for being a web-worker:
		1. Live in its own file - process should ==NOT== interact with user interface 
		2. Function is passed by copy 
		3. No global states nor variables, no `window` 
	
2. ==Web-Workers=: 
	1. Should not contain nor interact with:
		1. The ==parent== objects
		2. The ==window== objects 
		3. The ==document== objects 
		4. The ==DOM== 
	
	2.  ==Can have access to:==
		1. The ==local== objects
		2. The ==navigation== objects 
		3. ==XMLHttpRequests==
		4. The ==Application== ==cache== 
		5. Spawning other web-worker 
		6. Importing external script 