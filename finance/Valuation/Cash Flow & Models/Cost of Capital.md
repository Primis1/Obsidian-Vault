***
### Terms Recognition:

### Concepts:

#### 
#### Cost of Equity: 
- CAPM with different betas: upside/downside, bottom up, unleveraged beta
- 
#### Cost of Debt :
- Company's credit rating(S&P, Moody) shall be used to estimate cost of debt in **company's currency**. $$IFR + Rating = CoD$$
- If company does not have rating, we use ***Interest Coverage Ratio***$$\text{EBIT(Operating Income) / Interest Expenses} $$
	- The higher the ratio, the better. It indicates what margin company has towards its interest payments 

- Cost of equity is required for estimated **cost of capital**. We can get the rate from interest expenses divided to and by **a) `Debt`** (*to get the exact rate of expenses, **which however doesn't show the future cost of debt***) **b)`EBIT/Operating Profit`**

- Debt is tax deductible, true value of cost of is $$\text{Before tax CoD * (1 - Tax Rate) = After Tax Cost of Debt}$$

##### Proxy rating:
- It doesn't account for country and currency. For EM, `Risk free rate + Default Spread + Default Spread` 

| Large Cap      | Non Fin |          |        |     | Small Cap      | Non Fin |          |        |
| -------------- | ------- | -------- | ------ | --- | -------------- | ------- | -------- | ------ |
| Interest Ratio |         |          |        |     | Interest Ratio |         |          |        |
| 8.5            | 100.00  | Aaa/AAA  | 0.45%  |     | 12.5           | 100.00  | Aaa/AAA  | 0.45%  |
| 6.5            | 8.50    | Aa2/AA   | 0.60%  |     | 9.5            | 12.50   | Aa2/AA   | 0.60%  |
| 5.5            | 6.50    | A1/A+    | 0.77%  |     | 7.5            | 9.50    | A1/A+    | 0.77%  |
| 4.25           | 5.50    | A2/A     | 0.85%  |     | 6              | 7.50    | A2/A     | 0.85%  |
| 3              | 4.25    | A3/A-    | 0.95%  |     | 4.5            | 6.00    | A3/A-    | 0.95%  |
| 2.5            | 3.00    | Baa2/BBB | 1.20%  |     | 4              | 4.50    | Baa2/BBB | 1.20%  |
| 2.25           | 2.50    | Ba1/BB+  | 1.55%  |     | 3.5            | 4.00    | Ba1/BB+  | 1.55%  |
| 2              | 2.25    | Ba2/BB   | 1.83%  |     | 3              | 3.50    | Ba2/BB   | 1.83%  |
| 1.75           | 2.00    | B1/B+    | 2.61%  |     | 2.5            | 3.00    | B1/B+    | 2.61%  |
| 1.5            | 1.75    | B2/B     | 3.00%  |     | 2              | 2.50    | B2/B     | 3.00%  |
| 1.25           | 1.50    | B3/B-    | 4.42%  |     | 1.5            | 2.00    | B3/B-    | 4.42%  |
| 0.8            | 1.25    | Caa/CCC  | 7.28%  |     | 1.25           | 1.50    | Caa/CCC  | 7.28%  |
| 0.65           | 0.80    | Ca2/CC   | 10.10% |     | 0.8            | 1.25    | Ca2/CC   | 10.10% |
| 0.2            | 0.65    | C2/C     | 15.50% |     | 0.5            | 0.80    | C2/C     | 15.50% |
| -100           | 0.20    | D2/D     | 19.00% |     | -100           | 0.50    | D2/D     | 19.00% |

#### Bond-debt valuation - to calculate market value of debt we shall use NPV and transform debt into coupon 
- Unlike book approach(number on balance sheet), MV of debt may give insights into company's **real liabilities**
- On average, long term debt(both OL and NOL) ==is issued for 7-8 years==, therefore we perform and discount for that period. 
	- In footnotes business often specify maturity of debt
	- We take book amount, get the weight of debt, and then multiply weight on maturity 
![[Pasted image 20250401223448.png]]
- We discount payments, getting principal value and adding leases 
![[Pasted image 20250402002032.png]]




#### WACC  - the problem with excluding Tm(marginal tax rate) is that it isolates company's capital structure(we remove tax shield from equation) and focus solely on company operations. But tax shield has adds value, if it has value it can be used in cash-flow valuation   $$\frac{D}{D+E}k_d (1-T_m) +\frac{E}{D+E}k_e$$
- D - debt 
- E - equity 
- T - marginal tax rate
- K d, e - cost of debt and equity
- How much money they can generate for single dollar of assets (`Net Income / WACC`)
