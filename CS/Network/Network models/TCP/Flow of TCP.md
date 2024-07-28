***
Special values:
1. client/server - devices that initiating a conn, and connecting to 
2. 3-way hand shake 

To know:
1. Server is a device that all time, passively awaits for the request 
2. Doesn't matter who connected to who, the pipeline is bidirectional 
3. 3-way handshake:
		1. synch
		2. synch, acknowledge
		3. acknowledge, client sends byte[0]
		4. *establishment* of bidirectional flow
	4. Details:
		1. ==Client== sent a, ==SYN==, synchronization message(should be a unique number value) to the passively waiting server that he wants to do a request 
		2. ==Server== Sends a, ==SYN-ACK==, synchronization-acknowledgement message, that consist from two parts: SYN + 1, ACK which is a numeric value too
		3. ==Client== sent its own ACK: ACK +1 
		4. ![[Pasted image 20240701105257.png]]

4. Right after byte bidirectional pipeline is established 