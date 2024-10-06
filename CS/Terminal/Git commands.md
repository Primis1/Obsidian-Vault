***
### Special values:
1. git commands:
	1. init - the once used command, that creates a repository
	2. status - checks the status of changes
	3. add - add the file to the repo
	4. commit "name" - commits the change with the message 
	5. < command > HEAD - the HEAD is the current/last commit
	6. switch - switch to the branch 
	7. pull - pull the updates from the global branch to remote/local
2. tags:
	1. -c - creates a branch 
	2. -r - removes 
	3. -f - force something 
### To know:
1. Merge conflict - when git does not understand what changes to keep and what changes to delete on branch merge 

2. `DONT FKN MOVE FOLDERS HERE AND THERE `

#### Implementation:
- ##### Create a work tree over:
```sh
git worktree add ../<name-of-new-directory> <name of initial branch>
```
- ##### Reset last done commit:
```sh
git reset --soft HEAD
```
- ##### Force pull to overwrite existing files in branch:
```sh
git fetch --all

// optional backup
git branch backup-branch 
//

git reset --hard origin/main 
```
- ##### Remove remote and local branches:
```sh
git push -d origin or master/<branch_name> // remote one

git branch -d <branch_name> // local
```
- ##### Remove file/folder after `.gitignore`:
```sh
git rm --cached <file_name> 

git rm --cached -m <folder_name>
```