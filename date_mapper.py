import sys

for line in sys.stdin:
    word = line.split(',')[-1]
    #spliting the line on comma, that will return a list of words
    #then get the last value of the list, [-1] gives the last value of the list,
    #which is basically the date column
    word = word.replace('\n', '')
    #replacin newline syntax from end of the word
    word = word.strip()
    #replacing any leading or ending blank spaces
    if len(word) != 0:
        print('%s\t%s' % (word, 1))
        #emiting the value to reducer as tab separated value
    
    
    
    
    
