class Library(object):
	
	def __init__(self,name):
		self.name = name
		self.books = []

	def get_books(self):
		return self.books

	def add_book(self,book):
		self.books.append(book)
