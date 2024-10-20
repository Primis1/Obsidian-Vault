***
Special values:
1. #os - is a package interface for your actual OS, basically allows to code a terminal commands 

***
- File creation: 
	2. `os.OpenFile(file string, permition )` - opens/creates file with specific permission   
	3. `os.Create(fileName string)` - creates a file, or overwrites if exist, returns a pointer to the file for `I/O`
	4. `os.Stat(name string)` - receives file/directory information 
***
2. Directory manipulation
	1. `os.Mkdir()` - creates a directory 
	2. `os.GetWd()` - get the current directory 
	3. 
***
3. Terminal manipulation
	1. os.Args[ index] - string - allows to get a terminal or standard input string, by its index  

To know:
1. Package provides:
	1. #I/O file, functions
	2. File directory manipulations 
	3. Accessing environment variables  

#### Implementation: 

```go

```