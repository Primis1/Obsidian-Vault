***
[[Developing Methodologies]]
[[You don't know OOP]]
### Special values:
1. #OOP - pl paradigm for writing programs 
2. #SOLID - clean code methodology for writing maintainable code in team 
3. 
***
### OOP:

#### Jots:
1. ==Encapsulation== - building method and data inside an object and restricting access for changes into that object
2. ==Abstraction== - hide inner logic of an object from the user, exposing only necessary parts of functionality via interfaces 
3. ==Inheritance== - inherit methods and data from one object to another 
4. ==Polymorphism== - ability for different objects be treated as instances of same one, via common interface of `prime-interface` 
	- `Dog` &&  `Cat` may be treated as the same object via interface `Animal` 

### SOLID:

#### Jots:

- ###### Single responsibility principle (==SRP==) - class should have one reason to change, ==i.e has one responsibility== 

- ###### Open/Closed Principle (==OCP==) -  class should be opened for extension and closed for modifications, ==new functionality should be added via inheritance==

- ###### Liskov Substitution Principle (==LSP==) - inherited children should be compatible in places where parent object is used. ==Do not ruin what already works==

- ###### Interface Segregation Principle (==ISP==) - clients should be independent from inherited methods which they don't need/use. Interfaces should use D&C, i.e ==split large interfaces into smaller one== 
	- Instead `AnimalInterface` with `swim`, `fly`, `run` - use `whoFlies`, `whoSwims`, `whoRuns` interfaces 

- ###### Dependency Inversion Principle (==DIP==) -  hierarchy of object dependency on each other. Like FSD, ==higher should not depend on lower lever==. ==Instead may depend on its abstraction==
	- Instead of depending on object itself, it can depend on object interface, `PaymentProcessor`  depends on `CreditCardPayment`; instead `PaymentProcessor` can depend on `PaymentMethod` ==interface== 
