#### Question 1: Graph and Find Intersections  
I need to graph $y = -2(x-1)^2$ and $y = -8$ and **find where they intersect**.  
- $y = -2(x-1)^2$ is a downward parabola. The vertex is at $x = 1$ because $(1-1)^2 = 0$, so $y = 0$.  
  - At $x = 0$: $y = -2(0-1)^2 = -2(1) = -2$ → point $(0, -2)$  
  - At $x = 2$: $y = -2(2-1)^2 = -2(1) = -2$ → point $(2, -2)$  
	- $y = -8$ is a horizontal line at $-8$.  
- For intersections, set them equal:  
  $-2(x-1)^2 = -8$  
  $(x-1)^2 = 4$  
  $x-1 = 2$ or $x-1 = -2$  
  - $x = 3$  
  - $x = -1$  
  Check $y$: both give $y = -8$, so points are $(3, -8)$ and $(-1, -8)$.  
- (I’d sketch the parabola dropping from $(1, 0)$ to hit the line at those points.)  

**Answer:**  
$\boxed{(3, -8) \text{ and } (-1, -8)}$
![[Pasted image 20250225134751.png]]

---

#### Question 2: Are These Functions?  
**a. $[(-6, 4), (-3, -3), (0, -3), (2, 1)]$**  
- A function means each $x$ maps to one $y$. Check $x$-values:  
  - $-6, -3, 0, 2$ → all unique.  
- No repeats, so it’s a function!  

**Answer:**  
$\boxed{\text{Yes, it’s a function because each } x \text{ has one } y}$

*(b and c are missing, so I’ll leave it here.)*

---

#### Question 4: Find $f(m+1)$  
Given $f(x) = 2x^2 - 3x$, find $f(m+1)$.  
- Substitute $m+1$:  
  $f(m+1) = 2(m+1)^2 - 3(m+1)$  
- Expand:  
  - $(m+1)^2 = m^2 + 2m + 1$  
  - $2(m+1)^2 = 2(m^2 + 2m + 1) = 2m^2 + 4m + 2$  
  - $-3(m+1) = -3m - 3$  
- Combine:  
  $2m^2 + 4m + 2 - 3m - 3 = 2m^2 + 4m - 3m + 2 - 3 = 2m^2 + m - 1$  

**Answer:**  
$\boxed{2m^2 + m - 1}$

---

#### Question 5: Inverse of $f(x) = -7x + 5$  
- Swap $x$ and $y$:  
  $y = -7x + 5$ → $x = -7y + 5$  
- Solve for $y$:  
  $x - 5 = -7y$  
  $y = \frac{x - 5}{-7} = -\frac{x - 5}{7}$  
- Simplify:  
  $y = -\frac{x}{7} + \frac{5}{7}$  

**Answer:**  
$\boxed{-\frac{x}{7} + \frac{5}{7}}$

---

#### Question 6: $f(x) = \sqrt{x + 2} - 3$  

**a. $f(-2)$**  
- $f(-2) = \sqrt{-2 + 2} - 3 = \sqrt{0} - 3 = 0 - 3 = -3$  

**Final Answer:**  
$\boxed{-3}$

**b. What’s $f(-2)$ on the graph?**   
- $f(-2) = -3$ means the point is $(-2, -3)$. It’s the starting point since $x + 2 = 0$ at $x = -2$.  

**Answer:**  
$\boxed{\text{Point } (-2, -3)}$

**c. Domain and Range**  
- Domain: $x + 2 \geq 0$ → $x \geq -2$ → $[-2, \infty)$  
- Range:  
  - At $x = -2$, $y = -3$ (minimum).  
  - As $x$ increases, $\sqrt{x + 2}$ grows, minus 3 shifts it down, so $y \geq -3$ → $[-3, \infty)$  

**Final Answer:**  
$\boxed{\text{Domain: } [-2, \infty), \text{ Range: } [-3, \infty)}$

**d. Why is it a function?**  
- Each $x$ gives one $y$ since the square root has one value, and subtracting 3 doesn’t change that. It passes the vertical line test—looks like a sideways curve.  

**Answer:**  
$\boxed{\text{It’s a function because each } x \text{ has one } y}$

---

#### Question 7: Transformed Functions  

**a. $f(x) = x^2$, compressed by $\frac{1}{3}$ horizontally, reflected in $y$-axis, 1 left, 5 up**  
- Start: $x^2$  
- Horizontal compression by $\frac{1}{3}$: $x$ becomes $3x$ → $(3x)^2 = 9x^2$  
- Reflect in $y$-axis: $(-x)^2 = x^2$ (no change).  
- 1 left: $x$ becomes $x + 1$ → $9(x + 1)^2$  
- 5 up: $9(x + 1)^2 + 5$  

**Answer:**  
$\boxed{9(x + 1)^2 + 5}$

**b. $y = \frac{1}{x}$, compressed by $\frac{1}{3}$ horizontally, 3 left, 2 up**  
- Start: $\frac{1}{x}$  
- Compress by $\frac{1}{3}$: $x$ becomes $3x$ → $\frac{1}{3x}$  
- 3 left: $x$ becomes $x + 3$ → $\frac{1}{3(x + 3)}$  
- 2 up: $\frac{1}{3(x + 3)} + 2$  

**Answer:**  
$\boxed{\frac{1}{3(x + 3)} + 2}$

---

#### Question 8: Plot $\frac{1}{2} f(2x) + 3$  
Assuming $f(x) = \sqrt{x + 2} - 3$ from Q6 since no graph was given.  

- **Steps:**  
  - $f(2x)$: Horizontal compression by $\frac{1}{2}$, $x$-values halve.  
  - $\frac{1}{2} f(2x)$: Vertical compression, $y$-values halve.  
  - $+3$: Shift up 3.  

- **Transform points:**  
  - $(-2, -3)$ from $f(-2)$:  
    - $f(2x)$: $x = -1$ (since $2 \times -1 = -2$), $y = -3$ → $(-1, -3)$  
    - $\frac{1}{2}$: $y = \frac{1}{2} \times -3 = -1.5$ → $(-1, -1.5)$  
    - $+3$: $-1.5 + 3 = 1.5$ → $(-1, 1.5)$  
  - $(2, -1)$ from $f(2) = \sqrt{4} - 3 = -1$:  
    - $x = 1$ (since $2 \times 1 = 2$), $y = -1$ → $(1, -1)$  
    - $\frac{1}{2} \times -1 = -0.5$ → $(1, -0.5)$  
    - $-0.5 + 3 = 2.5$ → $(1, 2.5)$  
  - $(-1, -2)$ from $f(-1) = \sqrt{1} - 3 = -2$:  
    - $x = -0.5$, $y = -2$ → $(-0.5, -2)$  
    - $\frac{1}{2} \times -2 = -1$ → $(-0.5, -1)$  
    - $-1 + 3 = 2$ → $(-0.5, 2)$  

- **Plotting:**  
  - Points: $(-1, 1.5)$, $(-0.5, 2)$, $(1, 2.5)$.  
  - It’s a flatter square root curve starting at $(-1, 1.5)$, rising slowly above the x-axis.  
  - (I’d sketch it curving through those points.)  

**Answer:**  
$\boxed{\text{Plot points like } (-1, 1.5), (-0.5, 2), (1, 2.5) \text{ and sketch a flatter curve shifted up}}$

