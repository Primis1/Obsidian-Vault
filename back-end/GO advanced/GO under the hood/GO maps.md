***
[[GO advanced]]
### Special values:
1. #map - is golang implementation of #hash-table. It provide high speed==(`O(1)`)== insertion, looking and deleting operation because of `keys` 
	- associative array or dictionary or #hash-table - is an abstract data-type that work by `key-value` principle    
2. #map components:
	1. #hash-function - settled key is managed by `hash-function`, and decided to what bucket the value is going to be stored  
	2. buckets - small containers for the values, values should be evenly placed among existing buckets
	3. collision manager - go avoids collision by `chaining` method 
	4. growth and rehashing - when the amount values is close to specific capacity of the bucket, ==rehashing== begins. In that time elements are redistributed among new ==fresh== created buckets   
### To know: 
#### Syntax:
```go
//initialize the map 
map := make(map[string]int)
map := map[string]int{"foo": 1}

// get the value 
buzz := map['foo']

//re-assign 
map["foo"] = 2

// to avoid accessing not existing key, we can use second parameter
myVar, ok := map["something"]
if ok {
	return myVar 
} else {
	"key not found"
}

// delete operations are made by special method
delete(map, "foo")
```

#### Facts:
1. Map is implemented without #generic nor #interfaces. They do use `unsafe-pointers` and `type-descriptos` instead
	1. `unsafe.Pointer` - can *point* to anything 
	2. `type-descriptor` - we have to know what data `unsafe.Pointer` returns, to do so we use `type-descripor` 
		1. It contains meta-data==(information needed to work with datatype)==
```go

```