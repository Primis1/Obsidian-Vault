***
### Special values:
1. Multi-stage builds - process of separating images into leaner one
	- First build can contain unnecessary dependencies, but second could contain the actual project 
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