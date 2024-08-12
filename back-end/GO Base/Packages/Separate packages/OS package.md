***
Special values:
1. #os - is a package interface for your actual OS, basically allows to code a terminal commands 
2. #os functions: 
***
1. #I/O
	2. os.Open(file string) - opens file for ==read== access 
	3. os.Create(fileName string) - creates a file 
	4. os.Stat(name string) - receives file/directory information 
***
2. Directory manipulation
	1. os.Mkdir() - creates a directory 
	2. os.GetWd() - get the current directory 
	3. 
***
3. Env manipulation
	1. os.Args[] .[]string - allows to make write command-line arguments==?==

To know:
1. Package provides:
	1. #I/O file, functions
	2. File directory manipulations 
	3. Accessing environment variables  