***
[[GO WEB]]
Special values:
1. ==executables== - in most compiled programming languages are the output points for the program, usually executable file is a binary, aka .exe 
2. folders:
	1. /==cmd== - ==main== ==folder== the entire projects, should contain all ==executables== 
	
	2. /==internal== - private applications and libraries, code from that place should not be imported into other libraires or packages
	
	3. /==pkg== - library code that's safe to use in other applications 
	
	4. /==vendor== - dependencies of the project, can be created manually or automatically. *DON'T COMMIT DEPENDECIES IF BUILDING A LIBRARY*
	
	5. Work flow directories, such as /api, /web, /build, etc

To know:
1. In go we should build our executable, by `go build <file_name>`, if we didn't mention the file, Go compiler will look into ==main== ==package== in the current directory 
	1. An entry point in the go-program is ==main-function== in the ==main==-==package==

2. folders:
	1. /cmd:
		1. Should consist from entry points of the project 
		2. Should ==not== has much code in it 
		3. if the code withing cmd folder, can be imported from somewhere else. DO that
	2. /internal: 
		1. Files ==could== ==not== be imported, because of ==Go compiler itself==  
		2. ==Unsafe== to import, because it was NOT designed to be highly reusable and flexible 
		3. Code in internal file can ==separated== into other sub-folders, i.e. `internal/config`
	3. /pkg:
		1. Code can be used in different applications
		2. Used for grouping/organizing the project files. Commonly has only an organization purpose 
	4. /vendor:
		1. Used for storing the project dependencies 
		2. Could be managed automatically by the dependency manager, or terminal command 

3. Work Flow Folders:\
	1. /api - used for ?
	2. /web - specific components of web applications
	3. /configs - project configuration or default configs, env's, etc
	4. /build - Continuous Integrations(CI), packaging, cloud (AMI), docker containers 
	5. /deployment - 
	6. /test - 