Special values: 
1. #Authentication - is the login or registration
2. #Authorization - is accessing to special parts of the application 

To know:
1. #cookies are unsafe and can't be trusted by the server 
2. #sessions are created by database

3. #Authentication consist of those process:
	1. Login and password are covering into the session
	2. Session sends it to the database
	3. If you are in database:
		1. Database send the access token to session and session sends it to the user
		2. If it isn't, welp it returns an error.
![[Screenshot 2024-04-04 154712.png]]

4. #Authorization 
	1. Request to the protected page is covering into the session 
	2. Session sends it to the database
	3. If you have rights for access:
		1. Database sends a request token by session and session sends it to the user
		2. 200 - access; 404 - denied
![[Pasted image 20240404155533.png]]
5. Every #token should have a lifetime, if it is not, so it isn't a token 