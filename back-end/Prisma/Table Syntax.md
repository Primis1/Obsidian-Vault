Special values:
1. tables - that is how the database works, similar to excel, it has a rows and lines
2. models - are used to initialize the table
3. column, datatype, constraints - are parts of the syntax, and used for designing a table 
```ruby  
#initalazation of the table 
model Human {
	id int @id
}
```

To know: 
1. Prisma got its own parody on SQL syntax, but it is actually more concise 
2. Querying data from database(thank to the prisma) is kinda easy, we have to make a query to "schema" 