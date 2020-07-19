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

## How to evaluate a company? A brief introduction

How do you know if the current price is not overvaluated? Five things to take into consideration:
- Long term prospect
- Management
- Financial strenght and capital structure
- Dividends records
- Actual dividend rate

Look at the financial statements and ask yourself:
- What makes this company grow?
- Where does the profit came from?

Potential problems can be:
- Company is a serial acquier. Most of the acquisition went bad. Why should this company buy another one instead of investing on growing?
- Company keeps on taking debts and selling stocks to pump the business. Look for too high "cash form financial activities"
- Company has too few customers. What are her customers?

Good signs can be:
- Competitive advantages: brand, identity, monopoly,economy of scales, utilities, intengible assets (cocacola).
- Earnings are growing steadily (e.g 10% pretax) and are sustainable.
- Company must invest in R&D.

Management must be stable.
- If a company reprices, reissued or exchanges its stock options for insiders stay away.
- Normaly a company cancel worthless stock options for employees and exeutives. And replace for new one at advangateous prices. If their values has never allowed to go to zero they potential profit is always infinite. How can options encurage goods toword ship of corporate assets 


## Company key metrics

> This section contains data retrieved from the financial documents published by the companies (Income statement, Cash Flow, Balance sheet)

### Basic terms
- **Revenue** = Ammount of money the company make.
- **Net Income** = Earnings = Net Profits = Revenue−COGS−Operating and other expenses−Interests−Taxes
- **Operating Income** = Operative profit = Revenue - Operating expenses . Operative expenses are the day-to-day expenses to run the business and excludes items such as investments in other firms (non-operating income), taxes, and interest expenses. Also, nonrecurring items such as cash paid for a lawsuit settlement are not included.
- **COGS** = The cost of goods sold
- **EBIT** = Earnings before income tax
- **EBITDA** = Earnings before income tax, depreciation and ammortization.
- **Gross profit margin** = (REVENUEs - COGS)/REVENUEs
	
### From the Income statement:
- **Earnings x share (EPS)**: =((Net Income - preferred dividends) /shares outstanding). It is used as an indicator for company profitability. Higher number means company is more profitable. EPS diluted is often used, considering as the shares outstanging number the one calculated over the assumpion that all option,warranty etc. were converted immediatelly in stocks.
> EPS and Capital: EPS does not take into account the capitar required to generate the earnings (net income). To know the efficiency look at the ROE.

> EPS and Dividends: EPS does not turn into profit for shareholders. Part of the EPS is moved into the Dividends, part is retained back into the company.

> N.B EPS can be intentionally or unententionally faked by companies. Ofter to make this factor more realistic you would to use more precise formula: 
 EPS = (NI - PD +/- Extra Items +/- Discontinued operations)

> where Extra items = gain or losses related to one-time operation (e.g one factory burned (loss) or one land sell (gain) )

> where Discontinued operation = gain or loss related to specific operation valid in the period (e.g. part of the stores closed)

- **Net Income Ratio** : =*(Net Income/Revenue)*. It is also called Net Margin or Net Profit margin and it is expressed as percentage of the revenue. It describes how much of a given dollar in Revenue is translated into profit. Net profit margin is one of the most important indicators of a company's financial health.

> Limitation of Net Income Ratio : Net income ratio can be boosted by one time sale or other factors. It is used usually with Gross profit margin and operative profit margin

### From the Balance sheet:
- **Book value per share**: =*((Asset - Intangible assets - Liabilities)/Outstanding shares)*.  Also called "Net Book Value" or "Net asset value" , calculate what is the asset the shareholders would receive if the company were liquidated. When compared to market price it can tell you if a company is over or under priced.

- **Debt to equity**: = *Liabilities / Equities* . This metric compares the ammount of leverage the company is using, both in long and short term debt. In general the higher is the D/E the mor ethe company is a risky investment because it is financing it gowth with the debt. However this metric needs to be compared with others like the expected growth and the current ratio for a better view. Factors could be Current Ratio or Cash Ratio

- **Current Ratio**: *Short-term Assets/Short-term Liabilites* .  

- **Cash Ratio**: = *(Cash + Securities)/Short term Liabilites* . MEasure the short term liquidity or solvency.



## Current Ratios

> This section contains ratios calculated over the actual price of the stock

- **Price per earnings ratio (PE)**: = *Market Value/ EPS* . It gives what is the ammount of dollar you need to pay to expect a 1$ return one year later. HIgher PE than secotr average means comapny is overpriced or that high growth rates are expected in the future.Trailing PE gives you the current price over 12month period and is the most widely used.
The inverse of PE is giving you the expected earnings over one year period. To more accurate analysis use the PEG.

- **Price per book value ration (PBV)**: *Market Value/BV* . It gives you the ammount of dollar you need to pay to own 1$ in the company.

- **Price earnings to growth ratio (PEG)**:= *PE / EPS-growth* . PEG is used have a valueable metric to both take into account current price and EPS while using the expected growth on a specific time period. It gives a more specific view on the company than the PE itself. The lower PEG the company has the more this company could be undervalueated give its expected growth. Some may say the PEG > 1 indicate overvalued stocks, while PEG < 1 undervalued.

- **Divident Yield (DIV)**:= *annual dividends per share / price per share*.  It is showed as percentage and describe the ammount of money a company pays shareholders for owning a stock. It is an estimate of the dividend return for a stock investment. In general mature companies have higher returns than new comanies, but too high DIV Yelds sometimes shows reduced expected growth. Usually it is evaluated as TTM (trailing twelve month). Better indicator is Dividend Payout ratio.

- **Return on Equity** (ROE):

## Flexibility indicators

> This section contains indication to evaluate different types of flexibility

-**Investment Flexibility** :=*Revenues/Invested Capital* . This parameter describes the ammount of investments the company should make to have a given level of growth. This measure drops if the earnings drop. As en example telecom companies has low flexibility due to heavy infrastructure, while services or consulting busineses have high investment flexibility.

-**Operating Flexibility** :=*Gross profit Margin* . This parameter measures how much a change in revenues effects the operative income. The lower the revenues are the lower the operating flexibility is. In general losses effect businesses and the effect is more heavy when those businesses have lots of fixed costs. As an example airlines and industrial companies has low operating flexibility, while online retailing companies have high operating flexibility. Companies with higher gross profit margin have higher operating flexibility.

-**Financial Flexibility** :=*Net Debt/EBTDA* . This parameter measure how much a give change in the operating income results into a change into net income. If the company has more debts, there will be more expenses related to interests and it will reduce financial flexibility. If otherwise the company has more cash or income interests the financial flexibility will be higher.

-**Cash return Flexibility** :=**

## To be added:

- Beta:
- Liquidity indicators:
- Net Debt:


