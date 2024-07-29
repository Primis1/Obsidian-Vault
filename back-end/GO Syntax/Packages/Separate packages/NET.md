***
Special values:
1. #net - package provides a portable interface for network #I/O (input/output), [[TCP & IP]], UPD and UNIX domain sockets. In general it provides access to low-level network primitives
	1. ==It allows to write TCP server==

3. #net functions:
	1. net.==Listen== - listen for connection on a port, 
		1. ==first== argument should be the type of network we're using: =="tcp", "tcp4", "tcp6", "unix" or "unixpacket"==
		2. ==second==, should an address 
	
	2. net.Dial - connect to a server at an IP address and port 
	3. net.TCPConn - *bidirectional* TCP connection 
		1. bidirectional means the move of data in two ways between two points, be sent and re-sent like on the highway 
	4. net.Conn - *==bidirectional==* network connection interface

To know:
1. ==All TCP is sends data in bytes, so our logic for receiving data should be implemented in *bytes*== 
2. How the process works:
	1. Listen to upcoming connections 
	```go
		func main() {
			addr := "localhost:8888"
			// "tcp" means that it can be "tcp4" or "tcp6"
			l, err := net.Listen("tcp", addr)
			if err != nil {
				panic(err)
			}
			defer l.Close() //=> we close the listenning 
							//   section after other functions are done 
			//we getting the data about the server we established, 
			//doesn't has any logic purpose
			host, port, err := net.SplitHostPort(l.Addr().String())
			
			if err != nil {
				panic(err)
			}
			fmt.Printf("Listening on host: %s, port: %s\n", host, port)
		} 
	```
	2. 
3. 

Implementation: 
