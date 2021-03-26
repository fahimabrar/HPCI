from operator import itemgetter
import sys
current_word = None
current_count = 0
word = None
#initializing the variables

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    #getting value in two variables, word and count
    try:
        count = int(count)
        #typecasting count variable into integer
    except ValueError:
        continue

    if current_word == word:
        current_count += count
        #increasing the count based on new simillar word
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word
        #updating the value in each step

if current_word == word:
    print('%s\t%s' % (current_word, current_count))
    #printing the output as tab separated file

