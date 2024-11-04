***
[[Design Patterns]]
### Special values:
1. #abstract-factory - produces families of related objects, **without specifying their concrete classes** 

### To know:

#### Concepts:

- ##### Applicability - use the Abstract Factory when your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products

- ##### Problem - project requires several object in of same *sector*, but different in its logic - to be organized 

- ##### Solution:
1. Define explicit interface for each object family
2. Create children object following those interfaces 
	Chair  -> Coffee Chair + Game Chair

- ##### Declare an #abstract-factory, an interface with list of creation methods for all products of the family  
	CreateChair  -> CreateCoffeeChair -> CreateGameChair

	- These methods should abstract product *type* represented by previous interface
![[Pasted image 20241104003000.png]]

- ##### For each product of object family we create separate factory `class` based of `AbstractFactory` ==interface==
	- A factory is a class which returns product of particular kind.
		`ModernFurnitureFactory` -> `ModernChair` + `ModernSofa` + `ModernCoffeeTable`
![[Pasted image 20241104003646.png]]