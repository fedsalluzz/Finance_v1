import platform
import os
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['axes.grid'] = True
import numpy as np
import requests
from random import random
import matplotlib.dates as mdates
from matplotlib.ticker import PercentFormatter
import csv
import datetime

class Analyses:
	def __init__(self,ticker,period,api_key,document = None, title_data = None, statistic = None):
		self.ticker = ticker
		self.period = period
		self.api_key = api_key
		self.document = document
		self.title_data = title_data
		self.statistic =  statistic
		self.today = None


#A URL that returns an HTTP response in Json format is called API endpoint
#Financial_api_endpoint = 'https://financialmodelingprep.com/api/v3/'+api_method+'/'+symbol+'?apikey='+financial_api_key
#r = requests.get(Financial_api_endpoint)
#print(r.text)

############DEDICATED DATA FROM API #################
###########
##########
#########


	def Get_data_from_api(self, density = None, screener_list = None ):
		symbol = self.ticker
		api_key = self.api_key
		print('\n---- GET DATA FROM API starting...')
		api_endpoint_head ='https://financialmodelingprep.com/api/v3/'
		if (self.document == 'income_statement'):
			api_endpoint_body = api_endpoint_head+'income-statement/'
		elif (self.document == 'balance_sheet'):
			api_endpoint_body = api_endpoint_head+'balance-sheet-statement/'
		elif (self.document == 'cash_flow'):
			api_endpoint_body = api_endpoint_head+'cash-flow-statement/'
		elif (self.document == 'enterprise_value'):
			api_endpoint_body = api_endpoint_head+'enterprise-value/'
		elif (self.document == 'metrics'):
			api_endpoint_body = api_endpoint_head+'key-metrics/'
		elif (self.document == 'ratios'):
			api_endpoint_body = api_endpoint_head+'ratios/'
		elif (self.document =='stock-screener'):
			api_endpoint_body = api_endpoint_head+'stock-screener/'
			marketCapLowerThan= screener_list[1]
			marketCapMoreThan=screener_list[0]
			betaMoreThan=screener_list[2]
			betaLowerThan=screener_list[3]
			sector=screener_list[6]
			industry=screener_list[7]
			dividendMoreThan=screener_list[4]
			dividendLowerThan=screener_list[5]
			exchange=screener_list[8]
			api_endpoint =api_endpoint_body+'?marketCapMoreThan='+marketCapMoreThan+'&marketCapLowerThan='+marketCapLowerThan+'&betaMoreThan='+betaMoreThan+'&betaLowerThan='+betaLowerThan+'&sector='+sector+'&exchange='+exchange+'&industry'+industry+'&dividendLowerThan='+dividendLowerThan+'&dividendMoreThan='+dividendMoreThan+'&limit=100&apikey='+api_key
		elif (self.document =='quote'):
			api_endpoint_body = api_endpoint_head+'quote/'
		elif (self.document =='profile'):
			api_endpoint_body = api_endpoint_head+'profile/'
		else:
			error
		if (density == 'quarter'):
			api_endpoint =api_endpoint_body+symbol+'?period=quarter&apikey='+api_key
		elif (self.document == 'stock-screener'):
			api_endpoint =api_endpoint_body+'?marketCapMoreThan='+marketCapMoreThan+'&marketCapLowerThan='+marketCapLowerThan+'&betaMoreThan='+betaMoreThan+'&betaLowerThan='+betaLowerThan+'&sector='+sector+'&exchange='+exchange+'&industry'+industry+'&dividendLowerThan'+dividendLowerThan+'&dividendMoreThan='+dividendMoreThan+'&limit=100&apikey='+api_key
		else:
			api_endpoint =api_endpoint_body+symbol+'?apikey='+api_key
		try:
			r = requests.get(api_endpoint)
			print('-- API ENDPOINT IS : '+api_endpoint)
			print('-- GET '+self.document+' from endpoint' )
		except:
			print('**** EXCEPTION in Get_data_from_api :: message from API endopoint: '+r.text)
		return r.text



