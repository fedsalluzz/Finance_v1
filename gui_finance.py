import os
import sys
sys.path.append(".")

from analyses import Analyses
import tkinter as tk
from tkinter import *
import pandas as pd

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
		self.buttonBalance.grid(row=8, column=1,sticky = E, pady = 2)
		#Create the button 
		self.buttonIncome = tk.Button(self.frame, text="Income Statement ", fg="black", font="none 9 bold", command=self.IncomeStatement_click)
		self.buttonIncome.grid(row=8, column=2,sticky = W, pady = 2)
		#Create the button
		self.buttonCash = tk.Button(self.frame, text="Cash Flow", fg="black", font="none 9 bold", command=self.CashFlow_click)
		self.buttonCash.grid(row=8, column=3,sticky = W, pady = 2)
		#Create the button
		self.buttonCashFig = tk.Button(self.frame, text="Cash Figures", fg="black", font="none 9 bold", command=self.CashFigures_click)
		self.buttonCashFig.grid(row=10, column=3,sticky = W, pady = 2)
		#Create the button
		self.buttonDebt = tk.Button(self.frame, text="Debt Figures", fg="black", font="none 9 bold", command=self.DebtFigures_click)
		self.buttonDebt.grid(row=9, column=3,sticky = W, pady = 2)
		#Create the button 
		self.buttonANALYZE = tk.Button(self.frame, text="  Analyze  ", fg="black", font="none 9 bold", command=self.ANALYZE_click)
		self.buttonANALYZE.grid(row=11, column=3,sticky = W, pady = 2)
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
			BalanceSheet = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '  ')
			(date,totalCurrentLiabilities, totalCurrentAssets) = BalanceSheet.Get_document_for(ticker,'totalCurrentLiabilities','totalCurrentAssets','balance_sheet' ) 
			(date_2,shortTermDebt, longTermDebt) = BalanceSheet.Get_document_for(ticker, 'shortTermDebt', 'longTermDebt', 'balance_sheet' ) 
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
			CashFlow = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '  ')
			(date,netCashProvidedByOperating, netCashUsedForInvesting) = CashFlow.Get_document_for(ticker,'netCashProvidedByOperatingActivities','netCashUsedForInvestingActivites','cash_flow' ) 
			(date_2,netCashUsedProvidedByFinancing, netChangeInCash) = CashFlow.Get_document_for(ticker, 'netCashUsedProvidedByFinancingActivities', 'netChangeInCash', 'cash_flow' ) 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : netCashProvidedByOperating, 'y2' : netCashUsedForInvesting} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : netCashUsedProvidedByFinancing, 'y2' : netChangeInCash}
			#print(tickers_dict_eps
		CashFlow.title_data = ['netCashProvidedByOperatingActivities','netCashUsedForInvestingActivites','netCashUsedProvidedByFinancingActivities','netChangeInCash']
		plot = CashFlow.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'CashFlow' )




	def CashFigures_click(self):  #TO DO
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT CashFigures ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			CashFigures = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '  ')
			(date,netCashProvidedByOperating, netCashUsedForInvesting) = CashFigures.Get_document_for(ticker,'netCashProvidedByOperatingActivities','netCashUsedForInvestingActivites','cash_flow' ) 
			(date_2,netCashUsedProvidedByFinancing, netChangeInCash) = CashFigures.Get_document_for(ticker, 'netCashUsedProvidedByFinancingActivities', 'netChangeInCash', 'cash_flow' ) 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : netCashProvidedByOperating, 'y2' : netCashUsedForInvesting} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : netCashUsedProvidedByFinancing, 'y2' : netChangeInCash}
			#print(tickers_dict_eps
		CashFigures.title_data = ['netCashProvidedByOperatingActivities','netCashUsedForInvestingActivites','netCashUsedProvidedByFinancingActivities','netChangeInCash']
		plot = CashFigures.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'CashFigures' )





	def DebtFigures_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT DebtFigures ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		print('-- You selected '+str(len(ticker_list))+' tickers \n')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			DebtFigures = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '  ')
			(date,Current_ratio, Debt_to_Assets) = DebtFigures.Get_document_for(ticker, 'currentRatio', 'debtToAssets','metrics') 
			(date_2,bookValuePerShare,debtToEquity) =  DebtFigures.Get_document_for(ticker, 'netDebtToEBITDA', 'debtToEquity','metrics') 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : Current_ratio, 'y2' : Debt_to_Assets} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : bookValuePerShare, 'y2' : debtToEquity}
		DebtFigures.title_data = ['CurrentRatio =\n CurrentAssets/CurrentLiabilities','DebtToAssets =\n STDebts+LTDebts/TotalAssets','netDebtToEBITDA =\n TotalDebt - Cash&Equivalents / EBITDA','debtToEquity =\n TotalLiabilities/ShareholdersEquity']
		plot = DebtFigures.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'DebtFigures' )


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
			IncomeStatement = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = '  ')
			(date,Revenue, NetIncome) = IncomeStatement.Get_document_for(ticker, 'revenue', 'netIncome','income_statement') 
			(date_2,operatingIncome ,ebitda) =  IncomeStatement.Get_document_for(ticker, 'operatingIncome', 'ebitda','income_statement') 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : Revenue, 'y2' : NetIncome} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : operatingIncome , 'y2' : ebitda}
		IncomeStatement.title_data = ['Revenue','NetIncome','OperatingIncome','Ebitda ']
		plot = IncomeStatement.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'IncomeStatement' )
	
	
	def ANALYZE_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT ANALYZE ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		for ticker in ticker_list:
			print('---- Collecting data for '+str(ticker))
			a = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = 'ESP')
			#a.title_data = ['Earning Per Share','netIncomeRatio']
			(date,eps ,netIncomeRatio) = a.Get_document_for(ticker, 'eps', 'netIncomeRatio','income_statement') 
			(date_2,bookValuePerShare,debtToEquity) =  a.Get_document_for(ticker, 'bookValuePerShare', 'roe','metrics') 
			tickers_dict_eps[ticker] = { 'x' : date , 'y1' : eps, 'y2' : netIncomeRatio} 
			tickers_dict_debt[ticker] = { 'x' : date_2 , 'y1' : bookValuePerShare, 'y2' : debtToEquity}
			#self.Click()
		a.title_data = ['Earning Per Share =\n (NetIncome - PreferredDividends)/SharesOutstanding','netIncomeRatio =\n NetIncome/Revenue','bookValuePerShare =\n (TotalEquity-PreferredEquity)/SharesOutstanding','ROE =\n NetIncome/SharholdersEquity']
		print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
		#self.Click(tickers_dict_eps,tickers_dict_debt)
		#print(str(tickers_dict_eps))
		#print(str(tickers_dict_debt))
		plot = a.Multiple_plots(ticker_list, tickers_dict_eps, tickers_dict_debt, 'Analyze')
			






