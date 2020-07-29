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
		self.master.geometry("800x500")
		self.master.configure(background="black")
		self.frame = tk.Frame(self.master)
		self.prova = 'prova'
		self.apikey = 'c69c0e1c9f3b70a951441dc376b6d400'

		self.textDirectory = tk.Entry(self.frame, width=40, bg="white")
		self.textDirectory.grid(row=2, column=1)
		dir_path = os.path.dirname(os.path.realpath(__file__))
		self.textDirectory.insert(END,dir_path)

		#Create a Label and text entry box  for ticker
		self.labelTk = tk.Label (self.frame, text=" Selected symbol ", bg="black" , fg="white", font="none 12 bold") .grid(row=3, column=0,sticky = W, pady = 2)

		self.textTicker = tk.Entry(self.frame, width=40, bg="white")
		self.textTicker.grid(row=3, column=1)
		initial_ticker_fill = 'AAPL'
		self.textTicker.insert(END,initial_ticker_fill)
		
		#Create a Label with the Real Time evaluator
		self.label_real_time = tk.Label (self.frame, text="PE\nPBV\nPEG\nDIV\nROE\n", bg="black" , fg="white") .grid(row=4, column=2,sticky = E, pady = 1)
		self.text_real_time = tk.Text (self.frame, height = 5, width = 10)
		self.text_real_time.insert(tk.END,self.prova, 'blue')
		self.text_real_time.grid(row=4, column=3,sticky = W, pady = 2)
		
		#Create a Label and text entry box  for time
		TIME_SPAN = [
			("1Y", "1"),
			("2Y", "2"),
			("5Y", "5"),
			("10Y", "10"),
			("MAX", "MAX"),
			]
		i = 4
		self.buttonYears_var = StringVar()
		self.buttonYears_var.set("1") # initialize
		for text, mode in TIME_SPAN:
			i = i+1
			self.buttonYears = tk.Radiobutton(self.frame, text=text ,variable=self.buttonYears_var, value=mode, bg="white" , fg="black")
			self.buttonYears.grid(column=0, row=i,sticky = W, pady = 2)

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
		self.buttonCashFig = tk.Button(self.frame, text="Cash Figures", fg="black", font="none 9 bold", command=self.CashFigures_click)
		self.buttonCashFig.grid(row=10, column=3,sticky = W, pady = 2)
		#Create the button
		self.buttonDebt = tk.Button(self.frame, text="Debt Figures", fg="black", font="none 9 bold", command=self.DebtFigures_click)
		self.buttonDebt.grid(row=9, column=3,sticky = W, pady = 2)
		#Create the button 
		self.buttonANALYZE = tk.Button(self.frame, text="  Analyze  ", fg="black", font="none 9 bold", command=self.ANALYZE_click)
		self.buttonANALYZE.grid(row=11, column=3,sticky = W, pady = 2)
		#Create the button
		self.buttonNOW = tk.Button(self.frame, text="  NOW  ", fg="black", font="none 9 bold", command=self.NOW_click)
		self.buttonNOW.grid(row=12, column=3,sticky = W, pady = 2)
		#Create a Label and text entry box  for Directory
		self.labelDirectory = tk.Label (self.frame, text=" Program Directory ", bg="black" , fg="white", font="none 12 bold") .grid(row=2, column=0,sticky = W, pady = 2)

		self.textDirectory = tk.Entry(self.frame, width=40, bg="white")
		self.textDirectory.grid(row=2, column=1)
		dir_path = os.path.dirname(os.path.realpath(__file__))
		self.textDirectory.insert(END,dir_path)

		#Create a Label and text entry box  for ticker
		self.labelTk = tk.Label (self.frame, text=" Selected symbol ", bg="black" , fg="white", font="none 12 bold") .grid(row=3, column=0,sticky = W, pady = 2)

		self.textTicker = tk.Entry(self.frame, width=40, bg="white")
		self.textTicker.grid(row=3, column=1)
		initial_ticker_fill = 'AAPL'
		self.textTicker.insert(END,initial_ticker_fill)

		#Create a Label and text entry box  for time
		TIME_SPAN = [
			("1Y", "1"),
			("2Y", "2"),
			("5Y", "5"),
			("10Y", "10"),
			("MAX", "MAX"),
			]
		i = 4
		self.buttonYears_var = StringVar()
		self.buttonYears_var.set("1") # initialize
		for text, mode in TIME_SPAN:
			i = i+1
			self.buttonYears = tk.Radiobutton(self.frame, text=text ,variable=self.buttonYears_var, value=mode, bg="white" , fg="black")
			self.buttonYears.grid(column=0, row=i,sticky = W, pady = 2)


		self.frame.pack()
		