############GENERIC DATA FUNCTION #################
###########
##########
#########
	def Get_document_for(self,single_ticker, data_1, data_2, document ):
		print('\n---- Starting the Get_document_for function...')
		self.document = document
		self.ticker = single_ticker
		print('---- Requested document is '+self.document+' for'+self.ticker)
		json_data = self.Get_data_from_api('quarter') #it is a string json format
		load = json.loads(json_data) #list
		df = pd.DataFrame(load)
		self.Print_on_file(df, single_ticker, self.document )
		print('---- '+document+' Loaded , Dataframe loaded')
		date = df['date'].to_numpy()
		df_1 = df[data_1].to_numpy()
		df_2 = df[data_2].to_numpy()
		date_order,df_1_order,df_2_order = self.Time_and_statistic_sorter(date,df_1,df_2)
		#self.title_data = ['Earning Per Share','netIncomeRatio']
		print('---- Closing the Get_document_for...')
		return date_order.tolist(), df_1_order.tolist(), df_2_order.tolist()


	def Get_quote_for(self,single_ticker):
		print('\n---- Starting the Get_quote_for function...')
		self.document = 'quote'
		self.ticker = single_ticker
		print('---- Requested document is '+self.document+' for '+self.ticker)
		json_data = self.Get_data_from_api() #it is a string json format
		load = json.loads(json_data) #list
		df = pd.DataFrame(load)
		#print(df)
		self.Print_on_file(df, single_ticker, self.document )
		print('---- quote Loaded , Dataframe loaded')
		timestamp = df['timestamp'].to_numpy()
		price = df['price'].to_numpy()
		priceAvg50 = df['priceAvg50'].to_numpy()
		priceAvg200 = df['priceAvg200'].to_numpy()
		eps = df['eps'].to_numpy()
		sharesOutstanding =df['sharesOutstanding'].to_numpy()
		marketCap =df[ 'marketCap'].to_numpy()
		#self.title_data = ['Earning Per Share','netIncomeRatio']
		print(price)
		print('---- Closing the Get_quote_for...')
		price_str = str(price[0])
		priceAvg50_str = str(priceAvg50[0])
		priceAvg200_str = str(priceAvg200[0])
		eps_str = str(eps[0])
		sharesOutstanding_str =str(sharesOutstanding[0])
		marketCap_str = str(marketCap[0])
		dt = datetime.datetime.fromtimestamp(timestamp[0])
		print('DATE TIME IS : '+str(dt))
		self.today = str(dt)
		return price_str[:6],priceAvg50_str[:6],priceAvg200_str[:6],eps_str[:6],sharesOutstanding_str[:6], marketCap_str[:6]

	

#################
### Take the RATIOS for Latest Report
	def Ratios(self):
		print('\n---- Starting the Ratios function...')
		self.document = 'ratios'
		print('---- Requested Ratios. Selected document is '+self.document+' for'+self.ticker)
		ratios_data = self.Get_data_from_api('quarter') #it is a string json format
		load = json.loads(ratios_data) #list
		#print('Ratios json loaded')
		df = pd.DataFrame(load)
		#print(df)
		self.Print_on_file(df, self.ticker, self.document )
		print('---- Ratios Loaded , Dataframe loaded')
		#print(df)
		x_ax = df['date'].to_numpy()
		y1_ax = df['currentRatio'].to_numpy()
		y2_ax = df['quickRatio'].to_numpy()
		y3_ax = df['cashRatio'].to_numpy()
		y4_ax = df['grossProfitMargin'].to_numpy()
		y5_ax = df['operatingProfitMargin'].to_numpy()
		y6_ax = df['netProfitMargin'].to_numpy()
		y7_ax = df['returnOnAssets'].to_numpy()
		y8_ax = df['returnOnEquity'].to_numpy()
		y9_ax = df['debtRatio'].to_numpy()
		y10_ax = df['debtEquityRatio'].to_numpy()
		y11_ax = df['operatingCashFlowPerShare'].to_numpy()
		y12_ax = df['freeCashFlowPerShare'].to_numpy()
		print('-- Latest data is date on: '+str(x_ax[0]))
		self.today = str(x_ax[0])
		currentRatio = str(y1_ax[0])
		quickRatio = str(y2_ax[0])
		cashRatio = str(y3_ax[0])
		grossProfitMargin = str(y4_ax[0])
		operatingProfitMargin = str(y5_ax[0])
		netProfitMargin = str(y6_ax[0])
		returnOnAssets = str(y7_ax[0]) 
		returnOnEquity= str(y8_ax[0])
		debtRatio= str(y9_ax[0])
		debtEquityRatio= str(y10_ax[0]) 
		operatingCashFlowPerShare= str(y11_ax[0]) 
		freeCashFlowPerShare= str(y12_ax[0]) 
		return  currentRatio[:5], quickRatio[:5], cashRatio[:5],grossProfitMargin[:5],operatingProfitMargin[:5], netProfitMargin[:5], returnOnAssets[:5], returnOnEquity[:5], debtRatio[:5], debtEquityRatio[:5], operatingCashFlowPerShare[:5], freeCashFlowPerShare[:5] 



