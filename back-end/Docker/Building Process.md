***
### Special values:
1. Multi-stage builds - process of separating images into leaner one
	- First build can contain unnecessary dependencies, but second could contain the actual project 
2. Volumes and alternative for `build-mounts`, because they exist within the docker container, what makes them more isolated and managed by docker itself, they are preferred way to store data inside of container
3. Volumes, as a directory, does exist on a host machine, so they won't be deleted when container is killed, but can be accessed by docker just like a regular directory 

### To know:

#### Concepts:

- Create a `Dockerfile`, inside of which we gonna paste:
```go
# syntax=docker/dockerfile:1
```
- We inherit from base image, which has go's precompiled libraries 
- We create default directory. All commands going to start from that path 
```go 
WORKDIR /app
```
- Firstly we should install module's necessary to compile it. We do inherited from base image of GO, but we don't have our code there
	- So we copy our `go.mod & go.sum` files into image's folder we created previously 
```go
COPY go.mod go.sum ./ //=> first argument is thing we copy, second is destination
```
- We copied files into image directory. Now we run it by:
	- *it runs like in terminal*
```go
RUN go mod download
```
- We copy all source code:
```go
COPY *.go ./
```
- To compile it we use `RUN`, compiles taken `main.go` file
	- `CGO_ENABLED=0` - means that go binary will not be compatible with C
	- `GOOS=linux` - settles that go binary will be compiler like it is in `linux` 
```go
RUN CGO_ENABLED=0 GOOS=linux go build -o /docker-gs-ping 
```
- We use `CMD` to assign docker commands to when image starts a container 
```go
CMD ["/docker-gs-ping"]
```

#### Multistage build 
```ruby
# syntax=docker/dockerfile:1 

FROM golang:1.23.1 AS build-stage

WORKDIR /app

COPY /cmd/go.mod /cmd/go.sum ./

RUN go mod donwload 

COPY /cmd/*.go ./

RUN CGO_ENABLED=0 GOOS=linux go build -o /docker

FROM build-stage AS test-stage # we take our builded image, as default 

RUN go test -v ./.. 

FROM grc.io/distroless/base-debian11 AS final-stage 

WORKDIR /

COPY --from=build-stage /doc-image /doc-image

USER nonroot:nonroot

ENTRYPOINT ["/docker"]
```

***

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
