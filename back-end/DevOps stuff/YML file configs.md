***
[[DevOps]]
Special values:
1. local.yml - is a environment specification file, that used for deployment? or .env variable access  

To know:
1. Value pairs in the file:
	1. env - in what environment we're going to run. "local", "prod", "dev"
	2. storage_path - link to the db file 
	3. http_server:
		1. address - address and port of the server. "localhost:8888"
		2. timeout - time of given to read and write req/res
		3. idle_timeout - life of open connection 