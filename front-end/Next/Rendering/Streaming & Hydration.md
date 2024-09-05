***
### Special values:
1. Streaming - painting the components of page, by chunks and   
2. Hydration - adding interactivity to the page, ==via JS handlers== 

### To know:
1. Streaming:
	1. Streaming on *server-side*, allow to send HTML in chunks that the browser can progressively render as it is received
	
	2. Because of streaming we ==can quickly get "first" painting== of the page

2. Hydration:
	1. Client side JS convert the *static* HTML page, into the *dynamic web-page*, by attaching the event handlers to HTML components 

	2. It allow quick initial load, because of pre-rendered `html page` 
	
	- *==Blank or static web-page is rendered on a server==, and delivered to the client, where the `hydration`  process begins* 
