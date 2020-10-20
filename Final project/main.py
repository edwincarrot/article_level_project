import re
wordfreq = {}

def getMax():
	maxx = 0
	maxword = ""
	for d in wordfreq:
		if wordfreq[d] > maxx:
			maxx = wordfreq[d]
			maxword = d

	print "max "+maxword
	print maxx

def getScore(filename):
	score = 0
	wordcount = 0
	with open(filename) as file:
		for line in file:
			wordList = line.split(" ")
			for word in wordList:
				w = re.match("[a-zA-Z]+",word)
				if(w is None): 
					continue
				if(w.group() in wordfreq):
					wordcount += 1
					score += wordfreq[w.group()]
	# return score/wordcount
	level = score/wordcount
	if level < 300:
		level = 10
	elif 300 < level < 320:
		level = 9
	elif 320 < level < 340:
		level = 8
	elif 340 < level < 360:
		level = 7
	elif 360 < level < 380:
		level = 6
	elif 380 < level < 400:
		level = 5
	elif 400 < level < 420:
		level = 4
	elif 420 < level < 440:
		level = 3
	elif 440 < level < 460:
		level = 2
	elif level >500:
		level = 1
	return level
		 

def getWordFreq():
	with open("wordfreq.txt") as file:
		for line in file:
			entry = re.match("([a-zA-Z]+): (\d+)",line)
			if(entry is None): 
				continue
			word = entry.group(1)
			wordfreq[word] = int(entry.group(2))


getWordFreq()
print getScore("input.txt")
# getMax()




