*** 
Special values: 
1. Immutability - once an object or state was created it can *not* be changed
	1. remember that method that can change a string does ==*NOT*== exist(but we can modify string objects btw)
2. `map( )/foEach( )` - ==map== always returns  a new arrays, and can modify the existing one. forEach is the same, but can be used when there is no-need to return value

To know:
1. Immutable state advantages: 	
	1. We can track the full history of state changes(we basically create a new object, that we can put wherever we want)   
	
	2. Cons:
		1. Immutable state is usually hard for server, because lots of shit with -c obj, -r unused field, etc. So it is tough if it is on a server side. ==BUT== nobody forbid about clients ==devices==) 
	

2. Mutable state disadvantages: 
	3. Hard to track the changes in the the mutable/global object/state
	4. Hard to keep the history of the state

2. Immutable updates:
	*IT IS BASICALLY OOP*
	1. Incapsulate the state or object 
	2. Copy/inherit the values into the new object 
	3. Make changes into the created one 
	4. Snippet:
```ts
const immutableObject = {
    name: "Olaf",
    post: [
        {title: "Berserk"},
    ]
}

const mutatedObject = {
    ...immutableObject,
    name: "Polya",
    post: [
        ...immutableObject.post,
        {title: "Warhammer"},
    ]
} 

console.log(mutatedObject) //?

//with plain arrays, with only index access 

const abilities = skills.map((skill) =>
    skill.value === 'figma'
        ? { ...skill, value: 'useless part', label: undefined }
        : skill
);
```
3. Check did someone changed a global object:
```ts
function c(obj, obj2) {
    if(obj === obj2) {
        return "not changed"
    } else {
        return "who is this mf????"
    }
}

c(immutableObject, mutatedObject)
```

Reminders: 
1. React immutability is a paradigm, according to which we have to create a new property or state instead of modifying it.
	1. Because of [[DOM vs Virtual DOM]] 
2. In react component re-render when [[State]] is changed(it force component to mount)