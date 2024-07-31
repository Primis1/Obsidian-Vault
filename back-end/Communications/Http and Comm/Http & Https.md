***
[[Communication]]
Special values:
1. #HTTP - computer message protocol, it allows computer to send a messages between each other 
2. HTTPS - coded/secure version of HTTP 

To know:
1. To deliver HTTP messages, computer uses ==TCP==/==IP== connection
2. Required parts of http request are: 
	1. Request line:
		1. Method - GET, POST, PUT, DELETE, etc
		2. URI - path to resource request is going to sent 
		3. HTTP version 
	2. Host Header - domain name of the server and optionally host number(field required since HTTP/1.1)
	3. Blank line - \\n indicates the end of header section 
	4. Body - delivers the actual data, but not required for request to exist 
3. Custom headers:
	1. User-agent - client information (what kind of browser or OS used)
	2. Accept - type of content client can process 
	3. Cookie - 
	4. Accept-Language - preferred language of the client  
	5. Accept-Encoding -  preferred encoding 
	6. Connections - options for connecting manager 
4. Header attributes are parameters of headers

```ts
GET / HTTP/1.1
Host: www.example.com
'other headers'
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webpq=0.8 
Accept-Language: en-US,en;q=0.5 
Accept-Encoding: gzip, deflate, br 
Connection: keep-alive 
Upgrade-Insecure-Requests: 1 
Cookie: sessionId=abc123; theme=light; lastVisit=2024-07-28T12:00:00
\n blank 

```