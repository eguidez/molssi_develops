"""
util.py
File containing utility functions
"""

def title_case(sentence): 
	"""
	Convert a string to title case. 

	Parameters
	----------
	sentence : str
		String to be converted to title case

	Returns 
	-------
	title : str
		Sentence converted to title case

	Example
	-------
	>>> title_case("string to be coNverted") 
	'String To Be Converted'
	"""

	words = sentence.split()
	title = ""
	for word in words: 
		title = title + word[0].upper() + word[1:].lower() + " "
	return title
