*** 
Special values:
1. URL:
	1.  useRouter - could be use to manipulate the URL. Get current, push to one, etc
	2.  redirect( ) - imports from next/navigation, used for redirection to the specific url

To know:
1. URL redirection, although we can't track the user's location in SC
```ts
const route = useRouter()
route.push('/')

//  SSR
redirect('/')
```