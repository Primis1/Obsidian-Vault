import pandas as pd

# Define the structure of the Excel file
data = {
    "Co. Characteristics": ["Ticker", "Name", "Sector", "Industry", "Country", "Market Cap"],
    "Historical Growth": [
        "1Y EPS Gr", "3Y EPS Gr", "5Y EPS Gr", "10Y EPS Gr", 
        "1Y CF Gr", "3Y CF Gr", "5Y CF Gr", "10Y CF Gr",
        "5Y Sales Growth", "1Y Price Perform", "3Y Price Perform", 
        "5Y Price Perform", "10Y Price Perform", "20Y Price Perform"
    ],
    "Forecasted Growth": [
        "EPS", "Est EPS Gr", "Est EPS", "Est EPS Tgt Price", "Price",
        "Est EPS Tgt G/L", "Est EPS Tgt ROR", "Est EPS Tot Ann ROR",
        "Analyst Price Tgt M", "Analyst Price Tgt Med", "Finbox Fair Value"
    ],
    "Dividend": [
        "Yield", "Payout Ratio", "1Y Div CAGR", "5Y Div CAGR", "10Y Div CAGR", "20Y Div CAGR",
        "Chowder #", "Est. Div", "Est Div Growth"
    ],
    "Returns": [
        "Return on Assets", "CAGR 5Y ROA", "Return on Equity", "CAGR 5Y ROE", "Return on Investment"
    ],
    "Valuation": [
        "P/E", "5Y Norm PE", "10Y Norm PE", "20Y Norm PE", "Forward PE", "PEG",
        "P/FCF", "5Y Norm P/FCF", "10Y Norm P/FCF", "20Y Norm P/FCF",
        "P/S", "P/FS", "P/B", "5Y Ave P/B", "Piotroski Score"
    ],
    "Margins": ["Gross Margins", "Operating Margins", "5Y CAGR OM", "Profit Margins", "GPM 5Y CAGR"],
    "Company Safety and Stability": [
        "LT Debt to Equity", "Debt to Equity", "Short Term Debt Covrg", "LT D/C",
        "Interest Coverage", "D Paydown Yield", "Credit Rating",
        "Current Ratio", "Quick Ratio", "FCF Yield"
    ],
    "Future": ["Beta", "Moat", "Future"]
}

# Create a Pandas Excel writer object
file_path = "/mnt/data/Stock_Comparison_Template.xlsx"
with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
    for section, columns in data.items():
        df = pd.DataFrame(columns=columns)
        df.to_excel(writer, sheet_name=section, index=False)

file_path
