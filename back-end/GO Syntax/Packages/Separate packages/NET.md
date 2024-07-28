***
Special values:
1. #net - package provides a portable interface for network #I/O (input/output), [[TCP & IP]], UPD and UNIX domain sockets. In general it provides access to low-level network primitives
	1. ==It allows to write TCP server==

3. #net functions:
	1. net.Listen - listen for connection on a port 
	2. net.Dial - connect to a server at an IP address and port 
	3. net.TCPConn - *bidirectional* TCP connection 
		1. bidirectional means the move of data in two ways between two points, be sent and re-sent like on the highway 
	4. net.Conn - *==bidirectional==* network connection interface

To know:
1. ==All TCP is sends data in bytes, so our logic for receiving data should be implemented in *bytes*== 
2. How the process works:
	1. We should establish a TCP connection [[Flow of TCP]]
3. 

Implementation: 
1. We initialize the variables for net.Listen() 
	```go
const (
	HOST = "localhost"
	PORT = "8888"
	TYPE = "tcp"
)

listen, err := net.Listen(TYPE, HOST+":"+PORT)

if err != nil {

}
```
2. network must be tcp, tcp4, tcp6, Unix,
3. net.Close() 
