***
[[Communication]]
Special values:
1. #localStorage - is a browser special memory that could store for 10mb of data 
2. #sessionStorage -  is a browser special memory that could store for 5mb of data
3. #cookies - cookie could contain only 4kb of data, it exist on a client and server, cookie can store data but it's main purpose is communication between client and server

To know:
1. #sessionStorage 
	1. Never send to the server 
	2. Expires on tub close 

2. #localStorage
	1. Never send to the server
	2. It never expires, unless we or user cleared it 

3. #cookies - ==are the way for server to communicate with a client==
	1. Cookies help maintain user sessions, allowing websites to remember user data, preferences, and login status across multiple pages or visits.
	2. We can ==set== ==the== ==expiration== time for cookies, but if we didn't it will ==expire== with the end of the ==session== 
	3. There are different types of cookies:
		1. 
 
![[Pasted image 20240623170414.png]]