import collections

f=open(sys.argv[1],"r+")
total_counter=0
wordcount={}
for word in f.read().split():
    if len(word) < 4:
        continue
    total_counter+=1
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print wordcount

for k, v in collections.Counter(wordcount).most_common(10):
    print "%s: %s%%" % (k,v * 100 / total_counter)
f.close()