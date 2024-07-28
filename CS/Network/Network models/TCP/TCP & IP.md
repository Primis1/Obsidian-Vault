***
Special values: 
1. #TCP - Transmission Control Protocol help to deliver HTTP messages, and do that in correct order
2. #IP - Internet Protocol is the unique number of each computer that helps other computers to find it, it helps requests to deliver a message into the right place 

To know: 
1. TCP:
	1. How it works:
		1. [[Flow of TCP]]
		2. We send a packets of data to the remote computer, when an individual packet gets received, the remote computer sends an acknowledge("Sup, i got packet number 4") to the sender
		3. If computer doesn't get an acknowledge in a curtain time, it sends it again; if packet got corrupted, I send it again.
2. IP works:
	1. Each computer has the list of computers it knows about, and how to get to them. It calls a ==routing table==
	2. Address:
		1. Address of the C is has two forms: the ipv4 - 32bit number;  ipv6 - 128bit number
		2. IPV4 looks like DDD.DDD.DDD.DDD, it ranges between 0-255
		3. IPV6 looks like XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX, it ranges between 0-9 and a-f
	3. Port of the service it delivers a message, depends on a behave or purpose of the service. Each IP address should have a port, a port could be any number in 0-65535 range 
		1. Default ports:
			1. HTTP/80
			2. HTTPS/443
			3. SSH/22
			4. SMTP/25
			5. DNS/53
			6. FTP/21
			7. Postgres/5432
	4. How It works:
		1. When we have to deliver message, computer check its ==route table== for the path to *that* computer, if its undefined, so it check the route table of *other* computer it know.
		2. It works in the chain-kind way, until they find the right computer
		3. if there is no use, the request if fail. 