#################
### Take the METRICS for Latest Report
	def Metrics(self):
		print('\n---- Starting the Ratios function...')
		self.document = 'metrics'
		print('---- Requested Ratios. Selected document is '+self.document+' for'+self.ticker)
		ratios_data = self.Get_data_from_api('quarter') #it is a string json format
		load = json.loads(ratios_data) #list
		#print('Ratios json loaded')
		df = pd.DataFrame(load)
		#print(df)
		self.Print_on_file(df, self.ticker, self.document )
		print('---- Ratios Loaded , Dataframe loaded')
		#print(df)
		y1_ax = df['bookValuePerShare'].to_numpy()
		y2_ax = df['debtToAssets'].to_numpy()
		y3_ax = df['debtToEquity'].to_numpy()
		y4_ax = df['enterpriseValue'].to_numpy()
		y5_ax = df['enterpriseValueOverEBITDA'].to_numpy()
		y6_ax = df['freeCashFlowPerShare'].to_numpy()
		y7_ax = df['researchAndDdevelopementToRevenue'].to_numpy()
		y8_ax = df['roe'].to_numpy()
		y9_ax = df['roic'].to_numpy()
		bookValuePerShare= str(y1_ax[0])
		debtToAssets= str(y2_ax[0])
		debtToEquity= str(y3_ax[0])
		enterpriseValue= str(y4_ax[0])
		enterpriseValueOverEBITDA= str(y5_ax[0])
		freeCashFlowPerShare= str(y6_ax[0])
		researchAndDdevelopementToRevenue= str(y7_ax[0]) 
		roe= str(y8_ax[0])
		roic= str(y9_ax[0])
		return bookValuePerShare [:5], debtToAssets[:5], debtToEquity[:5],enterpriseValue[:5],enterpriseValueOverEBITDA[:5], freeCashFlowPerShare[:5], researchAndDdevelopementToRevenue[:5],roe[:5], roic[:5]



#################
### Take the PROFILE for Latest Report
	def Profile(self):
		print('\n---- Starting the Profile function...')
		self.document = 'profile'
		print('---- Requested Profile. Selected document is '+self.document+' for'+self.ticker)
		ratios_data = self.Get_data_from_api() #it is a string json format
		load = json.loads(ratios_data) #list
		#print('Ratios json loaded')
		df = pd.DataFrame(load)
		#print(df)
		self.Print_on_file(df, self.ticker, self.document )
		print('---- Profile Loaded , Dataframe loaded')
		#print(df)
		y1_ax = df['beta'].to_numpy()
		y2_ax = df['volAvg'].to_numpy()
		y3_ax = df['lastDiv'].to_numpy()
		y4_ax = df['dcf'].to_numpy()
		y5_ax = df['ipoDate'].to_numpy()
		y6_ax = df['industry'].to_numpy()
		y7_ax = df['sector'].to_numpy()
		beta= str(y1_ax[0])
		volAvg= str(y2_ax[0])
		lastDiv= str(y3_ax[0])
		dcf= str(y4_ax[0])
		ipoDate= str(y5_ax[0])
		industry= str(y6_ax[0])
		sector= str(y7_ax[0]) 
		return beta[:5],volAvg[:5],lastDiv[:5],dcf[:5],ipoDate[:4], industry,sector



	def Stock_screener(self, criteria_list):
		print('\n---- Starting the Stock screener function...')
		self.document = 'stock-screener'
		print('---- Requested strock screen...')
		ratios_data = self.Get_data_from_api(screener_list = criteria_list) #it is a string json format
		load = json.loads(ratios_data) #list
		print('Printing criteria list')
		print(criteria_list)
		df = pd.DataFrame(load)
		#print(df)
		criteria = ''
		criteria_heathers = ['marketCapMoreThan','marketCapLowerThan','betaMoreThan','betaLowerThan','dividendMoreThan','dividendLowerThan','sector','industry','exchange']
		length = len(criteria_list)
		for i in range(length):
			if (criteria_list[i] != ''):
				criteria = criteria+criteria_heathers[i]+'='+criteria_list[i]+'&'
		print(criteria)
		self.ticker = criteria
		self.Print_on_file(df, self.ticker, self.document )
		print('---- Printed on file --------')
		return 

