***
[[Flow of JS]]
Special values
1. JS Runtime - is the whole environment that allows environment(browser or node) ==run== JS code 
	- run time goes beyond the regular code execution, runtime is the whole set of tools that 

To know:
- Parts of JS runtime:
	1. First part is JS Engine
	2. Second part of the ==runtime== is *==Web APIs==*
	3. Third part is callback queue

1. ==JS engine is described in separate note==  

2. Web APIs:
	1. Web API is additional, environment, functions that extends JS-language. It means that functions APIs for ==DOM==, ==Fetch==, ==Timers==, etc. Are ==NOT== the parts of JS-language.
	2. APIs enable JavaScript to interact with environment(in our case browser)
	3. It is functionality provided to ==JS-engine==. These API are wrapped into the objects(`window`)
3. Callbacks queue 
	1. used for asynchronous operations within the runtime
	2. it allow the ==call stack== in the engine to do manage handlers and do asynchronous work   
![[Pasted image 20240807034130.png]]