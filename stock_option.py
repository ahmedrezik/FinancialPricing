import math
from stock_volatility import stock_vol


class stockoption():

	def __init__(self, S0, K, r, T, N, prm):
		"""
		Initialise parameters
		:param S0: initial stock price
		:param K: strike price
		:param r: risk free interest rate per year
		:param T: length of option in years
		:param N: number of binomial iterations
		:param prm: dictionary with additional parameters
		"""
		self.S0 = S0
		self.K = K
		self.r = r
		self.T = T
		self.N = N
		"""
		prm parameters:
		start = date from when you want to analyse stocks, "yyyy-mm-dd"
		end = date of final stock analysis (likely current date), "yyyy-mm-dd"
		tk = ticker label
		div = dividend paid
		sigma = volatility of stock
		is_call = is it a call option, boolean
		eu_option = European or American option, boolean
		"""
		self.tk = prm.get('tk', None)
		self.start = prm.get('start', None)
		self.end = prm.get('end', None)
		self.div = prm.get('div', 0)
		self.vol = stock_vol(self.tk, self.start, self.end)
		self.sigma = self.vol.mean_sigma()
		self.is_call = prm.get('is_call', True)
		self.eu_option = prm.get('eu_option', True)
		'''
		derived values:
		dt = time per step, in years
		df = discount factor
		'''
		self.dt = T/float(N)
		self.df = math.exp(-(r-self.div)*self.dt)
