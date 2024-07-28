Special values:

To know:
1. Attempt to not existing parameter gives away undefined or null
	```ts
	book.subtitle  // => undefined: property does not exist
```
2. Second example:
   ```ts
    book.subtitle.length  // => parameter undefined doesn't have property 'length'
```
3. Type protection:
   ```ts
	let surname = undefined;
	if (book) {
		if (book.author) {
			surname = book, author, surname;
		}
	}

// shorter variation 

	surname = book && book.author && book.author.surname;

// with use of 'optinal' properties 

	let surname = book?.author?.surname;
```
