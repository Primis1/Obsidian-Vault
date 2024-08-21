Special values:

1. Single page application - it is the web page that consists from single minimalistic HTML file, and gets all other functionality from the JS components 

2. Multi page application - it the web page that consists from multiple html pages

To know:
1. Single page application are faster because it just render the bundle on a server and gives it back to the user immediately 
	1. Despite of fast on-page work, such applications take more time for the primary load
		1. It can be optimized by well adjusted constructor(webpack, vite)
		2. Lazy loading *?*