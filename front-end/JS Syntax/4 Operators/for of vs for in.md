***
[[Loops & stuff]]
Special values:
1. #for/in - iterates over unlimited amount of properties in the object 
2. #for/of - iterates over the values of arrays

To know:
1. Both loops are iterating as many times, as the length of the iterated is  
```ts
const book = {
	title: 'JavaScript for Beginners',
	price: '$9.99', 
	year: 2018,
	pubisher: 'Amazon, Inc.'
}

for ( const prop in book) {
	console.log(`${prop} ${book[prop]}`) // 'title' 'price' 'year'
	//this one is clever
}
```