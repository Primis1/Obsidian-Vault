p.156
Special values:
#object - that is a complex value, it allows us to keep and extract internal values by its name.
#new - it is an operator that used to create a new object or class from another 

To know: 

1. In JS everything, besides of: numbers, strings, bool, undefined, and Symbol - are objects
2. Every object has properties.
	1. Property has name and values. 
	2. Name could be every string, included "empty string". But no object can have two properties with the same name. 
	3. Value could be every values or function
3. Properties which weren't inherited called "own property"  

4. Examples of using #new not with classes but global methods
```ts
let о = new Object ();  // Создает пустой объект: то же, что и {}
let а = new Array ();  // Создает пустой массив: то же, что и [ ]
let d = new Dated ; // Создает объект Date, представляющий текущее время
let г = new Мар (); // Создает объект Мар для отображения ключ/значение
```
