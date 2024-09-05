***
[[Design Patterns]]
### To know:
1. #simple-factory - pattern that generates an instance for client without exposing any inner logic 
2. We shall apply it when creating an object is long, heavy weight process, and it repeats multiple times
### Implementation:
```ts 
interface Door {
    getWidth(): number,
    getHeight(): number,

}

class WoodenDoor implements Door {
    height: number
    width: number

    constructor(width: number, height: number) {
        this.width = width
        this.height = height
    }

    getWidth(): number {
        return this.width
    }
    getHeight(): number {
        return this.height
    }
}

class DoorFactory {
    static makeDoor(width: number, height: number) {
        return new WoodenDoor(width, height)
    }
}

const door1 = DoorFactory.makeDoor(12, 23)

const door2 = DoorFactory.makeDoor(43, 12)

console.log('Width: ' + door1.height);
console.log('Height: ' + door1.width);

console.log('Width: ' + door2.height);
console.log('Height: ' + door2.width);
```

```go 

```