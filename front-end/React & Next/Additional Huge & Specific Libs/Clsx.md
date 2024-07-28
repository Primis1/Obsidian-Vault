***
Special values:
1. clsx - is a completely optional lib, that helps to reduce code-snippets for conditional styling 
	1. It has the following structure  className={clsx(==default/regular-styling==, ==condition==: optinal-styles)} 

Extra:
1. We can pass the whole functions and variables inside of class, so we can pass the whole well-organized properties with multiple conditions(just like in shad-cn)
```ts
const variant = clsx(
	styles.base/tailwind property,
	[styles.base]: buttonTheme === "outlone",
	[styles.base]: buttonTheme === "zinc",
	[styles.base]: buttonTheme === "ghost",
)
```