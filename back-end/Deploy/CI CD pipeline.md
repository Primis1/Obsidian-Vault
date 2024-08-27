*** 
[[Deployment]]
Special values:
1. #CI/CD - Continuous Integration, Continuous Deployment
2. CI/CD components:
	1. Jobs - task or set of tasks used for build, test and deployment 
	2. Pipelines - entire CI/CD workflow as code  

To know:
1. Key requirements:
	1. ==VCS== - place(repo) where all the code is stored
	
	2. ==Build server== - tool that automates launches the tests, build process, deployment(==Jenkins==)
		1. ==Testing== - automated unit, integration and other test run automatically 
		2. ==Deployment== - scripts to automatize the deployment  
		3. ==Monitoring== && ==Logging== - shows bugs, error and health of the pipeline 
	
	3. ==Artifact==-==Repo== - storage for containing artifacts, such as binaries, docker images, etc