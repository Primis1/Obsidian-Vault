

API


useless in this case but will in the #future
```ts
import React, { useState } from 'react';

function MyComponent() {
    const [isHovered, setIsHovered] = useState(false);

    return (
        <header 
            className={`header ${isHovered ? "stroke" : ''}}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
        >
            {/* Your content */}
        </header>
    );
}

export default MyComponent;
```


