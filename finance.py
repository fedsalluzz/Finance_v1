########################################################################################
# Process the information taken from API https://financialmodelingprep.com/developer/docs/
##########################################################################################

import platform
import os
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['axes.grid'] = True
import numpy as np
from tkinter import *
import requests


print('Your pithon version is: ' + platform.python_version())

#A URL that returns an HTTP response in Json format is called API endpoint
#Financial_api_endpoint = 'https://financialmodelingprep.com/api/v3/'+api_method+'/'+symbol+'?apikey='+financial_api_key
#r = requests.get(Financial_api_endpoint)
#print(r.text)

#
# Retrieve data from API endpoint
#
#de
def Get_data_from_api(document,symbol,period,api_key):
	print('\n---- GET DATA FROM API starting...')
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
	try:
		r = requests.get(api_endpoint)
		print('-- API ENDPOINT IS : '+api_endpoint)
		print('-- GET '+document+' from endpoint' )
	except:
		print('**** EXCEPTION in Get_data_from_api :: message from API endopoint: '+r.text)
	return r.text

#
# Plot wanted statitics for 2x1 or 2x2 suplots
#
#def Plot_statistic(company,title_data, x_data, y1_data, y2_data, y3_data = None,y4_data = None):
def Plot_statistic(ticker_list,title_data,tickers_dict, tickers_dict_2 = None ):
	print('\n---- Trying to plot statistics ')
	if (len(ticker_list) == 1):
		print('--Plotting statics for: '+str(ticker_list))
		if (len(title_data) == 2):
			fig, axs = plt.subplots(nrows=2,ncols=1, num=str(ticker_list)+' retrieved data')
			for ticker in ticker_list:
				#print(str(ticker))
				#print(tickers_dict)
				
				axs[0].plot(tickers_dict[str(ticker)]['x'],tickers_dict[str(ticker)]['y1'], 'tab:green',label = ticker)
				axs[0].set_title(str(title_data[0]))
				axs[1].plot(tickers_dict[str(ticker)]['x'],tickers_dict[str(ticker)]['y2'], 'tab:blue', label = ticker)
				axs[1].set_title(str(title_data[1]))
		else:
			ticker = ticker_list[0]
			fig, axs = plt.subplots(nrows=2,ncols=2, num=str(ticker)+' retrieved data')
			axs[0,0].plot(tickers_dict[str(ticker)]['x'],tickers_dict[str(ticker)]['y1'], 'tab:green')
			axs[0,0].set_title(str(title_data[0]))
			axs[0,1].plot(tickers_dict[str(ticker)]['x'],tickers_dict[str(ticker)]['y2'], 'tab:blue')
			axs[0,1].set_title(str(title_data[1]))
			axs[1,0].plot(tickers_dict_2[str(ticker)]['x'],tickers_dict_2[str(ticker)]['y1'], 'tab:red')
			axs[1,0].set_title(str(title_data[2]))
			axs[1,1].plot(tickers_dict_2[str(ticker)]['x'],tickers_dict_2[str(ticker)]['y2'], 'tab:orange')
			axs[1,1].set_title(str(title_data[3]))
	else:
		print('--Plotting statics for: '+str(ticker_list))
		pass
	fig.autofmt_xdate()
	print(' -- --- Plotting the graphs over time')
	plt.show()
	return #plt.show() 

#
# Sort data from oldest to newest
#
def Time_and_statistic_sorter(years,x_ax,y1_ax,y2_ax):
	if (years == "MAX"):
		pass
	else:
		timespan = x_ax[:int(years)*4] #quarter data
		y1_reduced_data = y1_ax[:int(years)*4] #quarter data
		y2_reduced_data = y2_ax[:int(years)*4] #quarter data

	x_ax_order = timespan[::-1]
	y1_ax_order = y1_reduced_data[::-1] 
	y2_ax_order = y2_reduced_data[::-1]
	print('-- Selected data for '+years+' years')
	return (x_ax_order,y1_ax_order,y2_ax_order)

#
# Create dataframe with EPS data from income_statement (x,y1 and y2 axis)
#
def EPS(ticker,years, financial_api_key):
	print('\n---- Starting the EPS function...')
	eps_data = Get_data_from_api('income_statement',ticker,'quarter', financial_api_key) #it is a string json format
	#print(eps_data)
	load = json.loads(eps_data) #list
	try:
		df = pd.DataFrame(load)
		print('-- Income Statement Loaded , Dataframe loaded, Selecting EPS and EPS diluted')
		x_ax = df['date'].to_numpy()
		y1_ax = df['eps'].to_numpy()
		y2_ax = df['epsdiluted'].to_numpy()
		x_ax_order,y1_ax_order,y2_ax_order = Time_and_statistic_sorter(years,x_ax,y1_ax,y2_ax)
		title_data = ['EPS','EPS diluted']
		print(x_ax_order)
		print('--- Closing the EPS function...')
	except:
		print('**** EXCEPTION in ESP function :: message from API endopoint: '+eps_data)
		exit
	return title_data , x_ax_order.tolist(), y1_ax_order.tolist(), y2_ax_order.tolist()  

