import re

# Opening the tab sepearted value file
def dataset(path='word_search.tsv',word_count={}):
	with open(path) as datafile: 
	    for row in datafile:
	    	#splitting it into word and frequency
	        word, frequency = row.split('\t')
	        #inserting into the word_count dictionary where we define key as word and value as frequency
	        word_count.setdefault(word,frequency.replace('\n', ''))
	return word_count


# To get the second item from the given tuple
def takeSecond(elem):
	return elem[1]


# To get the third item from the given tuple	
def takeThird(elem):
	return elem[2]

# This part search and sorts the words based on a match with the search keyword using regex
def search_word(search_string):

	# Regex pattern  -> greedy regex -> Joins a.*?b.*?c
	greedy_pattern = '.*?'.join(search_string.lower())
	# Compile regex.
	regex = re.compile(greedy_pattern)
	# Checks if the current item matches the regex and creating a list of tuples
	random=[(k,int(v),len(k),) for k,v in dataset().items() if regex.search(k)]
	# Sorting with respect to frequency 
	sortedList = sorted(random, key=takeSecond, reverse=True)
	# Sorting with respect to length of the  word 
	sortedList = sorted(random, key=takeThird)

	return([i[0] for i in sortedList[:25]])
