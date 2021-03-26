import sys

for line in sys.stdin:
    line = line.strip()
    #deleting all the whitspace
    try:
        words = line.split(',')[0] + "," + line.split(',')[1]
        #taking only first two columns, source and destination
        # an comma added between two columns for further split
        words = words.split(',')
        #spliting based on comma
    except Exception:
        pass
        
    for word in words:
        if len(word)!=0:
            print('%s\t%s' % (word, 1))
            #emiting the value to reducer as tab separated value
    
    
    
    
    
    
