import platform
import os
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['axes.grid'] = True
import numpy as np
import requests


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
	def Get_data_from_api(self, density = None):
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

	def Get_list(self):
		text = self.Get_data_from_api('quarter') #it is a string json format
		#print(text)
		load = json.loads(text) #list
		#print('I m in')
		df = pd.DataFrame(load)
		print('\n-- Single data function Dataframe loaded, Selecting '+self.statistic)
		x_ax = df['date'].to_numpy()
		y_ax = df[self.statistic].to_numpy()
		x_ax_order,y_ax_order = self.Time_and_statistic_sorter(x_ax,y1_ax)		
		self.title_data = [self.statistic]
		#print(x_ax_order)
		print('--- Closing the Single Data function...')
		return x_ax_order.tolist(), y_ax_order.tolist()
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
	
	#
	# Create dataframe with EPS data from income_statement (x,y1 and y2 axis)
	#
	
	
	def EPS(self):
		print('\n---- Starting the EPS function...')
		self.document = 'income_statement'
		self.statistic = 'ESP'
		print('-- Requested document is '+self.document+' for'+self.ticker)
		eps_data = self.Get_data_from_api('quarter') #it is a string json format
		#print(eps_data)
		load = json.loads(eps_data) #list
		#print('I m in')
		df = pd.DataFrame(load)
		print('-- Income Statement Loaded , Dataframe loaded, Selecting EPS and EPS diluted')
		x_ax = df['date'].to_numpy()
		y1_ax = df['eps'].to_numpy()
		y2_ax = df['netIncomeRatio'].to_numpy()
		x_ax_order,y1_ax_order,y2_ax_order = self.Time_and_statistic_sorter(x_ax,y1_ax,y2_ax)
		self.title_data = ['EPS','netIncomeRatio']
		#print(x_ax_order)
		print('--- Closing the EPS function...')
		return x_ax_order.tolist(), y1_ax_order.tolist(), y2_ax_order.tolist()  
	
	#
	# Create dataframe with book vlue and debt per earning data from metrics (x,y1 and y2 axis)
	#
	def BV_DEBT(self):
		print('\n---- Starting the BV_DEBT function...')
		self.document = 'metrics'
		self.statistic = 'BV_DEBT'
		print('-- Requested document is '+self.document+' for'+self.ticker)
		bv_data = self.Get_data_from_api('quarter') #it is a string json format
		load = json.loads(bv_data) #list
		try:
			df = pd.DataFrame(load)
			#print(bv_data)
			print('-- Income Statement Loaded , Dataframe loaded, Selecting BV and Debt')
			x_ax = df['date'].to_numpy()
			y1_ax = df['bookValuePerShare'].to_numpy()
			y2_ax = df['debtToEquity'].to_numpy()
			x_ax_order,y1_ax_order,y2_ax_order = self.Time_and_statistic_sorter(x_ax,y1_ax,y2_ax)
			self.title_data = ['bookValuePerShare','debtToEquity']
			print(x_ax_order)
			print('--- Closing the BD_DEBT function...')
		except:
			print('**** EXCEPTION in BV_DEBT function :: message from API endopoint: '+eps_data)
			exit
	
		return  x_ax_order.tolist(), y1_ax_order.tolist(), y2_ax_order.tolist()
	
	
	def CURRENT_RATIO(self):
		pass
		return 
	
#################
### Take the PE, PBV, PEG for TODAY
	def Ratios(self):
		print('\n---- Starting the Ratios function...')
		self.document = 'ratios'
		print('-- Requested Ratios. Selected document is '+self.document+' for'+self.ticker)
		ratios_data = self.Get_data_from_api('quarter') #it is a string json format
		#print(ratios_data)
		load = json.loads(ratios_data) #list
		print('I m in')
		df = pd.DataFrame(load)
		print('-- Income Statement Loaded , Dataframe loaded, Selecting Ratios')
		x_ax = df['date'].to_numpy()
		y1_ax = df['priceBookValueRatio'].to_numpy()
		y2_ax = df['priceEarningsRatio'].to_numpy()
		y3_ax = df['priceEarningsToGrowthRatio'].to_numpy()
		y4_ax = df['dividendYield'].to_numpy()
		y5_ax = df['returnOnEquity'].to_numpy()
		#price, shares, peg, roe, yeld, = self.Price()
		print('-- Latest data is date on: '+str(x_ax[0]))
		#print('-- Price:'+str(price))
		#print('-- SHares:'+str(shares))
		#print('-- PE/Grow:'+str(peg))
		#print('-- Div Yeld:'+str(yeld))
		#print('-- ROE:'+str(roe))
		#print('\n')
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
		#self.title_data = ['EPS','netIncomeRatio']
		#print(x_ax_order)
		print('--- Closing the RATIOS function...')
		return  pe, pbv, peg,div,roe  
	
	def Price(self):
		print('\n---- Starting the Price function...')
		self.document = 'enterprise_value'
		print('-- Requested Ratios. Selected document is '+self.document+' for'+self.ticker)
		self.statistic = 'Stock Price'
		x, price = self.Get_list()
		self.statistic = 'Number of Shares'
		a , shares = self.Get_list()
		self.statistic = 'priceEarningsToGrowthRatio'
		m ,peg = self.Get_list()
		self.statistic = 'returnOnEquity'
		f ,roe = self.Get_list()
		self.statistic = 'dividendYield'
		v ,yeld = self.Get_list()
		print('--- Closing the  Price function...')
		return price,shares,peg,roe,yeld 


