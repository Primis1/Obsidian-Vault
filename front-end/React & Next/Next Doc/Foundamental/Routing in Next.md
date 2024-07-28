Special values:
_ - before the name of the route makes it inaccessible or erase 
( ) - folders withing the brackets, counts as "organization" folder, which won't affect the actual URL
[ ] - dynamic route, mean that something that we don't know yet should be as a part of the route
[. . .auth ] - it calls "catch all-routes" [example]([javascript - Nextjs dynamic page routes: What is the purpose of using the spread operator [...example] or [[...example]] in a page variable? - Stack Overflow](https://stackoverflow.com/questions/67087932/nextjs-dynamic-page-routes-what-is-the-purpose-of-using-the-spread-operator))
API folder - this should contain all backend logic, everything there is a server side by default, and could be access through URL

To know:
1. I can use ( ) to add a .layout without affection the URL