import platform
import os
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
plt.rcParams['axes.grid'] = True
import numpy as np
import requests
from random import random
import matplotlib.dates as mdates



class Analyses:
	def __init__(self,ticker,period,api_key,document = None, title_data = None, statistic = None):
		self.ticker = ticker
		self.period = period
		self.api_key = api_key
		self.document = document
		self.title_data = title_data
		self.statistic =  statistic


#A URL that returns an HTTP response in Json format is called API endpoint
#Financial_api_endpoint = 'https://financialmodelingprep.com/api/v3/'+api_method+'/'+symbol+'?apikey='+financial_api_key
#r = requests.get(Financial_api_endpoint)
#print(r.text)

#
# Retrieve data from API endpoint
#
#de
	
	def Get_data_from_api(self, density = None ):
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
		else:
			error
		if (density == 'quarter'):
			api_endpoint =api_endpoint_body+symbol+'?period=quarter&apikey='+api_key
		else:
			api_endpoint =api_endpoint_body+symbol+'?apikey='+api_key
		try:
			r = requests.get(api_endpoint)
			print('-- API ENDPOINT IS : '+api_endpoint)
			print('-- GET '+self.document+' from endpoint' )
		except:
			print('**** EXCEPTION in Get_data_from_api :: message from API endopoint: '+r.text)
		return r.text



	#
	# Sort data from oldest to newest
	#
	def Time_and_statistic_sorter(self,x_ax,y1_ax,y2_ax = None):
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
	# Create dataframe with Income_statement data from income_statement (x,y1 and y2 axis)
	#
	
	
	def Income_statement(self,single_ticker):
		print('\n---- Starting the Income_statement function...')
		self.document = 'income_statement'
		self.statistic = 'Income_statement'
		self.ticker = single_ticker
		print('-- Requested document is '+self.document+' for'+self.ticker)
		eps_data = self.Get_data_from_api('quarter') #it is a string json format
		#print(eps_data)
		load = json.loads(eps_data) #list
		#print('I m in')
		df = pd.DataFrame(load)
		print('-- Income Statement Loaded , Dataframe loaded, Selecting Income_statement and Income_statement diluted')
		date = df['date'].to_numpy()
		eps = df['eps'].to_numpy()
		netIncomeRatio = df['netIncomeRatio'].to_numpy()
		date_order,eps_order,netIncomeRatio_order = self.Time_and_statistic_sorter(date,eps,netIncomeRatio)
		self.title_data = ['Earning Per Share','netIncomeRatio']
		#print(x_ax_order)
		print('--- Closing the Income_statement function...')
		return date_order.tolist(), eps_order.tolist(), netIncomeRatio_order.tolist()  
	
	#
	# Create dataframe with book vlue and debt per earning data from metrics (x,y1 and y2 axis)
	#
	def Company_key_metrics(self,single_ticker):
		print('\n---- Starting the Company_key_metrics function...')
		self.document = 'metrics'
		self.statistic = 'Company_key_metrics'
		self.ticker = single_ticker
		print('-- Requested document is '+self.document+' for'+self.ticker)
		bv_data = self.Get_data_from_api('quarter') #it is a string json format
		load = json.loads(bv_data) #list
		df = pd.DataFrame(load)
		#print(bv_data)
		print('-- Income Statement Loaded , Dataframe loaded, Selecting BV and Debt')
		date = df['date'].to_numpy()
		bookValuePerShare = df['bookValuePerShare'].to_numpy()
		debtToEquity = df['debtToEquity'].to_numpy()
		date_order,bookValuePerShare_order,debtToEquity_order = self.Time_and_statistic_sorter(date,bookValuePerShare,debtToEquity)
		self.title_data = ['bookValuePerShare','debtToEquity']
		#print(date)
		print('--- Closing the Company_key_metrics function...')
		return  date_order.tolist(), bookValuePerShare_order.tolist(), debtToEquity_order.tolist()
	
	


	#
	# Create dataframe with book vlue and debt per earning data from metrics (x,y1 and y2 axis)
	#
	def Current_and_Cash_ratio(self,single_ticker):
		print('\n---- Starting the Current_and_Cash_ratio function...')
		self.document = 'metrics'
		self.statistic = 'Current_and_Cash_ratio'
		self.ticker = single_ticker
		print('-- Requested document is '+self.document+' for'+self.ticker)
		bv_data = self.Get_data_from_api('quarter') #it is a string json format
		load = json.loads(bv_data) #list
		df = pd.DataFrame(load)
		#print(bv_data)
		print('-- Current_and_Cash_ratio Loaded , Dataframe loaded')
		date = df['date'].to_numpy()
		Current_ratio = df['currentRatio'].to_numpy()
		Debt_to_Assets = df['debtToAssets'].to_numpy()
		date_order,Current_ratio_order,Debt_to_Assets_order = self.Time_and_statistic_sorter(date,Current_ratio,Debt_to_Assets)
		self.title_data = ['currentRatio','debtToAssets']
		#print(date)
		print('--- Closing the Current_and_Cash_ratio function...')
		return  date_order.tolist(), Current_ratio_order.tolist(), Debt_to_Assets_order.tolist()





