***
### Special values:
1. #context 
2. #rss - Really Simple Syndication, format for work with content of html pages, basically takes the information in proper way 
 
 - packages/utils:
1. `goose` - utility for db-migrations
2. `rss` - library for #rss and #atoms parsing 

### To know:


### Implementation:
#### Stages:
1. Connecting migrations to database 
	1. Create `Article, Resource` tables 
	2. Generate #structs for these tables 
	3. 