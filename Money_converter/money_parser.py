import argparse

def parse_data():
	parser = argparse.ArgumentParser(description = '''
		Convert any money.
		''')

	parser.add_argument('-m', '--money', type = int, required = True,
		help = '''
		Write the amount of money
		''')
	parser.add_argument('-t', '--type', type = str, required = True,
		help = '''
		Write the type of money you want to convert
		''')
	parser.add_argument('-c', '--convert', type = str, required = True,
		help = '''
		Write the type of money you want to get
		''')

	return vars(parser.parse_args())