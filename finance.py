import requests

financial_api_key = 'c69c0e1c9f3b70a951441dc376b6d400'

api_method='profile'
symbol = 'AAPL'

#A URL that returns an HTTP response in Json format is called API endpoint
#Financial_api_endpoint = 'https://financialmodelingprep.com/api/v3/'+api_method+'/'+symbol+'?apikey='+financial_api_key
#r = requests.get(Financial_api_endpoint)
#print(r.text)


def Financial_statement(document,symbol,period,api_key):
	api_endpoint_head ='https://financialmodelingprep.com/api/v3/'+document
	if (document == 'income_statement'):
		api_endpoint_head ='https://financialmodelingprep.com/api/v3/income-statement/'
		if (period == 'quarter'):
			api_endpoint =api_endpoint_head+symbol+'?period=quarter&apikey='+api_key
		else:
			api_endpoint =api_endpoint_head+symbol+'?apikey='+api_key
        elif (document == 'balance_sheet'):
		api_endpoint_head ='https://financialmodelingprep.com/api/v3/balance-sheet-statement/'

	elif (document == 'cash_flow'):
		api_endpoint_head ='https://financialmodelingprep.com/api/v3/cash-flow-statement/'

	r = requests.get(api_endpoint)
	print('-- API ENDPOINT IS : '+api_endpoint)
	return r.text

#print(Income_statement('AAPL','0', financial_api_key))

