########################################################################################
# Process the information taken from API https://financialmodelingprep.com/developer/docs/
##########################################################################################

import requests
import platform
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


print('Your pithon version is: ' + platform.python_version())

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
	print('-- GET '+document+' from endpoint' )
	
	return r.text

def Plot_statistic(json_data, indicators ):
	load = json.loads(financial_data) #list
	df = pd.DataFrame(load)
	print('-- Dataframe loaded')
	x_ax = df['date'].to_numpy()
	y1_ax = df[indicators[0]].to_numpy()
	y2_ax = df[indicators[1]].to_numpy()
	x_ax_order = x_ax[::-1]
	y1_ax_order = y1_ax[::-1] 
	y2_ax_order = y2_ax[::-1]
	print('-- Dataframe reordered')
	#plot the graphix
	fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1)
	ax1.plot(x_ax_order,y1_ax_order, 'tab:green')
	ax1.set_title(indicators[0])
	ax2.plot(x_ax_order,y2_ax_order)  
	ax2.set_title(indicators[1])
	ax1.grid(True)
	ax2.grid(True)
	fig.autofmt_xdate()
	print('Plotting the selected graph')
	#plt.show()
	return plt.show() 


#################################################
#### MAIN #######################################
################################################

financial_api_key = 'c69c0e1c9f3b70a951441dc376b6d400'
document = 'metrics'
indicators = ['debtToEquity','peRatio']

financial_data = Get_data_from_api(document,'AAPL','quarter', financial_api_key) #it is a string json format

Plot_statistic(financial_data, indicators )

#load = json.loads(financial_data) #list
#df = pd.DataFrame(load)
#print(df)
#
#fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1)
#
#print(type(df['date'].to_numpy()))
#
#x_ax = df['date'].to_numpy()
#y1_ax = df['debtToEquity'].to_numpy()
#y2_ax = df['peRatio'].to_numpy()
#
#x_ax = x_ax[::-1]
#y1_ax = y1_ax[::-1]
#y2_ax = y2_ax[::-1]
#
#
#ax1.plot(x_ax,y1_ax, 'tab:green')
#ax1.set_title('debtToEquity')
#ax2.plot(x_ax,y2_ax)  
#ax2.set_title('peRatio')
#ax1.grid(True)
#ax2.grid(True)
#
#fig.autofmt_xdate()
##ax3.scatter(x = df['date'] , y = df['debtToEquity']) 
##ax4.scatter(x = df['date'] , y = df['peRatio']) 
#
##df.plot(x = 'date' , y = 'debtToEquity' )
##df.plot(x = 'date' , y = 'peRatio' )
#plt.show()
#
#
