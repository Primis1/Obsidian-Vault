***
[[GO WEB]]
### Special values:
1. #channels - are conduits(турбопровід) through which you can send and receive values ==between== ==goroutines== 
	1. `chan value` - is special keyword for creating a new channel. Its initialize in `make(chan int)`
	2. `<-` - ==`operator`== used for sending or receiving information on channel 
2. #channels have the following characteristics:
	1. They are ==typed== 
	2. The ==values== are transmitted/received in ==synchronous== way
	3. The ==values== are transmitted/received in ==FIFO== manner
	4. They can be either buffered or unbuffered 
	5. They are bi-directional 
	6. Data can have only one initial receiver. Two channels can't take the same data  
### To know:

1. Channels characteristics(detailed):
	1. They are ==typed==. You send and receive value ==ONLY== of the same type. You ==can't send string and int over same channel(гаuшники блять)== 
	
	2. The ==values== are transmitted/received in ==synchronous== way. The sender/receiver ==must wait== until other is ==finish== ==before== ==doing== their ==action==
	
	3. The ==values== are transmitted/received in ==FIFO== manner. First in, First out
	
	4. They can be either buffered or unbuffered. Channel hold the number of value before sending it, reducing the quantity of requests 
	
	5. They are directional. To send and receive. Or just send ==OR== receive 

2. Blocking and Unblocking channels:
	1. channels are blocked by default and can ==NOT== receive nor send data, until the CH is "==unblocked==" or ==invoked==
		- Like calling a phone, while call rings audio channel is still blocked, but right after phone on the other side is accepted - channel is unblocked 
	
	2. The channel will await until it receives the data which was send, somewhere, lower on a stream line
		-  ==SKIP, RECEIVE, DETONATE THE SKIPPED, RUN THE RECEIVER== 
	
	3. ==We use goroutine to manage this behavior, because only with goroutines we can indicate to WAIT for code to to be executed== 
	
	4. We should ==close the channels== after it's purpose is settled 
```go 
func Janis(ch chan string) {
	//this line await for the receiver to put some data into the channel 
	msg := <-ch
	//pass the assigned data into the print
	fmt.Println("Jimi said:", msg)
	//parse new data into the channel, because it is a fck function, dude like cmon 
	ch <- "Hello Jimi"
}

func main() {
	phone := make(chan string)

	defer close(phone)

	go Janis(phone)
	// parse some data into the channel 
	phone <- "Hello, Janis"
	// we assign the changed data into the new variable
	msg := <-phone
	fmt.Println("Janis Said:", msg)
}

Jimi said: Hello, Janis
Janis Said: Hello Jimi
```

Implementation:
1. <- operator points (left side) into the place, data will go ==from== (right side) 
```go
ch <- 12 // data is sent to the channel 
myVar <- ch // 
<- ch // data goes in NOWHERE from the channel 
```
2. Usually we want to listen on incoming information on channel, until it closes. To do that we can take for and for/range loops, 