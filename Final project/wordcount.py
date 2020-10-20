from collections import Counter
def wordcount(doc):
	word_list = doc.split()
	word_freq = Counter(word_list)
	print word_freq



dlist = open('dlist.txt')
for filename in dlist:
	filename = filename.strip('\n')
	print filename
	doc = open(filename)
	count = wordcount(doc)
	# print doc 
dlist.close()
