***
### Special values:
1. #docker-file - blueprint where we set all needed instructions
	- `directives` similar to comments things, we declare them at the top of `Dockerfile`, and only there 
### To know:

#### Concepts: 
1. Syntax is something between SQL and YAML files, where we got case sensitive `instruction` and argument to it
	- In #docker-file we specify the actual docker image, ==it is place where job is going==. 
2. We use 

#### Implementation:
```ruby 

#  syntax=docker/dockerfile:1
#  this is just a comment 

// availiable instruction:

ADD => Add local or remote files and dirs 

ARG => Use build-time variable 

CMD => Specify default commands 

COPY => Copy fs and dirs 

ENTRYPOINT => specify default executable 

ENV => Set envrionment variable 

EXPOSE => Set which ports applc is listed on 

FROM => Create new build stage from a base 

LABEL => Add metadata

MAININER => Specify the authour 

ONBUILD => Specify instruction, when image used in build

RUN => Executes the build commands 

SHELL => Set the default shell image 

STOPSIGN => Specify sys call signal for exiting container 

USER => Set user and group ID 

VOLUME => Create volume mounts 

WORKDIR => Change working directory 
```
