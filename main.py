from library import Library

def main():

	# init area
	bet_shemesh = Library("Bet Shemesh")

	# Menu section
	print "welcome to " + bet_shemesh.get_name() + " library"
	print "we have in our library " + str(bet_shemesh.get_books_count()) + " books"
	print "Main Menu:"
	print "1. Enter new author"
	print "2. Enter new book"
	print "3. search for a book by name"
	print "3. search for a book by author"
	print "3. search for a author"
	user_choice = input("Pease enter your choice ==> ")
	if user_choice == 1:
		pass








if __name__ == '__main__':
	main()