class Book(object):
	
	def __init__(self,name,author,price):
		self.name = name
		self.author = author
		self.price = price
	
	def get_name(self):
		return self.name
	
	def get_author(self):
		return self.author 
	
	def get_price(self):
		return self.price
	
	def set_price(self,price):
		self.price = price