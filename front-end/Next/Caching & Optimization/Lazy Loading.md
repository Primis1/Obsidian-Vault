***
Special values:
1. Lazy loading - also knows as demand-loading(Cache-aside). CS meaning is - "don't render this shit, till needed". In nextJS lazy loading allows to defer a CC and imported libraries, and only include them in the client bundle when needed 
2. [dynamic( )](https://nextjs.org/docs/app/building-your-application/optimizing/lazy-loading) - function, applies a lazy loading for a specific component. ==It could be called in CC just like in SC==

To know:
1. There are two ways of lazy load a component, one from react and second from next/dynamic, but method from nextJS is replaces, a react one 
	1. dynamic( )  - consists of few parts:
	```ruby
/* const    dynamic-itself   import       way-to-the-comp      ?part with ssr */ 
const LazyLoading = dynamic(() => import('../../some-route/or-api'), {ssr: false}) 
```
2. We have to call and structure the function ==outside== of component exportable component 

3. After we did call and structure a component with lazy-loading, we can use it as usual 
```ruby
	const LazyLoading = dynamic(() => import('../../lazy-client/component'))
	
	return(

	//renders imediately 
		<LazyLoading />
	
	//under some condition 
		{condition && <LazyLoading />}

	)
```
4. If we do lazy-load a server component, only its children CC will be lazy loaded, but not a server component itself 

***
5. Next allows to demand-load external libraries. 
	```ts
        <input type="text" onChange={(e) => {
            const {value} = e.target.value
            const Fuse = (await import('fuse.js')).default
            const fuse = new Fuse(names)
        }} 
        />
```