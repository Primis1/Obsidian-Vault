***
Special values:
1. #net - package provides a portable interface for network #I/O (input/output), [[TCP & IP]], UPD and UNIX domain sockets. In general it provides access to low-level network primitives
	1. ==It allows to write TCP server==

3. #net functions:
	1. net.==Listen== - listen for connection on a port, 
		1. ==first== argument should be the type of network we're using: =="tcp", "tcp4", "tcp6", "unix" or "unixpacket"==
		2. ==second==, should an address, if we out unspecified host, .Listen( ) will listen on all unicast address  
		3. Port can be automatically selected by the .Listen( ) because of [bind](https://dev.to/hgsgtk/how-go-handles-network-and-system-calls-when-tcp-server-1nbd)documentation 
			![[Pasted image 20240729024014.png]]
	
	2. net.Dial - connect to a server at an IP address and port 
	3. net.TCPConn - *bidirectional* TCP connection 
		1. bidirectional means the move of data in two ways between two points, be sent and re-sent like on the highway 
	4. net.Conn - *==bidirectional==* network connection interface

To know:
1. ==All TCP is sends data in bytes, so our logic for receiving data should be implemented in *bytes*== 
2. net.Listen( ) functions:
	1. Accept( ) - 
	2. Close( ) -
3. How the process works:
	1. ==Listen to upcoming connections== 
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
	2. ==Accept connections== 
		```go
	for {
		conn, err := l.Accept()
		if err != {
			panic(err)
		}
	}
		```
	3. ==Handle accepted connections in a thread/gorotine== 
		1. We use net.Listen( ).Accept( ).Read/Write( ) functions, they are used for processing accepted/incomed requests
	```go
	go func(conn net.Conn) {
		buffer := make([]byte, 1024)
		// we accesing the accepted data from the connection 
		len, err := conn.Read(buffer)
		if err != nil {
			log.Print("Error on reading connection: %v", err)	
			return
		}

		fmt.Print("Message received: %s", string(buffer[:len]))
		//we write something back to the client 
		conn.Write([]byte("Message received"))
		//cloing the handling function or gorotine?
		conn.Close()
	}(conn) //=> pass our 
	```

Implementation: 
