***
### Special values:
1. `passport.serializeUser` - writes data to and from sessions; 
	1. determines what data of User should be stored in session
2. `passport.deserializeUser` - retrieves data from sessions;
	1. In `deserializeUser` that key is matched with the in memory array / database or any data resource
### Concepts:

#### User ID is stored in session:
```ts
passport.serializeUser(function(user, done) {
        error
	done(null, user.id) -> indetifier of session
});
```

#### Retrieving data from session:
```typescript
				           passed in serialize
passport.deserializeUser(function(id, done) {
    User.findById(id, function(err, user) {
	    attaching object from db/storage to `req` object 
        done(err, user);
    });
});
```

#### Work flow illustration:
```ts
passport.serializeUser(function(user, done) {
    done(null, user.id);
});              │
                 │ 
                 │
                 └─────────────────┬──→ saved to session
                                   │    req.session.passport.user = {id: '..'}
                                   │
                                   ↓           
passport.deserializeUser(function(id, done) {
                   ┌───────────────┘
                   │
                   ↓ 
    User.findById(id, function(err, user) {
        done(err, user);
    });            └──────────────→ user object attaches to the request as req.user   

```