***
- Components:
1. Props:
	1. totalCount - should parse the total number of data object for count 
	2. currentPage - number of current page user on 
	3. pageSize - should put a max quantity of of showed object on a single page(how the fuck we should narrow )
	4. onPageChange - callback function that actually change the content on pages in paggination
	5. siblingsCount - show surrounded pages of the current one 
To know:
1. *==Well it fucked==*
2. Firstly we are creating a hook, after that a component itself, and only after we can put some data in the page component 
3. How each prop works:
```ts
const totalPageCount = Math.ceil(totalCount / pageSize) //that will show the subsetted amount of pages, by dividing a total number of components to page size that should be showed in the paggination 

```