######################################
# 
# 
#

	def Plot(self):
		ticker_list = self.ticker.split(',')
		tickers_dict = dict()
		if (len(ticker_list) > 1):
			print('\n-- PLOT FUNCTION starting: You selected '+str(len(ticker_list))+' tickers')
			for ticker in ticker_list:
				self.ticker = ticker
				print('\n---- Collecting data for '+str(self.ticker))
				if (self.statistic == 'BV_DEBT'):
					(x_ax_order,y1_ax_order,y2_ax_order) = self.BV_DEBT()

				else:
					(x_ax_order,y1_ax_order,y2_ax_order) = self.EPS()
				tickers_dict[ticker] = { 'x' : x_ax_order , 'y1' : y1_ax_order, 'y2' : y2_ax_order}
				print(str(self.title_data))
				self.Plot_statistic(tickers_dict)

		else:
			print('---- Collecting data for '+ticker_list[0])
			if (self.statistic == 'BV_DEBT'):
				(x_ax_order,y1_ax_order,y2_ax_order) = self.BV_DEBT()
			else:
				(x_ax_order,y1_ax_order,y2_ax_order) = self.EPS()
			print(str(self.title_data))
			#print(x_ax_order)
			tickers_dict[ticker_list[0]] = { 'x' : x_ax_order , 'y1' : y1_ax_order, 'y2' : y2_ax_order}
			#print(tickers_dict)
			self.Plot_statistic(tickers_dict)
		return


#
# Plot wanted statitics for 2x1 or 2x2 suplots
#
#def Plot_statistic(company,title_data, x_data, y1_data, y2_data, y3_data = None,y4_data = None):
	def Plot_statistic(self,tickers_dict, tickers_dict_2 = None ):
		print('\n---- Trying to plot statistics ')
		ticker_list = self.ticker.split(',')
		if (len(ticker_list) == 1):
			print('--Plotting statics for: '+str(ticker_list))
			if (len(self.title_data) == 2):
				fig, axs = plt.subplots(nrows=2,ncols=1, num=str(ticker_list)+' retrieved data')
				for ticker in ticker_list:
					#print(str(ticker))
					#print(tickers_dict)
					axs[0].plot(tickers_dict[str(ticker)]['x'],tickers_dict[str(ticker)]['y1'], 
									'tab:green',label = ticker)
					axs[0].set_title(str(self.title_data[0]))
					axs[1].plot(tickers_dict[str(ticker)]['x'],tickers_dict[str(ticker)]['y2'], 
								'tab:blue', label = ticker)
					axs[1].set_title(str(self.title_data[1]))
			else:
				ticker = ticker_list[0]
				fig, axs = plt.subplots(nrows=2,ncols=2, num=str(ticker)+' retrieved data')
				axs[0,0].plot(tickers_dict[str(ticker)]['x'],tickers_dict[str(ticker)]['y1'], 'tab:green')
				axs[0,0].set_title(str(self.title_data[0]))
				axs[0,1].plot(tickers_dict[str(ticker)]['x'],tickers_dict[str(ticker)]['y2'], 'tab:blue')
				axs[0,1].set_title(str(self.title_data[1]))
				axs[1,0].plot(tickers_dict_2[str(ticker)]['x'],tickers_dict_2[str(ticker)]['y1'],'tab:red')
				axs[1,0].set_title(str(self.title_data[2]))
				axs[1,1].plot(tickers_dict_2[str(ticker)]['x'],tickers_dict_2[str(ticker)]['y2'], 'tab:orange')
				axs[1,1].set_title(str(self.title_data[3]))
		else:
			print('--Plotting statics for: '+str(ticker_list))
			pass
		fig.autofmt_xdate()
		print(' -- --- Plotting the graphs over time')
		plt.show()
		return 

		


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






