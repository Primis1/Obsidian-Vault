***
### Special values:

- Options - derivatives/contracts which are bought ahead of time, have lifespan, force side A to sell 100 shares to the side B, for premium

- ITM, OTM - can be exercised(execute contract) other don't may expire worthless(yep lost premium if we aren't someone who wrote an option)

### Concepts:

#### Looking contract: 
- Call - derivative to sell you stock for lower price, when stock rose up
- Put - derivative to sell you the stock at higher price, when stock goes down   

### Sentiments:
- The higher the premium for option, the lesser chance for achieving the price 
- Drops/Spikes in prices indicates momentum sentiments about soon growth
	- After rise, same diapason of above strike prices may drop or stay the same, depending on what to expect
#### Option implied `*Culmunative Distribution Function*` - formula estimates the sentiments in current option period
- Theoretical CDF(Black Scholes model) - represents rational(base case) sentiments-free baseline

Difference between those two indicates current sentiment of the market, based on option price across maturities 
- If negative(-) - investors are optimistic towards the rise
- If positive(+) - market is pessimistic and expects that bottom has yet to be reached

##### Drivers 
- **Current Stock Price ($S_0=71$)**: 
- **Option calls and puts** - shows what investors are willing to pay(current sentiment)
	- Calls: $65 = $7.50, $70 = $4, $75 = $1.80, $80 = $0.70
	- Puts: $65 = $1.20, $70 = $2.80, $75 = $5.50, $80 = $9.20
- **Time to Maturity ($T=1month$)**:
- $r$  - risk free rate, 4%
- **Volatility ($\sigma = 35\%$)** - volatility annualized? The higher volatility, the bigger are premiums(luck is priced in)
- **Dividends **($\delta$)**** - if none, price is drive solely by growth factor

##### Calculations:
- We use rational(baseline) and emotional drivers for each strike price, then sum the difference and get the probability 

##### *ITM strikes*
Sentiment indicator for Calls:
$$
\Psi_0^c(T) = \sum_{K_i \in K} \left( \Theta^c(K_i, T) - \bar{\Theta}^c(K_i, T) \right)
$$
Sentiment Indicator for Puts:
$$
\Psi_0^p(T) = \sum_{K_i \in K} \left( \Theta^p(K_i, T) - \bar{\Theta}^p(K_i, T) \right)
$$
##### *Not-ITM strikes*
Call:
$$
\Psi_1^c(T) = \sum_{K_i \geq S_0} \left( \Theta^c(K_i, T) - \bar{\Theta}^c(K_i, T) \right)
$$
Put:
$$
\Psi_1^p(T) = \sum_{K_i \leq S_0} \left( \Theta^p(K_i, T) - \bar{\Theta}^p(K_i, T) \right)
$$

