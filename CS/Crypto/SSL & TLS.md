***
### Special values:
1. #SSL - Secure Sockets Layer encryption on SQL server
	1. Deprecated; #TLS (Transport Layer Security) used instead (Postgres) 

### To know:

#### Concepts:

- With `SSL` (which uses `TLS` protocol), server will listen for both SSL and normal connections on the same #TCP port 

##### Connection to HTTPS
- User Enters a site 
- Browser's look up for #TSL Certificate
- "Handshake", validation of certificates
	- If certificate is not valid - throw an `error`
- Once verified, secure **link** is created between `server` and `browser`
	- Operation is done on **Transport Layer**

*Certificate - installable file on a server, which contains:*
	*- Public && Private keys*