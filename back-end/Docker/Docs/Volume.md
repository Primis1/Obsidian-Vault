***
### Special values:
1. #volumes - file directory which exist within the docker container, used for storing data of the container

### To know:

#### Concepts:
1. Volumes and alternative for `build-mounts`, because they exist within the docker container, what makes them more isolated and managed by docker itself, they are preferred way to store data inside of container
2. Volumes, as a directory, does exist on a host machine, so they won't be deleted when container is killed, but can be accessed by docker just like a regular directory 

#### Implementation 