############################# CLICK FUNCTIONS ###############################################
#############################################################################################

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


	def CashFigures_click(self):  #TO DO
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT CashFigures ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		#print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			CashFigures = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '  ')
			(date,netCashProvidedByOperating, netCashUsedForInvesting) = CashFigures.Get_document_for(ticker,'netCashProvidedByOperatingActivities','netCashUsedForInvestingActivites',document = 'cash_flow' ) 
			(date_2,netCashUsedProvidedByFinancing, netChangeInCash) = CashFigures.Get_document_for(ticker, 'netCashUsedProvidedByFinancingActivities', 'netChangeInCash', document = 'cash_flow' ) 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : netCashProvidedByOperating, 'y2' : netCashUsedForInvesting} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : netCashUsedProvidedByFinancing, 'y2' : netChangeInCash}
			#print(tickers_dict_eps
		CashFigures.title_data = ['netCashProvidedByOperatingActivities','netCashUsedForInvestingActivites','netCashUsedProvidedByFinancingActivities','netChangeInCash']
		plot = CashFigures.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'CashFigures' )


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
			IncomeStatement = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '%')
			(date,grossProfitRatio, operatingIncome) = IncomeStatement.Get_document_for(ticker, 'grossProfitRatio', 'operatingIncomeRatio',document = 'income_statement') 
			(date_2,returnOnTangibleAssets ,roic) =  IncomeStatement.Get_document_for(ticker, 'returnOnTangibleAssets', 'roic',document = 'metrics') 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : grossProfitRatio, 'y2' : operatingIncome} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : returnOnTangibleAssets , 'y2' : roic}
		IncomeStatement.title_data = ['grossProfitRatio','operatingIncomeRatio','returnOnTangibleAssets','roic ']
		plot = IncomeStatement.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'Profitability' )



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

	
	
	def ANALYZE_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT ANALYZE ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			a = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '')
			#a.title_data = ['Earning Per Share','netIncomeRatio']
			(date,eps ,netIncomeRatio) = a.Get_document_for(ticker, 'epsdiluted', 'netIncomeRatio',document = 'income_statement') 
			(date_2,bookValuePerShare,roe) =  a.Get_document_for(ticker, 'bookValuePerShare', 'roe', document = 'metrics') 
			(date_2,dividendYield,roe ) =  a.Get_document_for(ticker, 'dividendYield', 'roe', document = 'metrics')
			for k in range (0, len(dividendYield)):
				dividendYield[k] = dividendYield[k]*100
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : eps, 'y2' : dividendYield} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : bookValuePerShare, 'y2' : roe}
			#self.Click()
		a.title_data = ['Earning Per Share Diluted =\n (NetIncome - PreferredDividends)/SharesOutstanding','dividendYield %','bookValuePerShare =\n (TotalEquity-PreferredEquity)/SharesOutstanding','ROE =\n NetIncome/SharholdersEquity']
		print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
		click_data = ['EPS' ,'netIncomeRatio','BVPS','ROE']
		self.Click(tickers_dict_eps,tickers_dict_debt,  click_data )
		#print(str(tickers_dict_eps))
		#print(str(tickers_dict_debt))
		plot = a.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'Analyze')
			

	def NOW_click(self):
		tickers_quote= dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get()
		print('\n---- CLICK EVENT  NOW_click ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		print('---- You selected '+str(len(ticker_list))+' tickers')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			Quote = Analyses(ticker,period = entered_years,api_key =self.apikey, statistic = ' ')
			price,priceAvg50,priceAvg200,eps = Quote.Get_quote_for(ticker) 
			print(price+'   '+priceAvg50+'   '+priceAvg200+'   '+eps)
			pe, pbv, peg,div,roe,dividendPayoutRatio =  Quote.Ratios() #return 5 strings
			divXsh_float = float(dividendPayoutRatio)*float(eps)
			divXsh = str(divXsh_float)[:5]
			divYield_float = divXsh_float / float(price)
			divYield = str(divYield_float)[:5]
			latest_ratio_date = Quote.today
			tickers_quote[ticker] = { 'price' : price , 'priceAvg50' : priceAvg50, 'priceAvg200' : priceAvg200,'divYield':divYield,'EPS' : eps ,'Latest Date': latest_ratio_date,'PBV':pbv ,'PE':pe ,'PEG':peg ,'DIV YiELD': div,'ROE':roe,'dividendPayoutRatio': dividendPayoutRatio, 'Dividend per share': divXsh}
		index_for_dataframe = Quote.title_data = ['price','priceAvg50','priceAvg200','divYield','EPS','Latest Date','PBV','PE','PEG','DIV YiELD','ROE','dividendPayoutRatio','Dividend per share']
		print('Dict is '+str(tickers_quote))
		mydict = tickers_quote
		#with open('dict.csv', 'w') as csv_file:  
    		#	writer = csv.writer(csv_file)
    		#	for key, value in mydict.items():
       		#		writer.writerow([key, value])
		frame = pd.DataFrame(tickers_quote, columns = entered_tickers.split(","), index=index_for_dataframe)
		print('Frame is '+str(frame)) 
		if(len(entered_tickers) > 1):
			f = open("saved_data/datalog/"+entered_tickers.replace(',','_')+"_now_click.log","w")
			print(frame,file = f)
			frame.to_csv(r'saved_data/csv/'+entered_tickers.replace(',','_')+'_now_click.csv', index = index_for_dataframe)
		print('-- NOW_click printed on files for: '+entered_tickers)

		




## This function get the RATIOS
	def Click(self, tickers_dict_eps = dict(), tickers_dict_debt = dict(), title_data = [] ):
		print('-- CLICK FUNCTION, got bunch of values for tickers')
		self.text_real_time.delete("1.0","end")
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get()
		data = {}
		print('title data is: '+str(title_data))
		index_for_dataframe = ['LatData','PBV','PE','PEG','DIV YiELD','ROE']+title_data
		print(str(index_for_dataframe))
		latest_d1_y2 = ' '
		latest_d1_y1 = ' '
		latest_d2_y2 = ' '
		latest_d2_y1 = ' '
		for ticker in entered_tickers.split(","):
			print(ticker)
			c = Analyses(ticker=ticker,period = entered_years, api_key =self.apikey,statistic = ' ')
			pe, pbv, peg,div,roe,dividendPayoutRatio =  c.Ratios()
			self.prova = pe[:4]+'\n'+pbv[:4]+'\n'+peg[:4]+'\n'+div[:4]+'\n'+roe[:4]
			#print(type(c.today))
			#print(str(c.today))
			latest_date_ratio = c.today
			#print(str(tickers_dict_eps))
			#print(type(tickers_dict_eps))
			#print(type(tickers_dict_debt))
			if tickers_dict_eps:
				latest_d1_y1 = tickers_dict_eps[ticker]['y1'][-1]
				latest_d1_y2 = tickers_dict_eps[ticker]['y2'][-1]
				latest_d2_y1 = tickers_dict_debt[ticker]['y1'][-1]
				latest_d2_y2 = tickers_dict_debt[ticker]['y2'][-1]
				d1_y1 = '{:.3f}'.format(latest_d1_y1)
				d1_y2 = '{:.3f}'.format(latest_d1_y2)
				d2_y1 = '{:.3f}'.format(latest_d2_y1)
				d2_y2 = '{:.3f}'.format(latest_d2_y2)
				data[ticker] = [latest_date_ratio,pe[:4],pbv[:4],peg[:4],div[:4],roe[:4],d1_y1,d1_y2,d2_y1,d2_y2]
			else:
				print('No dict to use')
				data[ticker] = [latest_date_ratio,pe[:4],pbv[:4],peg[:4],div[:4],roe[:4]]
		#print(str(latest_date))
		#print(str(data))
		#print(str(index_for_dataframe))
		frame = pd.DataFrame(data, columns = entered_tickers.split(","), index=index_for_dataframe)
		if(len(entered_tickers) > 1):
			f = open("saved_data/datalog/"+entered_tickers.replace(',','_')+"_datalog.log","w")
			print(frame,file = f)
			frame.to_csv(r'saved_data/csv/'+entered_tickers.replace(',','_')+'_simplified_ratios.csv', index = False)
		print('-- RATIOS printed on files for: '+entered_tickers)
		csv =frame.to_csv(r'saved_data/'+entered_tickers.replace(',','_')+'_simplified_ratios.csv', header=True, index=['PE','PBV','PEG','DIV YiELD','ROE'], sep='\t', mode='a')
		self.text_real_time.insert(tk.END,self.prova, 'blue')
		f.close()	
		

def main ():
	window = tk.Tk()
	#create the window
	app = GUI(window)
	app.Click()
	window.mainloop()


if __name__ == '__main__':
	main()



