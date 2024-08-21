[Resources](https://react.dev/learn/importing-and-exporting-components)  
Special values:

To know:
1. I can use as many regular exports in one file as i want, however there should only be one default export
2. Finally some clarity about exporting/importing it actually affects only the syntax of those two:
```ts
export default function Button( )  => import Button from ...

export function Button( )          => import {Button} from ...
```
3. If I write default, I can set any name after import, *that is actually why we can't set as much default exports as we want.* 