#################
### Take the PE, PBV, PEG for TODAY
	def Ratios(self):
		print('\n---- Starting the Ratios function...')
		self.document = 'ratios'
		print('-- Requested Ratios. Selected document is '+self.document+' for'+self.ticker)
		ratios_data = self.Get_data_from_api('quarter') #it is a string json format
		load = json.loads(ratios_data) #list
		print('Ratios json loaded')
		df = pd.DataFrame(load)
		print('-- Income Statement Loaded , Dataframe loaded, Selecting Ratios')
		#print(df)
		x_ax = df['date'].to_numpy()
		y1_ax = df['priceBookValueRatio'].to_numpy()
		y2_ax = df['priceEarningsRatio'].to_numpy()
		y3_ax = df['priceEarningsToGrowthRatio'].to_numpy()
		y4_ax = df['dividendYield'].to_numpy()
		y5_ax = df['returnOnEquity'].to_numpy()
		print('-- Latest data is date on: '+str(x_ax[0]))
		pe = str(y1_ax[0])
		pbv = str(y2_ax[0])
		peg = str(y3_ax[0])
		div = str(y4_ax[0])
		roe = str(y5_ax[0])
		print('-- PE: '+str(y1_ax[0]))
		print('-- PBV: '+str(y2_ax[0]))
		print('-- PEG: '+str(y3_ax[0]))
		print('-- DividentYeld: '+str(y4_ax[0]))
		print('-- ROE: '+str(y5_ax[0]))
		#self.title_data = ['Income_statement','netIncomeRatio']
		#print(x_ax_order)
		print('--- Closing the RATIOS function...')
		return  pe, pbv, peg,div,roe  



#
# Plot wanted statitics for 2x1 or 2x2 suplots
#
	def Plot_statistic(self,tickers_dict, tickers_dict_2 = None, ticker_gui_list = None ):
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
						color = self.Random_color()
						t = tickers_dict[str(ticker)]['x'];
						y = tickers_dict[str(ticker)]['y'+str(i+1)]
						y_mean = [np.mean(y)]*len(t)
						axs[i].plot(t,y,c=color,label = ticker)
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
		print('-- TRYING MULTI PLOT OPERATION '+str(ticker_list))
		self.set_draw_settings()
#		if (button == 'Analyze'):
#			plt = plt1
#		else:
#			plt = plt2
		fig, axs = plt.subplots(nrows=2,ncols=2, num=str(ticker_list)+' retrieved data with ' +button)
		#print(tickers_dict)
		myFmt = mdates.DateFormatter('%Y-%m-%d')
		for ticker in ticker_list:
			color = self.Random_color()
			print('((((( THE COLOR IS ...'+ str(color))
			for i in range(0,2):
				for j in range(0,2):
					axs[i,j].xaxis.set_major_formatter(myFmt)
					t1_list = tickers_dict[str(ticker)]['x'];
					y1 = tickers_dict[str(ticker)]['y'+str(j+1)]
					y1_mean = [np.mean(y1)]*len(t1_list)
					t2_list = tickers_dict_2[str(ticker)]['x'];
					y2 = tickers_dict_2[str(ticker)]['y'+str(j+1)]
					y2_mean = [np.mean(y2)]*len(t2_list)
					t1 =pd.to_datetime(pd.Series(t1_list), format='%Y-%m-%d')
					t2 =pd.to_datetime(pd.Series(t2_list), format='%Y-%m-%d')
					#print(str(int(str(i)+str(j), base= 2)))
					if ( int(str(i)+str(j),2) < 2 ):
						axs[i,j].plot(t1,y1,c=color)
						axs[i,j].plot(t1,y1_mean,c=color,label = ticker,linestyle='--')
						#print('y'+str(j+1))
						axs[i,j].set_title(str(self.title_data[int(str(i)+str(j), base= 2)]))
					else:
						axs[i,j].plot(t2,y2,c=color)
						axs[i,j].plot(t2,y2_mean,c=color,label = ticker,linestyle='--')
						axs[i,j].set_title(str(self.title_data[int(str(i)+str(j), base= 2)]))
					leg = axs[i,j].legend();
					fig.autofmt_xdate()
					#print('........................y1 \n')
					#print(t1)
					#print('........................t1 \n')
					#print(y1)
					#print('........................t2 \n')
					#print(t2)
					#print('........................y2 \n')
					#print(y2)
		print(' -- --- Plotting the graphs over time')
		plt.show()
		return 
 





	def set_draw_settings(self):
		params = {"figure.facecolor": "#cad9e1",
		"axes.facecolor": "#cad9e1",
		"axes.grid" : True,
		"axes.grid.axis" : "y",
		"grid.color"    : "#ffffff",
		"grid.linewidth": 2,
		"axes.spines.left" : False,
		"axes.spines.right" : False,
		"axes.spines.top" : False,
		"ytick.major.size": 0,     
		"ytick.minor.size": 0,
		"xtick.direction" : "in",
		"xtick.major.size" : 7,
		"xtick.color"      : "#191919",
		"axes.edgecolor"    :"#191919",
		"axes.prop_cycle" : plt.cycler('color',['#006767', '#ff7f0e', '#2ca02c', '#d62728','#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf'])}
		plt.rcParams.update(params)



def main():
	pass
	##tickers = "AAPL,JNJ"
	#eps_analysis = Analyses(ticker='RCL',period = '1',api_key = 'c69c0e1c9f3b70a951441dc376b6d400', statistic = 'ESP')
	#print(eps_analysis.ticker)
	#print(eps_analysis.period)
	#print(eps_analysis.api_key)
	#print(eps_analysis.document)
	#eps_analysis.Ratios()



if __name__ == '__main__':
	main()


