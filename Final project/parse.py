import re
f = open('./test.txt')
lines = f.readlines()
f.close()
d = {}


pattern = '[\.+;:,"?!]'
for line in lines:
	parse = re.sub(pattern, "", line)
	parse = parse.split()
	print parse
	for word in parse:
		if word in d:
			d[word] = d[word] + 1
		else:
			d[word] = 1
print d



# print lines