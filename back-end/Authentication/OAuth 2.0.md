***
[OAuth Docs](https://datatracker.ietf.org/doc/html/rfc6749#section-1.1)
### Special values:
1. #OAuth - protocol for third party's access authentication  
2. #callback  URL - is a URL in an application, where AuthO redirects the user after it is authenticated. This URL must be added into `Allowed Callbacks URL` in configuration on authO site 

### To know:

#### Concepts:

##### Roles:
- `Resource owner` - an entity of granting access to a resource. If resource owner is a person, it called end-user 

- `Resource server` - server which host protected resource. Capable of accepting and responding to protected resource request using access token.

- `Client` - an application which make requests to the server, on behalf of the resource owner and with its authorisation. "client" does not imply particular implementation.

- `Authorization server` -  the server issuing access token to the client after successfully 


##### Protocol Flow: 
```ruby
     +--------+                               +---------------+
     |        |--(A)- Authorization Request ->|   Resource    |
     |        |                               |     Owner     |
     |        |<-(B)-- Authorization Grant ---|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(C)-- Authorization Grant -->| Authorization |
     | Client |                               |     Server    |
     |        |<-(D)----- Access Token -------|               |
     |        |                               +---------------+
     |        |    + Optional Refresh Token
     |        |                               +---------------+
     |        |--(E)----- Access Token ------>|    Resource   |
     |        |                               |     Server    |
     |        |<-(F)--- Protected Resource ---|               |
     +--------+                               +---------------+
```

- ##### (A) - `client` requests authorization from the resource owner.
	- The authorization request can be made  directly to the resource owner. Or **indirect** via authorization server as an intermediary 
- ##### (B) - client receives an authorization grant.
	- **Grant - credential representing resource owner's** authorization. 
	- Four grant types, or custom one. 
	- Grant depends on a method used in by the client to request authorization and grants which are available on a server


- ##### (C) - client request on `access token` by authenticating with the `authorization  server` and presenting the authorization grant 
- ##### (D) - auth server authenticates and validates client and his grant 
	- If valid - sends `access token`


- ##### (E) -  client requests the protected resource from the `resource server` 
	- authenticates by presenting an access token received earlier 
- ##### (F) - `resource server` validate the access token, if good, serve request 

#### Access Token:
```ruby
  +--------+                                           +---------------+
  |        |--(A)------- Authorization Grant --------->|               |
  |        |                                           |               |
  |        |<-(B)----------- Access Token -------------|               |
  |        |               & Refresh Token             |               |
  |        |                                           |               |
  |        |                            +----------+   |               |
  |        |--(C)---- Access Token ---->|          |   |               |
  |        |                            |          |   |               |
  |        |<-(D)- Protected Resource --| Resource |   | Authorization |
  | Client |                            |  Server  |   |     Server    |
  |        |--(E)---- Access Token ---->|          |   |               |
  |        |                            |          |   |               |
  |        |<-(F)- Invalid Token Error -|          |   |               |
  |        |                            +----------+   |               |
  |        |                                           |               |
  |        |--(G)----------- Refresh Token ----------->|               |
  |        |                                           |               |
  |        |<-(H)----------- Access Token -------------|               |
  +--------+           & Optional Refresh Token        +---------------+

               Figure 2: Refreshing an Expired Access Token
```


- ##### (A) - client requests an access token by authenticating in authorization server and presenting `grant`
- ##### (B) - client receives an authorization grant and validates it
	- If valid, gives `access toke` + `refresh token`


- ##### (C) - client makes a protected resource request to the resource server by presenting the access token

- ##### (D) - `resource server` validate the access token, if good, serve request 

- ##### (E) - steps (C) and (B) repeats until `access token` expires.  

- ##### (F) - when it access token is invalid, resource server returns an invalid token error


- ##### (G) - the client request a new **`access token`** by repeating step (B)
	- For this time, it presents `refresh token`
- ##### (H) - The Auth Server authenticates a client and validates refresh token
	- If valid, servers new `access token` and optionally `refresh token`  