
***
### Special values:
1. #facade - structural design pattern, used for:
	1. reducing dependency overlay 
	2. protecting the class
	3. reducing non-used logic 

### To know:

##### Problem:
- *Large object with many sub-objects, which can be a library or framework. It leads to unnecessary managing of its dependencies, track for order of execution. Also a more complex alternative to #singleton, what allows us to reduce number of dependencies*

#### Concepts:
##### Solutions:
- #facade - is a class that provides simple interface for complex systems

```go
// Facade interface
package storefacade

import (
    "fmt"
)

// Inventory subsystem
type Inventory struct{}

func (i *Inventory) CheckStock(itemID string) bool {
    fmt.Println("Checking stock for item:", itemID)
    return true // assuming the item is in stock
}

// Payment subsystem
type Payment struct{}

func (p *Payment) ProcessPayment(amount float64) bool {
    fmt.Println("Processing payment of:", amount)
    return true // assuming payment succeeds
}

// Shipping subsystem
type Shipping struct{}

func (s *Shipping) ShipItem(itemID string) {
    fmt.Println("Shipping item:", itemID)
}

// StoreFacade struct as the Facade
type StoreFacade struct {
    inventory *Inventory
    payment   *Payment
    shipping  *Shipping
}

// NewStoreFacade creates an instance of StoreFacade
func NewStoreFacade() *StoreFacade {
    return &StoreFacade{
        inventory: &Inventory{},
        payment:   &Payment{},
        shipping:  &Shipping{},
    }
}

// PlaceOrder is a high-level method that wraps subsystem interactions
func (f *StoreFacade) PlaceOrder(itemID string, amount float64) {
    if f.inventory.CheckStock(itemID) {
        if f.payment.ProcessPayment(amount) {
            f.shipping.ShipItem(itemID)
            fmt.Println("Order placed successfully!")
        } else {
            fmt.Println("Payment failed.")
        }
    } else {
        fmt.Println("Item is out of stock.")
    }
}
```

```go
store := storefacade.NewStoreFacade() store.PlaceOrder("item123", 49.99)
store.PlaceOrder()
```