#
# Create dataframe with book vlue and debt per earning data from metrics (x,y1 and y2 axis)
#
def BV_DEBT(ticker,years, financial_api_key):
	print('\n---- Starting the BV_DEBT function...')
	bv_data = Get_data_from_api('metrics',ticker,'quarter', financial_api_key) #it is a string json format
	load = json.loads(bv_data) #list
	try:
		df = pd.DataFrame(load)
		#print(bv_data)
		print('-- Income Statement Loaded , Dataframe loaded, Selecting BV and Debt')
		x_ax = df['date'].to_numpy()
		y1_ax = df['bookValuePerShare'].to_numpy()
		y2_ax = df['debtToEquity'].to_numpy()
		x_ax_order,y1_ax_order,y2_ax_order = Time_and_statistic_sorter(years,x_ax,y1_ax,y2_ax)
		title_data = ['bookValuePerShare','debtToEquity']
		print(x_ax_order)
		print('--- Closing the BD_DEBT function...')
	except:
		print('**** EXCEPTION in BV_DEBT function :: message from API endopoint: '+eps_data)
		exit

	return  title_data , x_ax_order.tolist(), y1_ax_order.tolist(), y2_ax_order.tolist()


def CURRENT_RATIO(ticker, financial_api_key):
	current_ratio_data = Get_data_from_api('metrics',ticker,'quarter', financial_api_key) #it is a string json format
	return current_ratio_data


#
# Check if the wanted data are present into internal database. Avoid max count to be reached fro API request
#in trial version it is up to 200 calls
#
#def Ticker_data_is_saved(ticker,document):
#	print('----\n Checking if '+ticker+' data has been previously saved...')
#	file = open("user_requests.log","r")
#	content = file.read()
#	dictionary = ast.litteral_eval(content)
#	for tick in dictionary:
#		if (tick == ticker);
#			print('-- Some data found...')
#			if(dictionary[tick][document] == True )
#				print('-- '+document+' data has been found in previous research. New data will not be request')
#				found = True
#			else:
#				print('-- '+document+' data has *NOT* been found in previous research. New data will be request')
#
#				found = False
#	return found 
#
#
#
##################################################
##### MAIN #######################################
#################################################

financial_api_key = 'c69c0e1c9f3b70a951441dc376b6d400'
#document = 'metrics'
#indicators = ['debtToEquity','peRatio']
#financial_data = Get_data_from_api(document,'AAPL','quarter', financial_api_key) #it is a string json format

#Plot_statistic(financial_data, indicators )




##################################################
####### WINDOW with TKINTER ######################
###############################################

def ESP_click():
	tickers_dict = dict()
	entered_tickers=textTicker.get()
	entered_years = buttonYears_var.get()
	print('\n---- CLICK EVENT -- Selected ticker is/are: '+entered_tickers)
	ticker_list = entered_tickers.split(',')
	if (len(ticker_list) > 1):
		print('-- You selected '+str(len(ticker_list))+' tickers\n')
		for ticker in ticker_list:
			print('---- Collecting data for '+ticker)
			(title_data,x_ax_order,y1_ax_order,y2_ax_order) = EPS(ticker,entered_years, financial_api_key)
			tickers_dict[ticker] = { 'x' : x_ax_order , 'y1' : y1_ax_order, 'y2' : y2_ax_order}
			Plot_statistic(ticker_list,title_data,tickers_dict)
	else:
		print('-- You selected '+str(len(ticker_list))+' tickers\n')
		print('---- Collecting data for '+ticker_list[0])
		(title_data,x_ax_order,y1_ax_order,y2_ax_order) = EPS(entered_tickers,entered_years, financial_api_key)
		print(str(title_data))
		print(x_ax_order)
		tickers_dict[ticker_list[0]] = { 'x' : x_ax_order , 'y1' : y1_ax_order, 'y2' : y2_ax_order}
		print(tickers_dict)
		Plot_statistic(ticker_list,title_data,tickers_dict)
	return

def BV_DEBT_click():
	tickers_dict = dict()
	entered_tickers=textTicker.get()
	entered_years = buttonYears_var.get()
	print('-- Selected ticker is/are: '+entered_tickers)
	ticker_list = entered_tickers.split(',')
	if (len(ticker_list) > 1):
		print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			(title_data,x_ax_order,y1_ax_order,y2_ax_order) = BV_DEBT(ticker,entered_years, financial_api_key)
			tickers_dict[ticker] = { 'x' : x_ax_order , 'y1' : y1_ax_order, 'y2' : y2_ax_order} 
	else:
		print('---- Collecting data for '+ticker_list[0])
		(title_data,x_ax_order,y1_ax_order,y2_ax_order) = BV_DEBT(entered_tickers,entered_years, financial_api_key)
		print(str(title_data))
		print(x_ax_order)
		tickers_dict[ticker_list[0]] = { 'x' : x_ax_order , 'y1' : y1_ax_order, 'y2' : y2_ax_order}
		print(tickers_dict)
		Plot_statistic(ticker_list,title_data,tickers_dict)
	return

