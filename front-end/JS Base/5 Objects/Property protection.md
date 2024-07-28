Special values:
#In - more advanced description that was in previous chapter

To know:
1. Tag #in expects the name of the property and on the right side object
2. #in returns true if object has the property with the specific name
```ts
	let о = { х : 1 };
	"х" in о  // => true: о имеет собственное свойство "х"
	"у" in о  // => false: о не имеет свойства "у”
	"toString" in о  // => true: о наследует свойство toString
```