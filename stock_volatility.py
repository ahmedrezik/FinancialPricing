import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt



class stock_vol:

	def __init__(self, tk, start, end):
		self.tk = tk
		self.start = start
		self.end = end
		all_data = pdr.get_data_yahoo(self.tk, start=self.start, end=self.end)
		self.stock_data = pd.DataFrame(all_data['Adj Close'], columns=["Adj Close"])
		self.stock_data["log"] = np.log(self.stock_data)-np.log(self.stock_data.shift(1))

	def mean_sigma(self):
		st = self.stock_data["log"].dropna().ewm(span=252).std()
		sigma = st.iloc[-1]
		return sigma




if __name__ == "__main__":
	vol = stock_vol("AAPL", start="2016-01-01", end="2016-03-01")
	test = vol.stock_data["log"].dropna()
	print(test)
	fig = plot_acf(test)
	plt.show()
