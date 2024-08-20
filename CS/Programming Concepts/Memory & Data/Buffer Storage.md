*** 
[[Memory & Data]]
Special values:
1. #buffer - buffer advanced data structure, it temporary storge that helps to transfer data between components when their reading/writing speed is not the same (buffer zone) or when we want to reduce amount request

To know:
1. As an example of use:
	1. Fast #CPU sent data to the slow external device, would not be possible without a buffer storage
2. We can build our own buffer for application 
3. Buffer could be overflowed
4. The size of buffer affects the performance, if we gonna make it too big, it'll result underutilization, if too small, it'll cause a data loss 
![[Pasted image 20240626114508.png]]