***
[[Types of Rendering]]
#### Special values:
1. #SSG - static site generation. Generates pages during build time. Page is static and its data is "locked" until next new build.   
#### To know: 
1. On a server we do prepare ALL fully rendered pages, data on that pages is *static*
2. Pros:
	1. Fast page opening
	2. Good SEO
	3. Independent from user device
3. Cons
	1. Terrible scalability 
	2. No re-renders 
	![[Pasted image 20240821153834.png]]
