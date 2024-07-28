***
Special values:
1. #RPC - remote procedure call, 
2. OSI - *framework* that explains the work of computer connections, its power is in independent work of each layer of connection, it is an alternative for #TCP & #IP model
3. ==Layers== of network connection:
	1. L7 - Application layer, interacts directly with the user, operates with such communication ==protocols== ==like== #HTTP, FTP, etc 
	
	2. L6 - Presentation layer, responsible for ==translating== data into application ==readable== format for L7, like wrk with ASCII and other strings formats 
	
	3. L5 - Session layer,  provides access to ==open==, ==maintain== and ==close== the session between end-user application 
	
	4. L4 - ==Transportation layer==, ==incapsulates== the data from the L5, and provides the mechanisms for ==decapsulating== the data on the L3, basically for *transporting*, this layer can use ==TCP==
	
	5. L3 - ==Network layer==, responsible for packet forwarding and so on, this layer can use ==IP==
	
	6. L2 - Data Link layer, used for transferring data between node of *PHYSICAL ROUTERS*, intercepts with technician stuff, uses protocols like ==IEEE==
	
	7. L1 - Physical layer, unlike the previous layer, this brutally physical, operates over hardware of the real devices 

To know:
1. OSI used only as a reference model
2. Services of each layer:
	1. L7 - __
	
	2. L6 - ==Data conversion==, character code translation (==remember encoding==), encrypting and decrypting  
	
	3. L5 - #Authentication and #Authorization, #sessions restoration, Reliability 
	
	4. L4 - ==Flow== control, Port multiplexing 
		1. ==multiplexing== - combination of two or more signals into one. When multiple data streams share single channel 
	
	5. L3 - *functions*, *Connection* model, *Host* address, *Message* forwarding 
	
	6. L2 - Encapsualation, Frame SYN
	
	7. L1 - __
