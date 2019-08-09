#opening the file
#read lines
#split the word. (split function)
#counting the frequency of the word.
#updating count.
#print output


#importing the counter module
from collections import Counter
def word_count(filename):  
    with open(filename) as f: #opening the file
        return Counter(f.read().split()) # reading the file and splitting words.
counter = word_count('/home/jerusha/project 5/netlist_counter.v') #location of the file.
for word in counter:
    print( word, ' No of times the word occurs is :', counter[word] ) 
