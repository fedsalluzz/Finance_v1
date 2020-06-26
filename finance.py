########################################################################################
# Process the information taken from API https://financialmodelingprep.com/developer/docs/
##########################################################################################

import requests


#A URL that returns an HTTP response in Json format is called API endpoint
#Financial_api_endpoint = 'https://financialmodelingprep.com/api/v3/'+api_method+'/'+symbol+'?apikey='+financial_api_key
#r = requests.get(Financial_api_endpoint)
#print(r.text)


def Get_data_from_api(document,symbol,period,api_key):
	api_endpoint_head ='https://financialmodelingprep.com/api/v3/'
	if (document == 'income_statement'):
		api_endpoint_body = api_endpoint_head+'income-statement/'
	elif (document == 'balance_sheet'):
		api_endpoint_body = api_endpoint_head+'balance-sheet-statement/'
	elif (document == 'cash_flow'):
		api_endpoint_body = api_endpoint_head+'cash-flow-statement/'
	elif (document == 'enterprise_value'):
		api_endpoint_body = api_endpoint_head+'enterprise-value/'
	elif (document == 'metrics'):
		api_endpoint_body = api_endpoint_head+'key-metrics/'
	else:
		error
	
	if (period == 'quarter'):
		api_endpoint =api_endpoint_body+symbol+'?period=quarter&apikey='+api_key
	else:
		api_endpoint =api_endpoint_body+symbol+'?apikey='+api_key

	r = requests.get(api_endpoint)
	print('-- API ENDPOINT IS : '+api_endpoint)
	
	return r.text


financial_api_key = 'c69c0e1c9f3b70a951441dc376b6d400'
document = 'metrics'
print(Get_data_from_api(document,'AAPL','0', financial_api_key))

