***
### Special values:
1. #bufio - is made for buffering #I/O. it temporary stores data till certain amount before transmitting it further, basically makes #buffer It helps in performance   
2. bufio functions:
	1. bufio.NewWriter( ) - ==wraps== the existing input/io.Writer( ) into the buffer, sends it after limit is reached 
	
	2. bufio.NewReader( ) - ==wraps== the existing output/io.Reader( ) into the buffer, gets it after limit is reached
	
	3. buffio.NewScanner( ) - it ==creates a scanner==, that returns existing io.Reader( ), but without white spaces or somethings 

### To know:
1. bufio - literary allows us create ==own buffer==, it stocks a small pieces of data in the buffer-storage, and only after some amount of it reaches, it process it further. Also provides methods for additional manipulations   
```go
func main() {  
	fmt.Println("Unbuffered I/O")  
	w := new(Writer)  
	w.Write([]byte{'a'})  
	w.Write([]byte{'b'})  
	w.Write([]byte{'c'})  
	w.Write([]byte{'d'})  
	fmt.Println("Buffered I/O")  
	
	bw := bufio.NewWriterSize(w, 3)
	  
	bw.Write([]byte{'a'})  
	bw.Write([]byte{'b'})  
	bw.Write([]byte{'c'})  
	bw.Write([]byte{'d'})  
	err := bw.Flush()  
	
	if err != nil {  
		panic(err)  
	}  
}

producer buffer destination (io.Writer)  
a -----> a  
b -----> ab  
c -----> abc  
d -----> abcd  
e -----> e ------> abcd  
f -----> ef abcd  
g -----> efg abcd  
h -----> efgh abcd  
i -----> i ------> abcdefgh
```