import os
import sys
sys.path.append(".")

from analyses import Analyses
import tkinter as tk
from tkinter import *

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


		#Create the button calculate the EPS
		self.buttonEPS = tk.Button(self.frame, text="ESP/ESP diluted", fg="black", font="none 12 bold", command=self.EPS_click)
		self.buttonEPS.grid(row=9, column=3,sticky = W, pady = 2)
		#Create the button calculate the BV and DEBT 
		self.buttonDEBT = tk.Button(self.frame, text="BV / DEBT ", fg="black", font="none 12 bold", command=self.BV_DEBT_click)
		self.buttonDEBT.grid(row=10, column=3,sticky = W, pady = 2)
		#Create the button calculate the main parameters 
		self.buttonANALYZE = tk.Button(self.frame, text="  Analyze  ", fg="black", font="none 12 bold", command=self.ANALYZE_click)
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
		
	
	def EPS_click(self):
		self.text_real_time.delete("1.0","end")
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get()
		print('\n---- CLICK EVENT ESP ---- Selected ticker is/are: '+entered_tickers)
		eps_analysis = Analyses(ticker=entered_tickers,period = entered_years,api_key = self.apikey, statistic = 'ESP')
		self.Click()
		eps_analysis.Plot()


	def BV_DEBT_click(self):
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get()
		print('\n~~~~ CLICK EVENT BV_DEBT ~~~~ Selected ticker is/are: '+entered_tickers)
		bv_analysis = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey,statistic='BV_DEBT')
		self.Click()
		bv_analysis.Plot()
	
	def ANALYZE_click(self):
		tickers_dict_eps = dict()
		tickers_dict_debt = dict()
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get() 
		print('\n---- CLICK EVENT ANALYZE ---- Selected ticker is/are: '+entered_tickers)
		ticker_list = entered_tickers.split(',')
		if (len(ticker_list) > 1):
			print('-- You selected '+str(len(ticker_list))+' tickers \n')
			print('---- Collecting EPS and BD and DEBT data for '+ticker_list[0])
			for ticker in ticker_list:
				print('---- Collecting data for '+str(ticker))
				a = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = 'ESP')
				b = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey,statistic='BV_DEBT')
				(x_eps,y1_eps,y2_eps) = a.EPS(ticker,entered_years, financial_api_key) 
				(x_debt,y1_debt,y2_debt) =  b.BV_DEBT(ticker,entered_years, financial_api_key) 
				tickers_dict_eps[ticker] = { 'x' : x_eps , 'y1' : y1_eps, 'y2' : y2_eps} 
				tickers_dict_debt[ticker] = { 'x' : x_debt , 'y1' : y1_debt, 'y2' : y2_debt}
		else:
			
			print('-- You selected '+str(len(ticker_list))+' tickers \n')
			print('---- Collecting EPS and BD and DEBT data for '+ticker_list[0])
			a = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey, statistic = 'ESP')
			b = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey,statistic='BV_DEBT')
			(x_eps,y1_eps,y2_eps) = a.EPS() 
			(x_debt,y1_debt,y2_debt) =  b.BV_DEBT() 
			tickers_dict_eps[ticker_list[0]] = { 'x' : x_eps , 'y1' : y1_eps, 'y2' : y2_eps} 
			tickers_dict_debt[ticker_list[0]] = { 'x' : x_debt , 'y1' : y1_debt, 'y2' : y2_debt}
			print(str(a.title_data + b.title_data))
			title_data = a.title_data + b.title_data
			c = Analyses(ticker=entered_tickers,period = entered_years,api_key =self.apikey,title_data = title_data)
			self.Click()
			c.Plot_statistic(tickers_dict_eps,tickers_dict_debt)

	def Click(self):
		self.text_real_time.delete("1.0","end")
		entered_tickers=self.textTicker.get()
		entered_years = self.buttonYears_var.get()
		c = Analyses(ticker=entered_tickers,period = entered_years, api_key =self.apikey)
		pe, pbv, peg,div,roe =  c.Ratios()
		print('-- Price:'+pe)
		print('-- SHares:'+pbv)
		print('-- PE/Grow:'+peg)
		print('-- Div Yeld:'+div)
		print('-- ROE:'+roe)
		self.prova = pe+'\n'+pbv+'\n'+peg+'\n'+div+'\n'+roe
		print('////// STAMPO ///////')
		self.text_real_time.insert(tk.END,self.prova, 'blue')
		
		

def main ():
	window = tk.Tk()
	#create the window
	app = GUI(window)
	app.Click()
	window.mainloop()


if __name__ == '__main__':
	main()



