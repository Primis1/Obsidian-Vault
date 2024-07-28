***
Special values:
1. Zod - validation library used for forms, API responses, etc
2. z.datatype() - zod is an object based, and use special object {z}, with methods for all TS datatypes 
3. z.string().method - provides a methods for client validation(min )
4. `zodResolver` - is configuration function created for integration with hookforms 
5. refine() - function that's used for data validation, it take a function as a first argument and, and second as the error handler 

To know:
1. refine() accept a function, that will return a boolean, and as a second argument returns handler that will process when the returning value is false \
```ts
z.object({
	registarion: z.string()
}).refine(e => e.regisrtation === e.repeatRegistarion, {"YOU ARE IDIOT, WRITE THE FCK PASSWORD PROPERLY!!!"})
```
1. In `zodResolver` 
```ts 

const createNoteSchema = z.object({
  title: z.string(),
  text: z.string(),
});

const form = useForm({
	resolver: zodResolver(createNoteSchema),
})
```

