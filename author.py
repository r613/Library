class Author(object):
	
	def __init__(self,name,email,gender):
		self.name = name
		self.email = email
		self.gender = gender
		self.books = []

	def get_name(self):
		return = self.name

	def get_email(self):
		return = self.email

	def get_gender(self):
		return = self.gender

	def add_books(self,new_book):
		self.books.append(new_book)