***
[[JS object]]
Special values:
1. `constructor( )` - method where we can manipulate arguments of the class itself, which are passed during initialization `const obj = new Class(2, 3)`
2. `this` - used for accessing to environment variable
To know:
1. `constructor()` - is called when the object is initialized
2. Scope within the `method( )` is not really class environment. It starts to support regular, global, scope 
```ts
class FetcClass {
  constructor() {
    console.log("constructor")
  }
}

const obj = new FetcClass

// constructor 
```
2. With use of this, we can access the environment variables, `if they are declared`, otherwise `this` returns and empty object `{}`
	 - Each method or inherited class has its own environment 
3. Suffixes:
	1. public - default suffix. Properties can used in access in ==subclasses== and via `dot notation`
	
	2. protected - properties can be accessed `only in subclasses`. Should be specified every time 
	
	3. static - such methods are not bind to any class instance, they are accessible through class constructor 
	
	4. private - accessed only within the current class-scope
- ==TS is that useful, therefore we can access every single method of property in iterations, despite the given suffix==  
```ts
class FetchDataClass {
  private baseURL: string = "https://pokeapi.co/api/v2/";
  private headers: Record<string, string> = {
    "Content-Type": "application/json",
    Accept: "application/json",
  };
  
  async post({ url, headers, body }: DeliverData) {
    const res = await fetch(this.baseURL + url, {
      method: "POST",
      headers: headers,
      body: JSON.stringify(body),
    });
    return this.handleResponse(res);
  }

  async delete(url: string) {
    const res = await fetch(this.baseURL + url, {
      method: "delete",
    });
    return this.handleResponse(res);
  }
  // error handling in class 
  private async handleResponse<T>(response: Response) {
    if (!response.ok) {
      throw new Error("HTTP request went wrong!!!");
    }
    return await response.json();
  }
}
export const fetchData = new FetchDataClass();

```