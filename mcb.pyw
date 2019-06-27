#! python3
# platform = Ubuntu
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save or delete the items in presence of three arguments
# Example : python3 mcb.pyw save <keyword> 
# Example : python3 mcb.pyw del <keyword>
if len(sys.argv) == 3:
	# if conditions agress paste the clipboard items in shelve file.(mcb)
	if sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()

	# if conditions agress delete the allocated item.
	elif sys.argv[1].lower() == 'del':
		try:
			del mcbShelf[sys.argv[2]]
		except:
			print("Keyword '{}' not found!!".format(sys.argv[2]))

# Load keywords or delete all items in presence of two arguments
elif len(sys.argv) == 2:

	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
			pyperclip.copy(str(list(mcbShelf.keys())))
	
	# Load specific values of keyword
	# Example : python3 mcb.pyw <keyword>
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

	# Delete all items from the shelf file 
	elif sys.argv[1].lower() == 'del':
		mcbShelf.clear()

	else:
		print("Keyword '{}' not found!!".format(sys.argv[1]))

mcbShelf.close()
