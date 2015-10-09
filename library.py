class Library(object):
	
	def __init__(self,name):
		self.name = name
		self.books = []
		self.authors = []

	def get_name(self):
		return self.name

	def get_books(self):
		return self.books

	def get_author(self):
		return self.authors

	def add_book(self,book):
		self.books.append(book)

	def add_author_(self,author):
		self.books.append(author)
		
	def get_books_count(self):
		return len(self.books)