def ANALYZE_click():
	tickers_dict_eps = dict()
	tickers_dict_debt = dict()
	entered_tickers=textTicker.get()
	entered_years = buttonYears_var.get() 
	print('-- Selected ticker is/are: '+entered_tickers)
	ticker_list = entered_tickers.split(',')
	if (len(ticker_list) > 1):
		print('-- You selected '+str(len(ticker_list))+' tickers \n')
		print('---- Collecting EPS and BD and DEBT data for '+ticker_list[0])
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			(eps_title,x_eps,y1_eps,y2_eps) = EPS(ticker,entered_years, financial_api_key) 
			(debt_title,x_debt,y1_debt,y2_debt) = BV_DEBT(ticker,entered_years, financial_api_key) 
			tickers_dict_eps[ticker] = { 'x' : x_eps , 'y1' : y1_eps, 'y2' : y2_eps} 
			tickers_dict_debt[ticker] = { 'x' : x_debt , 'y1' : y1_debt, 'y2' : y2_debt}
	else:
		
		print('-- You selected '+str(len(ticker_list))+' tickers \n')
		print('---- Collecting EPS and BD and DEBT data for '+ticker_list[0])
		(eps_title,x_eps,y1_eps,y2_eps) = EPS(entered_tickers,entered_years, financial_api_key) 
		(debt_title,x_debt,y1_debt,y2_debt) = BV_DEBT(entered_tickers,entered_years, financial_api_key) 
		tickers_dict_eps[ticker_list[0]] = { 'x' : x_eps , 'y1' : y1_eps, 'y2' : y2_eps} 
		tickers_dict_debt[ticker_list[0]] = { 'x' : x_debt , 'y1' : y1_debt, 'y2' : y2_debt}
		print(str(eps_title+debt_title))
		title_data = eps_title+debt_title
		Plot_statistic(ticker_list,title_data,tickers_dict_eps,tickers_dict_debt)
		if (len(x_eps) == len(x_debt)):
			x_ax_order = x_eps
			Plot_statistic(ticker_list,title_data,tickers_dict_eps,tickers_dict_debt)
			print(tickers_dict_eps)
		else:
			print('**** ERROR time lists not equal lenght ********')
			exit
	return



#create the window
window = Tk()
window.title("FINANCE GUI")
window.geometry("800x800")
window.configure(background="black")

#Create a Label and text entry box  for Directory
Label (window, text=" Program Directory ", bg="black" , fg="white", font="none 12 bold") .grid(row=2, column=0, sticky=W)

textDirectory = Entry(window, width=40, bg="white")
textDirectory.grid(row=2, column=1, sticky=W)
dir_path = os.path.dirname(os.path.realpath(__file__))
textDirectory.insert(END,dir_path)

#Create a Label and text entry box  for ticker
Label (window, text=" Selected symbol ", bg="black" , fg="white", font="none 12 bold") .grid(row=3, column=0, sticky=W)

textTicker = Entry(window, width=40, bg="white")
textTicker.grid(row=3, column=1, sticky=W)
initial_ticker_fill = 'AAPL'
textTicker.insert(END,initial_ticker_fill)

#Create a Label and text entry box  for time
TIME_SPAN = [
	("1Y", "1"),
	("2Y", "2"),
	("5Y", "5"),
	("10Y", "10"),
	("MAX", "MAX"),
	]
i = 4
buttonYears_var = StringVar()
buttonYears_var.set("1") # initialize
for text, mode in TIME_SPAN:
	i = i+1
	buttonYears = Radiobutton(window, text=text ,variable=buttonYears_var, value=mode, bg="white" , fg="black")
	buttonYears.grid(column=0, row=i)


#Create the button calculate the EPS
buttonEPS = Button(window, text="ESP/ESP diluted", fg="black", font="none 12 bold", command=ESP_click)
buttonEPS.grid(row=9, column=3, sticky=W)

#Create the button calculate the BV and DEBT 
buttonDEBT = Button(window, text="BV / DEBT ", fg="black", font="none 12 bold", command=BV_DEBT_click)
buttonDEBT.grid(row=10, column=3, sticky=W)

#Create the button calculate the main parameters 
buttonANALYZE = Button(window, text="  Analyze  ", fg="black", font="none 12 bold", command=ANALYZE_click)
buttonANALYZE.grid(row=11, column=3, sticky=W)




window.mainloop()

