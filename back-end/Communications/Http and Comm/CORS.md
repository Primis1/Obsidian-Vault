***
[[Http & Https]]
#### Special values:
1. CORS - *Cross Origin Resource Sharing*, mechanism allows the website request resources from other domain, that is different from its own 

#### To know:

##### How it works:
1. When website ready to create cross-domain-request, browser automatically add header: `"Origin: website-domain"`, after the server to which request was made, checks the header and choose: ==*let it go* or *don't let it go*==
2. If `server` allowed the `connection`, it responses with `CORS` headers that describe what we `can` and `can not do`
```ts
"Access-Control-Allow-Methods"
"Access-Control-Allow-Headers"
"Access-Control-Allow-Origin"
```

##### Purpose:
1. Allow to control who can access the resources of my website 
2. Prevents the possible attack on the website, such as `CSRF`(Cross Site Request Forgery(==підробки==))

##### Drawbacks:
1. Headers of CORS can be accidently useless against the attacker, through rich amount of fields in `"Access-Control-Allow-Origin"`