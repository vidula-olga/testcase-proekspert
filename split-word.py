import sys
wordcount={}
nyanya=[]
def oliacuts(word,i):
        return [ word[beginlen:endlen] for beginlen in range(i+1) for endlen in range(i+1,len(word)+1)]
file=open(sys.argv[1],"r+")
for word in file.read().split():
        letter=list(word)
        b = len(word)
        a = len(letter)
        i = 3 
        ololocut=oliacuts(word,i)
        for word1 in ololocut:
				nyanya 		
                if len(word1)>3:
                        print word1
file.close();