## This function get the RATIOS
	def Click(self, tickers_dict_eps = None, tickers_dict_debt = None ):
		print('-- CLICK FUNCTION, got bunch of values for tickers')
		self.text_real_time.delete("1.0","end")
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get()
		data = {}
		index_for_dataframe = ['PE','PBV','PEG','DIV YiELD','ROE']#+self.title_data
		print(str(index_for_dataframe))
		for ticker in entered_tickers.split(","):
			print(ticker)
			c = Analyses(ticker=ticker,period = entered_years, api_key =self.apikey)
			pe, pbv, peg,div,roe =  c.Ratios()
			self.prova = pe[:4]+'\n'+pbv[:4]+'\n'+peg[:4]+'\n'+div[:4]+'\n'+roe[:4]
			#latest_date = tickers_dict_eps[ticker]['x'][-1]
			#latest_y1 = tickers_dict_eps[ticker]['x'][-1]
			#latest_y2 = tickers_dict_eps[ticker]['x'][-1]
			#latest_y1 = tickers_dict_debt[ticker]['x'][-1]
			#latest_y2 = tickers_dict_debt[ticker]['x'][-1]
			data[ticker] = [pe[:4],pbv[:4],peg[:4],div[:4],roe[:4]]#,latest_date,latest_y1,latest_y2,latest_y1,latest_y2]
			#latest = tickers_dict_eps[ticker]['x'][-1]
		frame = pd.DataFrame(data, columns = entered_tickers.split(","), index=index_for_dataframe)
		#if(len(entered_tickers) > 1):
		#	f = open("saved_data/"+entered_tickers.replace(',','_')+"_datalog.log","w")
		#	print(frame,file = f)
		print('-- RATIOS printed on files for: '+entered_tickers)
		csv =frame.to_csv(r'saved_data/'+entered_tickers.replace(',','_')+'_ratios.csv', header=True, index=['PE','PBV','PEG','DIV YiELD','ROE'], sep='\t', mode='a')
		self.text_real_time.insert(tk.END,self.prova, 'blue')
		#f.close()	
		

def main ():
	window = tk.Tk()
	#create the window
	app = GUI(window)
	app.Click()
	window.mainloop()


if __name__ == '__main__':
	main()



