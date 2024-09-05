***
### Special values:
1. #prisma - is an #ORM for JS/TS ecosystem. It can be used for `node` in general and `nextJS` in particular.
2. Prisma application components:
	- `prisma-client` - main object through which we do our queries, is generated based on schema. Queries are made over the `table`
	- `prisma-schema`- file where the database described, there are ==migrations==, ==relations==, ==actual DB URL==
	- `prisma-migrate`- keeps track over the history of my DB changes 
	- `prisma-CLI` - command line of prisma, `prisma init`, `prisma migrate`, `prisma generate`
3. Prisma-client functions:

### To know:
```ts
//             write
	const newUser = await prisma.user.create({
	  data: {
	    name: 'Alice',
	    email: 'alice@example.com',
	  },
	});
// over and under we create records
	const newUsers = await prisma.user.createMany({
		data: [
		{name: "Olaf"},
		{name: "Polya"}
		]
	})
// UPDATE
	const updateUser = await prisma.user.update({
		where: {id: 2},
		// modify existing value 
		data: {name: "Ruzaya Tvar", age: {increment: 1}},
		inclide: {name: true}
	})

//            READ
	const user = await prisma.user.findMany()
	const uniqueUser = await prisma.user.findUnique({
		where: {name: "Polya"}
	})
	const userFields = await prisma.user.findMany({
		select: {
			name: true,
			email: true
		}
	})
```
