***
[[back-end/Communications/Http and Comm/Http & Https|Http & Https]]
Special values:
1. Http Body - is last, optional with some type of request, part of HTTP message

To know:
1. The ==type== of ==content== send to client/server is defined in ==Content-Type== header
2. Body of HTTP message used to CONTAIN the data we are sending
	1. It can be anything we want, from XML to data from the form 

3. During the initial load, server sends the HTML pages in the body of request 
*Response Message*
```
HTTP/1.1 200 OK

Date: Sun, 10 Oct 2010 23:26:07 GMT
Server: Apache/2.2.8 (Ubuntu) mod_ssl/2.2.8 OpenSSL/0.9.8g
Last-Modified: Sun, 26 Sep 2010 22:04:35 GMT
ETag: "45b6-834-49130cc1182c0"
Accept-Ranges: bytes
Content-Length: 12
Connection: close
Content-Type: text/html

Hello world! <- this guy is a body 
```