### Take the PE, PBV, PEG for TODAY
# Sort data from oldest to newest
#
	def Time_and_statistic_sorter(self,x_ax,y1_ax,y2_ax = None, y3_ax = None):
		if (self.period == "MAX"):
			pass
		else:
			timespan = x_ax[:int(self.period)*4] #quarter data
			y1_reduced_data = y1_ax[:int(self.period)*4] #quarter data
			y2_reduced_data = y2_ax[:int(self.period)*4] #quarter data
		x_ax_order = timespan[::-1]
		y1_ax_order = y1_reduced_data[::-1] 
		y2_ax_order = y2_reduced_data[::-1]
		print('-- Selected data for '+self.period+' years')
		return (x_ax_order,y1_ax_order,y2_ax_order)
	
	
	def Random_color(self):
		r = random()
		b = random()
		g = random()
		color = (r, g, b)
		return color

#
# Save dataframe on .csv file
#

	def Print_on_file(self,dataframe, ticker, document ):
		dataframe.to_csv(r'saved_data/'+document+'/'+ticker+'_'+document+'.csv', index = False)
		return

	


#
# Plot statitics for 2x1 or 2x2 suplots for one ticker only.
#
	def Plot_statistic(self,tickers_dict, tickers_dict_2 = None, ticker_gui_list = None ):
		color = ['b','g','r','c','m','y','k']
		print('\n---- Trying to plot statistics ')
		ticker_list = self.ticker.split(',')
		if (len(ticker_list) == 1):
			print('--Plotting statics for: '+str(ticker_list))
			if (len(self.title_data) == 2):
				#self.set_draw_settings()
				fig, axs = plt.subplots(nrows=2,ncols=1, num=str(ticker_list)+' retrieved data')
				for ticker in ticker_list:
					#print(str(ticker))
					#print(tickers_dict)
					for i in range(0,2):
						#color = self.Random_color()
						t = tickers_dict[str(ticker)]['x'];
						y = tickers_dict[str(ticker)]['y'+str(i+1)]
						y_mean = [np.mean(y)]*len(t)
						axs[i].plot(t,y,c=color[i+j],label = ticker)
						axs[i].plot(t,y_mean,color='red',label = ticker,linestyle='--')
						axs[i].set_title(str(self.title_data[i]))
			else: #All four drawings
				ticker = ticker_list[0]
				#self.set_draw_settings()
				fig, axs = plt.subplots(nrows=2,ncols=2, num=str(ticker)+' retrieved data')
				for i in range(0,2):
					for j in range(0,2):
						color = self.Random_color()
						t = tickers_dict[str(ticker)]['x'];
						y1 = tickers_dict[str(ticker)]['y'+str(j+1)]
						y1_mean = [np.mean(y1)]*len(t)
						y2 = tickers_dict_2[str(ticker)]['y'+str(j+1)]
						y2_mean = [np.mean(y2)]*len(t)
						#print(str(int(str(i)+str(j), base= 2)))
						if ( int(str(i)+str(j),2) < 2 ):
							axs[i,j].plot(t,y1,c=color)
							axs[i,j].plot(t,y1_mean,c='red',label = ticker,linestyle='--')
							#print('y'+str(j+1))
							axs[i,j].set_title(str(self.title_data[int(str(i)+str(j), base= 2)]))
						else:
							axs[i,j].plot(t,y2,c=color)
							axs[i,j].plot(t,y2_mean,c='red',label = ticker,linestyle='--')
							axs[i,j].set_title(str(self.title_data[int(str(i)+str(j), base= 2)]))
		else:
			print('-- Use the Multiple_plots function for '+str(ticker_list))
		fig.autofmt_xdate()
		print(' -- --- Plotting the graphs over time')
		plt.show()
		return 

	


	def Multiple_plots(self,ticker_list, tickers_dict, tickers_dict_2, button ):
		print('\n---- TRYING MULTI PLOT OPERATION '+str(ticker_list))
		colors = ['b','g','r','c','m','y','k']
		self.set_draw_settings()
		fig, axs = plt.subplots(nrows=2,ncols=2, num=str(ticker_list)+' retrieved data with ' +button)
		print(self.statistic)
		if (self.statistic == 'log'):
			print('yes')
		myFmt = mdates.DateFormatter('%Y-%m-%d')
		for index,ticker in enumerate(ticker_list):
			color = colors[index]
			#print('((((( THE COLOR IS ...'+ str(color))
			for i in range(0,2):
				for j in range(0,2):
					axs[i,j].xaxis.set_major_formatter(myFmt)
					t1_list = tickers_dict[str(ticker)]['x'];
					y1 = tickers_dict[str(ticker)]['y'+str(j+1)]
					#print('LIST TYPE IS: '+str(type(y1)))
					#print('ELEMENT OF LIST Y1[0] is'+str(y1[0])+' of type '+str(type(y1[0])))
					y1_mean = [np.mean(y1)]*len(t1_list)
					t2_list = tickers_dict_2[str(ticker)]['x'];
					y2 = tickers_dict_2[str(ticker)]['y'+str(j+1)]
					y2_mean = [np.mean(y2)]*len(t2_list)
					#print(str(y1))
					#print(str(y2))
					t1 =pd.to_datetime(pd.Series(t1_list), format='%Y-%m-%d')
					t2 =pd.to_datetime(pd.Series(t2_list), format='%Y-%m-%d')
					if (self.statistic == 'log'):
						axs[i,j].set_yscale('log')
					elif (self.statistic == '%'):
						axs[i,j].yaxis.set_major_formatter(PercentFormatter())
						#for u in range(0,len(y1)):
						#	print(u)
						#	y1[u] = y1[u]*100
						#	y2[u] = y2[u]*100
					#print(str(int(str(i)+str(j), base= 2)))
					if ( int(str(i)+str(j),2) < 2 ): #i primi due grafici sono in %
						if (self.statistic == '%'):
							for u in range(0,len(y1)):
								#print(u)
								y1[u] = y1[u]*100
								y2[u] = y2[u]*100
						axs[i,j].plot(t1,y1,c=color)
						axs[i,j].plot(t1,y1_mean,c=color,label = ticker,linestyle='--')
						axs[i,j].set_title(str(self.title_data[int(str(i)+str(j), base= 2)]))
					else:
						axs[i,j].plot(t2,y2,c=color)
						axs[i,j].plot(t2,y2_mean,c=color,label = ticker,linestyle='--')
						axs[i,j].set_title(str(self.title_data[int(str(i)+str(j), base= 2)]))
					leg = axs[i,j].legend();
					fig.autofmt_xdate()
		print('--- Plotting the multiple graphs over time')
		plt.show()
		return 
 


	def set_draw_settings(self):
		params = {"figure.facecolor": "#cad9e1",
		"axes.facecolor": "#cad9e1",
		"axes.grid" : True,
		"axes.grid.axis" : "y",
		"grid.color"	: "#ffffff",
		"grid.linewidth": 2,
		"axes.spines.left" : False,
		"axes.spines.right" : False,
		"axes.spines.top" : False,
		"ytick.major.size": 0,	 
		"ytick.minor.size": 0,
		"xtick.direction" : "in",
		"axes.titlesize"	  : "small",
		"xtick.major.size" : 7,
		"xtick.color"	  : "#191919",
		"axes.edgecolor"	:"#191919",
		"axes.prop_cycle" : plt.cycler('color',['#006767', '#ff7f0e', '#2ca02c', '#d62728','#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf'])}
		plt.rcParams.update(params)



def main():
	pass




if __name__ == '__main__':
	main()


