***
[[Testing]]
Special values:
1. Play wright - is a testing framework, used for E2E testing 
2. end-to-end - testing is kind of testing that emulates user's interactions with web-application  

To know:

- Facts:
1. ==Play wright generally used for UI testing== across the browser( click on a button, navigates the URL, fill user input)
2. Play wright can ==also== check the ==HTTP==  requests 
3. Each test has ==it's time - 30s==. If action takes longer than that, Play wright will through an error 
4. Each test is ==open in it's tab==. Kills the possibility of one test, interrupts the flow of other  

- Core syntax:
5. `test("name", async  ({page}) => {})` - ==main== object with all methods that are used by Play wright
6. #await - because we declare actions of our test, we can use #await for asynchronous operations(all actions of user are asynchronous) 

7. `page object` - is the main object within the test's scope, it contains all methods used for testing 
8. `locators`  - are used to select the DOM element on a page 
9. `locators.action` - are used to perform action over selected element, 
```ts
test("my new test", async ({page}) => {
	//navigate to the url, where component should be tested  
	await page.goto("https://full-url")
	
})
```