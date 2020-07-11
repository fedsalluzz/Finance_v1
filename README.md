# FINANCE V1

> Financial analysis on companies

## How to use this tool:
- Clone the folder
- From inside the folder run gui_finance.py from your terminal
- Add the tickers comma-spaced e.g. JNJ,QCOM
- Select years NOTE: MAX is not always present for all the stocks
- Click ANALYZE
- ENjoy the analysis
- log files wit Ratios (PBV,PE,ROE etc) for selected companies are in the data folder

NOTE: buttons EPS and BV can plot data for just one share

## Company key metrics

> This section contains data retrieved from the financial documents published by the companies (Income statement, Cash Flow, Balance sheet)

### Basic terms
- Revenue = Ammount of money the company make.
- Net Income = Net Profits = Revenue−COGS−Operating and other expenses−Interests−Taxes
- COGS = The cost of goods sold
	
### From the Income statement:
- Earnings x share (EPS): =((Net Income - preferred dividends) /shares outstanding). It is used as an indicator for company profitability. Higher number means company is more profitable. EPS diluted is often used, considering as the shares outstanging number the one calculated over the assumpion that all option,warranty etc. were converted immediatelly in stocks.
> EPS and Capital: EPS does not take into account the capitar required to generate the earnings (net income). To know the efficiency look at the ROE.

> EPS and Dividends: EPS does not turn into profit for shareholders. Part of the EPS is moved into the Dividends, part is retained back into the company.

> N.B EPS can be intentionally or unententionally faked by companies. Ofter to make this factor more realistic you would to use more precise formula: 
 EPS = (NI - PD +/- Extra Items +/- Discontinued operations)

> where Extra items = gain or losses related to one-time operation (e.g one factory burned (loss) or one land sell (gain) )

> where Discontinued operation = gain or loss related to specific operation valid in the period (e.g. part of the stores closed)

- Net Income Ratio : =(Net Income/Revenue). It is also called Net Margin or Net Profit margin and it is expressed in percentage of the revenue. It describes how much of a given dollar in Revenue is translated into profit. Net profit margin is one of the most important indicators of a company's financial health.

> Limitation of Net Income Ratio : Net income ratio can be boosted by one time sale or other factors. It is used usually with Gross profit margin and operative profit margin
### From the Balance sheet:
- Book value per share: ((Asset - Intangible assets - Liabilities)/Outstanding shares).  Also called "Net Book Value" or "Net asset value" , calculate what is the asset the shareholders would receive if the company were liquidated. When compared to market price it can tell you if a company is over or under priced.
- Debt to equity:


## Current Ratios

> This section contains ratios calculated over the actual price of the stock

- Price per earnings ratio (PE):
- Price per book value ration (PBV):
- Price earnings to growth ratio (PEG):
- Divident Yield (DIV):
- Return on Equity (ROE):

## To be added:

- Beta:
- Liquidity indicators:
- Net Debt:




