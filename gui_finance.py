import os
import sys
sys.path.append(".")

from analyses import Analyses
import tkinter as tk
from tkinter import *
import pandas as pd
import csv


##################################################
####### WINDOW with TKINTER ######################
###############################################

class GUI:
	def __init__(self, master):
		self.master = master
		self.master.title("FINANCE GUI")
		self.master.geometry("1200x900")
		self.master.configure(background="black")
		self.frame = tk.Frame(self.master)
		self.prova = 'prova'
		self.apikey = 'c69c0e1c9f3b70a951441dc376b6d400'

		self.textDirectory = tk.Entry(self.frame, width=60, bg="white")
		self.textDirectory.grid(row=2, column=1)
		dir_path = os.path.dirname(os.path.realpath(__file__))
		self.textDirectory.insert(END,dir_path)

		#Create a Label and text entry box  for ticker
		self.labelTk = tk.Label (self.frame, text=" Selected symbol ", bg="black" , fg="white", font="none 12 bold") .grid(row=3, column=0,sticky = W, pady = 2)

		self.textTicker = tk.Entry(self.frame, width=40, bg="white")
		self.textTicker.grid(row=3, column=1)
		initial_ticker_fill = 'AAPL'
		self.textTicker.insert(END,initial_ticker_fill)
		
#marketCapMoreThan & marketCapLowerThan : Number
#betaMoreThan & betaLowerThan : Number
#dividendMoreThan & dividendLowerThan : Number
		
		
		#Create a Label and text entry box  for stock screener
		self.labelTk = tk.Label (self.frame, text=" Stocks Screener marketCap > ", bg="black" , fg="white", font="none 12 bold") .grid(row=4, column=0,sticky = W, pady = 2)
		self.textTicker2 = tk.Entry(self.frame, width=20, bg="white")
		self.textTicker2.grid(row=4, column=1)
		self.textTicker2.insert(END,'1000000')	
		self.labelTk = tk.Label (self.frame, text=" Stocks Screener marketCap < ", bg="black" , fg="white", font="none 12 bold") .grid(row=5, column=0,sticky = W, pady = 2)
		self.textTicker3 = tk.Entry(self.frame, width=20, bg="white")
		self.textTicker3.grid(row=5, column=1)
		self.labelTk = tk.Label (self.frame, text=" Stocks Screener beta > ", bg="black" , fg="white", font="none 12 bold") .grid(row=6, column=0,sticky = W, pady = 2)
		self.textTicker4 = tk.Entry(self.frame, width=20, bg="white")
		self.textTicker4.grid(row=6, column=1)
		self.labelTk = tk.Label (self.frame, text=" Stocks Screener beta < ", bg="black" , fg="white", font="none 12 bold") .grid(row=7, column=0,sticky = W, pady = 2)
		self.textTicker5 = tk.Entry(self.frame, width=20, bg="white")
		self.textTicker5.grid(row=7, column=1)
		self.labelTk = tk.Label (self.frame, text=" Stocks Screener dividend > ", bg="black" , fg="white", font="none 12 bold") .grid(row=8, column=0,sticky = W, pady = 2)
		self.textTicker6 = tk.Entry(self.frame, width=20, bg="white")
		self.textTicker6.grid(row=8, column=1)
		self.labelTk = tk.Label (self.frame, text=" Stocks Screener dividend < ", bg="black" , fg="white", font="none 12 bold") .grid(row=9, column=0,sticky = W, pady = 2)
		self.textTicker7 = tk.Entry(self.frame, width=20, bg="white")
		self.textTicker7.grid(row=9, column=1)
		self.labelTk = tk.Label (self.frame, text=" Stocks Screener sector", bg="black" , fg="white", font="none 12 bold") .grid(row=10, column=0,sticky = W, pady = 2)
		self.textTicker8 = tk.Entry(self.frame, width=20, bg="white")
		self.textTicker8.grid(row=10, column=1)
		self.labelTk = tk.Label (self.frame, text=" Stocks Screener Industry ", bg="black" , fg="white", font="none 12 bold") .grid(row=11, column=0,sticky = W, pady = 2)
		self.textTicker9 = tk.Entry(self.frame, width=20, bg="white")
		self.textTicker9.grid(row=11, column=1)
		self.labelTk = tk.Label (self.frame, text=" Stocks Screener exchange ", bg="black" , fg="white", font="none 12 bold") .grid(row=12, column=0,sticky = W, pady = 2)
		self.textTicker10 = tk.Entry(self.frame, width=20, bg="white")
		self.textTicker10.grid(row=12, column=1)
		self.textTicker10.insert(END,'NYSE,NASDAQ')	

		#Create a Label with the Real Time evaluator
#		self.label_real_time = tk.Label (self.frame, text="PE\nPBV\nPEG\nDIV\nROE\n", bg="black" , fg="white") .grid(row=4, column=2,sticky = E, pady = 1)
#		self.text_real_time = tk.Text (self.frame, height = 5, width = 10)
#		self.text_real_time.insert(tk.END,self.prova, 'blue')
#		self.text_real_time.grid(row=4, column=3,sticky = W, pady = 2)
		
		#Create a Label and text entry box  for time
		TIME_SPAN = [
			("1Y", "1"),
			("2Y", "2"),
			("5Y", "5"),
			("10Y", "10"),
			("MAX", "MAX"),
			]
		i = 0
		self.buttonYears_var = StringVar()
		self.buttonYears_var.set("1") # initialize
		for text, mode in TIME_SPAN:
			i = i+1
			self.buttonYears = tk.Radiobutton(self.frame, text=text ,variable=self.buttonYears_var, value=mode, bg="white" , fg="black")
			self.buttonYears.grid(column=3, row=i,sticky = W, pady = 2)

		#Create the button
		self.buttonGrowth = tk.Button(self.frame, text=" Financial Growth % ", fg="black", font="none 9 bold", command=self.Growth_click)
		self.buttonGrowth.grid(row=6, column=1,sticky = E, pady = 2)
		#Create the button
		self.Cash_growth = tk.Button(self.frame, text=" Cash Flow Growth % ", fg="black", font="none 9 bold", command=self.Cash_Flow_Growth_click)
		self.Cash_growth.grid(row=6, column=2,sticky = E, pady = 2)
		#Create the button
		self.buttonExtra2 = tk.Button(self.frame, text=" ES ", fg="black", font="none 9 bold", command=self.BalanceSheet_click)
		self.buttonExtra2.grid(row=6, column=3,sticky = E, pady = 2)

		#Create the button
		self.buttonBalance = tk.Button(self.frame, text="Balance Sheet", fg="black", font="none 9 bold", command=self.BalanceSheet_click)
		self.buttonBalance.grid(row=7, column=1,sticky = E, pady = 2)
		#Create the button 
		self.buttonIncome = tk.Button(self.frame, text="Income Statement ", fg="black", font="none 9 bold", command=self.IncomeStatement_click)
		self.buttonIncome.grid(row=7, column=2,sticky = W, pady = 2)
		#Create the button
		self.buttonCash = tk.Button(self.frame, text="Cash Flow", fg="black", font="none 9 bold", command=self.CashFlow_click)
		self.buttonCash.grid(row=7, column=3,sticky = W, pady = 2)
		#Create the button
		self.buttonProf = tk.Button(self.frame, text="Profitability", fg="black", font="none 9 bold", command=self.Profitability_click)
		self.buttonProf.grid(row=8, column=3,sticky = W, pady = 2)
		#Create the button
		self.buttonDebt = tk.Button(self.frame, text="Debt Figures", fg="black", font="none 9 bold", command=self.DebtFigures_click)
		self.buttonDebt.grid(row=9, column=3,sticky = W, pady = 2)
		#Create the button 
		self.buttonANALYZE = tk.Button(self.frame, text="  Fundamentals  ", fg="black", font="none 9 bold", command=self.Fundamentals_click)
		self.buttonANALYZE.grid(row=10, column=3,sticky = W, pady = 2)
		#Create the button
		self.buttonStockScreener= tk.Button(self.frame, text="Stocks Screener", fg="black", font="none 9 bold", command=self.StockScreener_click)
		self.buttonStockScreener.grid(row=12, column=2,sticky = W, pady = 2)
		#Create the button
		self.buttonNOW = tk.Button(self.frame, text="  Analyze Stock ", fg="black", font="none 9 bold", command=self.Analyze_stock)
		self.buttonNOW.grid(row=12, column=3,sticky = W, pady = 2)
		#Create a Label and text entry box  for Directory
		self.labelDirectory = tk.Label (self.frame, text=" Program Directory ", bg="black" , fg="white", font="none 12 bold") .grid(row=2, column=0,sticky = W, pady = 2)
		#Button Yield and label with entry
		self.buttonYield= tk.Button(self.frame, text=" Div Yeld Screener ", fg="black", font="none 9 bold", command=self.YieldSearch_click)
		self.buttonYield.grid(row=13, column=2,sticky = W, pady = 2)
		self.labelYield = tk.Label (self.frame, text=" Yield target ", bg="black" , fg="white", font="none 12 bold") .grid(row=13, column=0,sticky = W, pady = 2)
		self.textYield = tk.Entry(self.frame, width=20, bg="white")
		self.textYield.grid(row=13, column=1)
		self.textYield.insert(END,'0.02')	

		self.labelDirectory = tk.Label (self.frame, text=" Program Directory ", bg="black" , fg="white", font="none 12 bold") .grid(row=2, column=0,sticky = W, pady = 2)
		self.buttonTickers= tk.Button(self.frame, text=" Ticker List ", fg="black", font="none 9 bold", command=self.Ticker_list_click)
		self.buttonTickers.grid(row=13, column=3,sticky = E, pady = 2)

		self.textTicker11 = tk.Text(self.frame, height=50, width=80, bg="white")
		self.textTicker11.grid(row=16, column=0,columnspan=4)
		instructions_fill = '\n\t\t\t *** HOW TO USE STOCK SCREENER ***\n\n1. Select criteria\nmarketCapMoreThan & marketCapLowerThan : Number \nbetaMoreThan & betaLowerThan : Number \nvolumeMoreThan & volumeLowerThan : Number \ndividendMoreThan & dividendLowerThan : Number \nsector : \n\tConsumer Cyclical - Energy - Technology - Industrials \n\tFinancial Services - Basic Materials - Communication Services Consumer Defensive - Healthcare - Real Estate - Utilities - Industrial Goods - Financial - Services - Conglomerates \n Industry :  \n\tAutos - Banks - Banks Diversified - Software - Banks Regional - Beverages Alcoholic  \n\tBeverages Brewers - Beverages Non-Alcoholic \n exchange : nyse - nasdaq - amex - euronex - tsx - etf - mutual_fund \n limit : Number \n\nexample.\nstock-screener?marketCapMoreThan=1000000000&betaMoreThan=1&volumeMoreThan=10000&sector=Technology&exchange=NASDAQ&dividendMoreThan=0&limit=100\n\n2. Select Yield Target \n\n3. Press $$$'
		self.textTicker11.insert(END,instructions_fill)
		self.frame.pack()
		

############################# CLICK FUNCTIONS ###############################################
#############################################################################################


	def Cash_Flow_Growth_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT Cash_Flow_Growth_click ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			Growth = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '%')
			(date,operatingCashFlowGrowth, freeCashFlowGrowth) = Growth.Get_document_for(ticker,'operatingCashFlowGrowth','freeCashFlowGrowth','financial-growth' ) 
			(date_2,rdexpenseGrowth, debtGrowth) = Growth.Get_document_for(ticker, 'rdexpenseGrowth', 'debtGrowth', document = 'financial-growth' ) 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : operatingCashFlowGrowth, 'y2' : freeCashFlowGrowth} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : rdexpenseGrowth, 'y2' : debtGrowth}
			#print(tickers_dict_eps
		Growth.title_data = ['operatingCashFlowGrowth','freeCashFlowGrowth','rdexpenseGrowth','debtGrowth']
		plot = Growth.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'Growth' ) 




	def Growth_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT Growth_click ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			Growth = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '%')
			(date,revenueGrowth, operatingIncomeGrowth) = Growth.Get_document_for(ticker,'revenueGrowth','operatingIncomeGrowth','financial-growth' ) 
			(date_2,netIncomeGrowth, epsdilutedGrowth) = Growth.Get_document_for(ticker, 'netIncomeGrowth', 'epsdilutedGrowth', document = 'financial-growth' ) 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : revenueGrowth, 'y2' : operatingIncomeGrowth} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : netIncomeGrowth, 'y2' : epsdilutedGrowth}
			#print(tickers_dict_eps
		Growth.title_data = ['revenueGrowth','operatingIncomeGrowth','netIncomeGrowth','epsdilutedGrowth']
		plot = Growth.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'Growth' ) 




	def BalanceSheet_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT BalanceSheet ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			BalanceSheet = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = 'log')
			(date,totalCurrentLiabilities, totalCurrentAssets) = BalanceSheet.Get_document_for(ticker,'totalCurrentLiabilities','totalCurrentAssets','balance_sheet' ) 
			(date_2,shortTermDebt, longTermDebt) = BalanceSheet.Get_document_for(ticker, 'shortTermDebt', 'longTermDebt', document = 'balance_sheet' ) 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : totalCurrentLiabilities, 'y2' : totalCurrentAssets} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : shortTermDebt, 'y2' : longTermDebt}
			#print(tickers_dict_eps
		BalanceSheet.title_data = ['totalCurrentLiabilities','totalCurrentAssets','shortTermDebt','longTermDebt']
		plot = BalanceSheet.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'BalanceSheet' ) 




	def CashFlow_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT CashFlow ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			CashFlow = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = ' ')
			(date,netCashProvidedByOperating, netCashUsedForInvesting) = CashFlow.Get_document_for(ticker,'netCashProvidedByOperatingActivities','netCashUsedForInvestingActivites',document = 'cash_flow' ) 
			(date_2,netCashUsedProvidedByFinancing, netChangeInCash) = CashFlow.Get_document_for(ticker, 'netCashUsedProvidedByFinancingActivities', 'netChangeInCash', document =  'cash_flow' ) 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : netCashProvidedByOperating, 'y2' : netCashUsedForInvesting} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : netCashUsedProvidedByFinancing, 'y2' : netChangeInCash}
			#print(tickers_dict_eps
		CashFlow.title_data = ['netCashProvidedByOperatingActivities','netCashUsedProvidedByForInvestingActivities','netCashUsedProvidedByFinancingActivities','netChangeInCash']
		plot = CashFlow.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'CashFlow' )



	def IncomeStatement_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT IncomeStatement ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			IncomeStatement = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = 'log')
			(date,Revenue, NetIncome) = IncomeStatement.Get_document_for(ticker, 'revenue', 'netIncome',document = 'income_statement') 
			(date_2,operatingIncome ,ebitda) =  IncomeStatement.Get_document_for(ticker, 'operatingIncome', 'ebitda',document = 'income_statement') 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : Revenue, 'y2' : NetIncome} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : operatingIncome , 'y2' : ebitda}
		IncomeStatement.title_data = ['Revenue','NetIncome','OperatingIncome','Ebitda ']
		plot = IncomeStatement.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'IncomeStatement' )



###################figures


	def Profitability_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT Profitability ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		#print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			Profitability = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '%')
			(date,grossProfitRatio, operatingIncome) = Profitability.Get_document_for(ticker, 'grossProfitRatio', 'operatingIncomeRatio',document = 'income_statement') 
			(date_2,returnOnTangibleAssets ,roic) =  Profitability.Get_document_for(ticker, 'returnOnTangibleAssets', 'roic',document = 'metrics') 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : grossProfitRatio, 'y2' : operatingIncome} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : returnOnTangibleAssets , 'y2' : roic}
		Profitability.title_data = ['grossProfitRatio','operatingIncomeRatio','returnOnTangibleAssets','roic ']
		plot = Profitability.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'Profitability' )



	def DebtFigures_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT DebtFigures ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		#print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			DebtFigures = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '  ')
			(date,Current_ratio, Debt_to_Assets) = DebtFigures.Get_document_for(ticker, 'currentRatio', 'debtToAssets',document = 'metrics') 
			(date_2,bookValuePerShare,debtToEquity) =  DebtFigures.Get_document_for(ticker, 'netDebtToEBITDA', 'debtToEquity',document = 'metrics') 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : Current_ratio, 'y2' : Debt_to_Assets} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : bookValuePerShare, 'y2' : debtToEquity}
		DebtFigures.title_data = ['CurrentRatio =\n CurrentAssets/CurrentLiabilities','DebtToAssets =\n STDebts+LTDebts/TotalAssets','netDebtToEBITDA =\n TotalDebt - Cash&Equivalents / EBITDA','debtToEquity =\n TotalLiabilities/ShareholdersEquity']
		plot = DebtFigures.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'DebtFigures' )

	
	
	def Fundamentals_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK Fundamentals_click---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			a = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '')
			#a.title_data = ['Earning Per Share','netIncomeRatio']
			(date,eps ,netIncomeRatio) = a.Get_document_for(ticker, 'epsdiluted', 'netIncomeRatio',document = 'income_statement') 
			(date_2,bookValuePerShare,roe) =  a.Get_document_for(ticker, 'bookValuePerShare', 'roe', document = 'metrics') 
			(date_2,dividendYield,roe ) =  a.Get_document_for(ticker, 'dividendYield', 'roe', document = 'metrics')
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : eps, 'y2' : dividendYield} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : bookValuePerShare, 'y2' : roe}
		a.title_data = ['Earning Per Share Diluted =\n (NetIncome - PreferredDividends)/SharesOutstanding','dividendYield %','bookValuePerShare =\n (TotalEquity-PreferredEquity)/SharesOutstanding','ROE =\n NetIncome/SharholdersEquity']
		print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
		click_data = ['EPS' ,'netIncomeRatio','BVPS','ROE']
		plot = a.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'Analyze')
			

	def Analyze_stock(self):
		tickers_quote= dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get()
		print('\n---- CLICK EVENT  Analyze_stock ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		print('---- You selected '+str(len(ticker_list))+' tickers')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			Quote = Analyses(ticker,period = entered_years,api_key =self.apikey, statistic = ' ')
			price,priceAvg50,priceAvg200,eps,sharesOutstanding,marketCap = Quote.Get_quote_for(ticker) 
			today = Quote.today
			#Thoise values are evaluated at the latest date
			currentRatio,quickRatio, cashRatio, grossProfitMargin,operatingProfitMargin,netProfitMargin,returnOnAssets,returnOnEquity,interestCoverage,unused_1,operatingCashFlowPerShare,freeCashFlowPerShare =  Quote.Ratios(ttm = False) #return 12 strings
			latest_ratio_date = Quote.today
			currentRatio_ttm,quickRatio_ttm, cashRatio_ttm, grossProfitMargin_ttm,operatingProfitMargin_ttm,netProfitMargin_ttm,returnOnAssets_ttm,returnOnEquity_ttm,unused_0,unused_1,operatingCashFlowPerShare_ttm,freeCashFlowPerShare_ttm =  Quote.Ratios(ttm = True) #return 12 strings for TTM
			bookValuePerShare,debtToAssets,debtToEquity,enterpriseValue,enterpriseValueOverEBITDA,freeCashFlowPerShare,researchAndDdevelopementToRevenue,roe,roic = Quote.Metrics()
			beta,volAvg,lastDiv,dcf,ipoDate,industry,sector= Quote.Profile()
			tickers_quote[ticker] = { 'Today' : today ,
				'beta':beta, 
				'volAvg':volAvg, 
				'lastDiv':lastDiv, 
				'dcf':dcf, 
				'ipoDate':ipoDate, 
				'industry':industry, 
				'sector':sector, 
				'marketCap':marketCap, 
				'price' : price , 
				'priceAvg50' : priceAvg50, 
				'priceAvg200' : priceAvg200,
				'EPS' : eps ,
				'bookValuePerShare' : bookValuePerShare,
				'roe' : roe,
				'roic' :roic ,
				'sharesOutstanding' :sharesOutstanding, 
				'Latest report date': latest_ratio_date,
				'grossProfitMargin':grossProfitMargin ,
				'operatingProfitMargin':operatingProfitMargin,
				'netProfitMargin':netProfitMargin, 
				'returnOnAssets' : returnOnAssets, 
				'returnOnEquity' : returnOnEquity,
				'researchAndDdevelopementToRevenue' :researchAndDdevelopementToRevenue ,
				'currentRatio':currentRatio ,
				'quickRatio':quickRatio ,
				'debtToAssets' :debtToAssets ,
				'debtToEquity' :debtToEquity ,
				'cashRatio':cashRatio ,
				'interestCoverage' :interestCoverage ,
				'operatingCashFlowPerShare' :operatingCashFlowPerShare, 
				'freeCashFlowPerShare' :freeCashFlowPerShare,
				'enterpriseValue' :enterpriseValue ,
				'enterpriseValueOverEBITDA' :enterpriseValueOverEBITDA,
				'grossProfitMargin_ttm' :grossProfitMargin_ttm,
				'operatingProfitMargin_ttm' :operatingProfitMargin_ttm,
				'netProfitMargin_ttm' :netProfitMargin_ttm,
				'returnOnAssets_ttm' :returnOnAssets_ttm,
				'returnOnEquity_ttm' :returnOnEquity_ttm,
				'currentRatio_ttm' :currentRatio_ttm,
				'quickRatio_ttm' :quickRatio_ttm,
				'cashRatio_ttm' :cashRatio_ttm,
				'operatingCashFlowPerShare_ttm' :operatingCashFlowPerShare_ttm,
				'freeCashFlowPerShare_ttm' :freeCashFlowPerShare_ttm }
		index_for_dataframe = Quote.title_data = ['Today' ,
			'beta',
			'volAvg',
			'lastDiv',
			'dcf',
			'ipoDate',
			'industry',
			'sector',
			'marketCap',
			'price',
			'priceAvg50',
			'priceAvg200',
			'EPS',
			'bookValuePerShare',
			'roe',
			'roic' ,
			'sharesOutstanding' ,
			'Latest report date',
			'grossProfitMargin',
			'operatingProfitMargin',
			'netProfitMargin', 
			'returnOnAssets' ,
			'returnOnEquity' ,
			'researchAndDdevelopementToRevenue',
			'currentRatio',
			'quickRatio',
			'debtToAssets',
			'debtToEquity',
			'cashRatio',
			'interestCoverage',
			'grossProfitMargin',
			'operatingProfitMargin',
			'netProfitMargin', 
			'returnOnAssets' ,
			'returnOnEquity' ,
			'researchAndDdevelopementToRevenue',
 			'operatingCashFlowPerShare', 
			'freeCashFlowPerShare',
			'enterpriseValue',
			'enterpriseValueOverEBITDA', 
			'grossProfitMargin_ttm' ,
			'operatingProfitMargin_ttm' ,
			'netProfitMargin_ttm' ,
			'returnOnAssets_ttm' ,
			'returnOnEquity_ttm' ,
			'currentRatio_ttm' ,
			'quickRatio_ttm' ,
			'cashRatio_ttm' ,
			'operatingCashFlowPerShare_ttm' ,
			'freeCashFlowPerShare_ttm' ]
		mydict = tickers_quote
		frame = pd.DataFrame(tickers_quote, columns = entered_tickers.split(","), index=index_for_dataframe)
		print('Frame is '+str(frame)) 
		if(len(entered_tickers) > 1):
			f = open("saved_data/dataframe/"+entered_tickers.replace(',','_')+"_analyses_stock.log","w")
			print(frame,file = f)
			frame.to_csv(r'saved_data/csv/'+entered_tickers.replace(',','_')+'_analyses_stock.csv', index = index_for_dataframe)
		print('-- Analyze_stock printed on files for: '+entered_tickers)
		Quote.Get_Industry_Ratios(industry)
		self.CashFlowCalculator()
		#Quote.Get_History_data()





	def CashFlowCalculator(self):
		tickers_quote= dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get()
		print('\n----   CashFlowCalculator ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		print('---- You selected '+str(len(ticker_list))+' tickers')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			Quote = Analyses(ticker,period = entered_years,api_key =self.apikey, statistic = ' ')
			price,priceAvg50,priceAvg200,eps,sharesOutstanding,marketCap = Quote.Get_quote_for(ticker) 
			#Thoise values are evaluated at the latest date
			revenue,netIncome,ebitda,depreciationAndAmortization,interestExpense,incomeTaxExpense,operatingIncome,date,period =  Quote.IncomeStatement( history_year = 'latest') #return 12 strings
			date, period,totalAssets , totalLiabilities, totalCurrentAssets,totalCurrentLiabilities,totalNonCurrentAssets, shortTermDebt, longTermDebt, cashAndShortTermInvestments, retainedEarnings, propertyPlantEquipmentNet = Quote.BalanceSheet( history_year = 'latest') #return 14 strings
			date, period,operatingCashFlow , capitalExpenditure, dividendsPaid,commonStockRepurchased,changeInWorkingCapital, netCashProvidedByOperatingActivities, commonStockIssued, capitalExpenditure, freeCashFlow = Quote.CashFlowStatement( history_year = 'latest') #return 14 strings
			latest_ratio_date = Quote.today
			tickers_quote[ticker] = {'date': date, 
				'period' :period, 
				'price':price, 
				'sharesOutstanding':sharesOutstanding, 
				'revenue':revenue , 
				'netIncome': netIncome, 
				'ebitda': ebitda, 
				'depreciationAndAmortization': depreciationAndAmortization, 
				'interestExpense': interestExpense, 
				'incomeTaxExpense': incomeTaxExpense, 
				'operatingIncome': operatingIncome,
				'totalAssets': totalAssets,
				'totalLiabilities': totalLiabilities,
				'totalCurrentAssets':totalCurrentAssets ,
				'totalCurrentLiabilities': totalCurrentLiabilities,
				'totalNonCurrentAssets': totalNonCurrentAssets,
				'shortTermDebt': shortTermDebt,
				'longTermDebt': longTermDebt,
				'cashAndShortTermInvestments': cashAndShortTermInvestments,
				'retainedEarnings':retainedEarnings,
				'operatingCashFlow':operatingCashFlow,
				'capitalExpenditure':capitalExpenditure,
				'dividendsPaid':dividendsPaid,
				'commonStockRepurchased':commonStockRepurchased,
				'changeInWorkingCapital':changeInWorkingCapital,
				'netCashProvidedByOperatingActivities':netCashProvidedByOperatingActivities,
				'commonStockIssued':commonStockIssued,
				'capitalExpenditure':capitalExpenditure,
				'freeCashFlow':freeCashFlow,
				'propertyPlantEquipmentNet':propertyPlantEquipmentNet }
		index_for_dataframe = Quote.title_data = ['date', 
			'period',
			'price', 
			'sharesOutstanding', 
			'revenue', 
			'netIncome', 
			'ebitda', 
			'depreciationAndAmortization', 
			'interestExpense', 
			'incomeTaxExpense', 
			'operatingIncome',
			'totalAssets',
			'totalLiabilities',
			'totalCurrentAssets',
			'totalCurrentLiabilities',
			'totalNonCurrentAssets',
			'shortTermDebt',
			'longTermDebt',
			'cashAndShortTermInvestments',
			'retainedEarnings',
			'operatingCashFlow',
			'capitalExpenditure',
			'dividendsPaid',
			'commonStockRepurchased',
			'changeInWorkingCapital',
			'netCashProvidedByOperatingActivities',
			'commonStockIssued',
			'capitalExpenditure',
			'freeCashFlow',
			'propertyPlantEquipmentNet']
		mydict = tickers_quote
		frame = pd.DataFrame(tickers_quote, columns = entered_tickers.split(","), index=index_for_dataframe)
		print('Frame is '+str(frame)) 
		if(len(entered_tickers) > 1):
			f = open("saved_data/dataframe/"+entered_tickers.replace(',','_')+"_cashflowcalculator.log","w")
			print(frame,file = f)
			frame.to_csv(r'saved_data/csv/'+entered_tickers.replace(',','_')+'_cashflowcalculator.csv', index = index_for_dataframe)
		print('-- CashFlowCalculator printed on files for: '+entered_tickers)



	def StockScreener_click(self):  
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		marketcap_high= self.textTicker2.get()
		marketcap_low =self.textTicker3.get()
		beta_high = self.textTicker4.get()
		beta_low = self.textTicker5.get()
		dividend_high = self.textTicker6.get()
		dividend_low = self.textTicker7.get()
		sector = self.textTicker8.get()
		industry = self.textTicker9.get()
		exchange = self.textTicker10.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT StockScreener_click ---- Selected criteria are are: '+marketcap_high+' '+marketcap_low+' '+beta_high+' '+beta_low+' '+dividend_high+' '+dividend_low+' '+sector+' '+industry+' '+exchange)
		Quote = Analyses('stockscreener',period = entered_years,api_key =self.apikey, statistic = ' ')
		criteria_list = [marketcap_high,marketcap_low,beta_high,beta_low,dividend_high,dividend_low,sector,industry,exchange]
		Quote.Stock_screener(criteria_list) 
		#Thoise values are evaluated at the latest date YieldSearch_click



	def YieldSearch_click(self):
		marketcap_high= self.textTicker2.get()
		marketcap_low =self.textTicker3.get()
		beta_high = self.textTicker4.get()
		beta_low = self.textTicker5.get()
		dividend_high = self.textTicker6.get()
		dividend_low = self.textTicker7.get()
		sector = self.textTicker8.get()
		industry = self.textTicker9.get()
		exchange = self.textTicker10.get()
		targetYield = self.textYield.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT Yeld finder click ---- Selected criteria are are: '+marketcap_high+' '+marketcap_low+' '+beta_high+' '+beta_low+' '+dividend_high+' '+dividend_low+' '+sector+' '+industry+' '+exchange)
		Quote = Analyses('stockscreener',period = entered_years,api_key =self.apikey, statistic = ' ')
		criteria_list = [marketcap_high,marketcap_low,beta_high,beta_low,dividend_high,dividend_low,sector,industry,exchange]
		Quote.Stock_screener(criteria_list, 1, targetYield ) #YIELD function is enabled
		#Thoise values are evaluated at the latest date YieldSearch_click Ticker_list_click


	def Ticker_list_click(self):  #TO DO
		print('\n---- CLICK EVENT Ticker_list_click : Ticker list will be listed /saved_data/Ticker_list.csv  ---- ')
		entered_years = self.buttonYears_var.get() 
		Quote = Analyses('list',period = entered_years,api_key =self.apikey, statistic = ' ')
		Quote.Ticker_list() #Get the ticker list

def main ():
	window = tk.Tk()
	#create the window
	app = GUI(window)
	window.mainloop()


if __name__ == '__main__':
	main()



