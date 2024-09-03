***
Components: 
1. ==type== TitleSize - type for identifying the component size
2. ==interface== Props - used for *props* of component 
	- size?: TitleSize 
	- className: string 
	- text: string 
3. ==const== mapTagBySize - used for identifying the HTML tag in the properties of `React.craeteElement()` 
4. ==const== mapNameBySize - we identifying the size properties of tailwind, according to size parameter 

5. return `React.craeteElement()` - creates a new component, immutable, component based on the settled params 

Assembling:
- Each of these constants or more like maps, has the same keys' that argument has, we basically accessing the value we want, through the typed argument 
```ts
import clsx from "clsx";
import React from "react";

type TitleSize = "xs" | "sm" | "md" | "lg" | "xl" | "2xl";

interface Props {
  size?: TitleSize;
  text: string;
  className: string;
}

export const Title: React.FC<Props> = ({ size = "sm", text, className }) => {
  const mapTagBySize = {
    xs: "h5",
    sm: "h4",
    md: "h3",
    lg: "h2",
    xl: "h1",
    "2xl": "h1",
  };

  const mapClassNameBySize = {
    xs: "text-[16px] ys-text",
    sm: "text-[22px] ys-text",
    md: "text-[26px] ys-text",
    lg: "text-[32px] ys-display",
    xl: "text-[40px] ys-display",
    "2xl": "text-[48px] ys-display",
  };

  return React.createElement(
	  mapTagBySize[size],
	  { className: clsx(mapClassNameBySize[size], className)},
	  text	  
  );
};

```