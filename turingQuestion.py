# Now change all sentences to a question
import sys
import os
import hashlib
import Queue
import getopt

verbs = dict()
nouns = dict()
prepositions = dict()
articles = dict()
punct = dict()
modal_aux_verb = dict()
intrans_verbs = dict()
rel_pronouns = dict()

def makeDicts():
    with open('dict.txt') as input_file:
        for i, line in enumerate(input_file):
	    line = line.split(' ')
            if line[0] == 'verbs:':
		line.pop(0)
		for j in line:
		    j = j.rstrip('\n')
		    verbs[j] = hashlib.md5(j)
            elif line[0] == 'prepositions:':
                line.pop(0)
                for j in line:
		    j = j.rstrip('\n')
                    prepositions[j] = hashlib.md5(j)
            elif line[0] == 'articles:':
                line.pop(0)
                for j in line:
		    j = j.rstrip('\n')
                    articles[j] = hashlib.md5(j)
            elif line[0] == 'punctuation:':
                line.pop(0)
                for j in line:
		    j = j.rstrip('\n')
                    punct[j] = hashlib.md5(j)
            elif line[0] == 'modal-verb:':
                line.pop(0)
                for j in line:
		    j = j.rstrip('\n')
                    modal_aux_verb[j] = hashlib.md5(j)
            elif line[0] == 'intransitive-verbs:':
                line.pop(0)
                for j in line:
		    j = j.rstrip('\n')
                    intrans_verbs[j] = hashlib.md5(j)
            elif line[0] == 'rel-pronouns:':
                line.pop(0)
                for j in line:
		    j = j.rstrip('\n')
                    rel_pronouns[j] = hashlib.md5(j)
            elif line[0] == 'nouns:':
                line.pop(0)
                for j in line:
		    j = j.rstrip('\n')
                    nouns[j] = hashlib.md5(j)
def updateDict():
	open("dict.txt", "w").close()
	fo = open("dict.txt","w")
	str = 'verbs: '
	for keys in verbs:
		str = str + ' ' + keys.rstrip()
	fo.write(str + '\n')
	str = 'nouns:'
	for keys in nouns:
		str = str + ' ' + keys.rstrip()
	fo.write(str + '\n')
	str = 'prepositions:'
	for keys in prepositions:
		str = str + ' ' + keys.rstrip()
	fo.write(str + '\n')
	str = 'articles:'
	for keys in articles:
		str = str + ' ' + keys.rstrip()
	fo.write(str + '\n')
	str = 'modal-verb:'
	for keys in modal_aux_verb:
		str = str + ' ' + keys.rstrip()
	fo.write(str + '\n')
	str = 'intransitive-verbs:'
	for keys in intrans_verbs:
		str = str + ' ' + keys.rstrip()
	fo.write(str + '\n')
	str = 'rel-pronouns:'
	for keys in rel_pronouns:
		str = str + ' ' + keys.rstrip()
	fo.write(str + '\n')
	fo.close()

def makeQuestion(tape):
    first = ''
    rest = ''
    tape = tape.split(' ')
    for i in tape:
        if i in verbs:
            first = i
        else:
            rest = rest + i + ' '
    print "New: ", first, rest

makeDicts()

options, remainder = getopt.getopt(sys.argv[2:], 'av:an:ap:aa:apunct:amv:ain:arel:', ['addverb','addnoun','addpreposition','addarticle',
		'addpunctuation','addmodal_verb','addintransitive_verb','addrel_pronoun'])

#print 'OPTIONS:', options
for opt, arg in options:
    	#print opt + " " + arg
    	args.split(' ')
	if opt == '-av':
		for j in args:
			verbs[j] = hashlib.md5(j)
	elif opt == '-an':
        	for j in line:
        		nouns[j] = hashlib.md5(j)
	elif opt == '-ap':
		for j in line:
			prepositions[j] = hashlib.md5(j)
	elif opt == '-aa':
    		for j in line:
        		articles[j] = hashlib.md5(j)
	elif opt == '-apunct':
		for j in line:
			punct[j] = hashlib.md5(j)
	elif opt == '-amv':
	        for j in line:
			modal_aux_verb[j] = hashlib.md5(j)
	elif opt == '-ain':
		for j in args:
        		intrans_verbs[j] = hashlib.md5(j)
	elif opt == '-arel':
        	for j in line:
			rel_pronouns[j] = hashlib.md5(j)

paragraph = raw_input('')
sentences = []
tempsen = ''
quote = False

makeDicts()

for c in paragraph:
    if (c == '\"' or c == "\'") and quote == False:
        quote = True
    elif c == '\"' or c == "\'":
        quote = False
    if c == '.' or c == '?' or c == '!' or c == '\n':
        if quote == False:
            tempsen = tempsen + c
            sentences.append(tempsen)
            tempsen = ''
        else:
            tempsen = tempsen + c
    else:
        tempsen = tempsen + c
for i in sentences:
    i.strip()
    print  "Original: ", i
    makeQuestion(i)
updateDict()
