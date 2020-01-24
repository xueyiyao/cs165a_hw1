import numpy as np
from collections import OrderedDict
import itertools
import operator


# Hint: You may want to use "ISO-8859-1" encoding in open(filename, encoding="ISO-8859-1").

def generate_word_collection(file_name):
  '''
  @input:
    file_name: a string. should be either "training.txt" or "texting.txt"
  @return:
    word_collection: a dict. The (key,value) pair should be (word,count), where the count is how many times the word appears in a given file.
  '''
  f = open(file_name, encoding='ISO-8859-1') 
  word_collection = OrderedDict()
  for line in f:
    for word in line.split(' '):
      if(not any(i.isdigit() for i in word)):
        if word in word_collection:
          word_collection[word] += 1
        else:
          word_collection[word] = 1

  f.close()
  return word_collection

word_collection = generate_word_collection("training.txt")

def print_top_k(word_collection, k):
  '''
  @input:
    word_collection: a dict. The (key,value) pair should be (word,count), where the count is how many times the word appears in a given file. 
                     Should be used with the output of generate_word_collection(file_name).
    k: a int. Indicate the top-k words to print. Should be 20 in question Q2(c).
  @return:
    None. Result is printed.
  '''
  # Step1: Sort all word in word_collection based on its count, from large to small.
  # TODO
  # Step2: Print the first k elements in the sorted word_collection. 
  # TODO
  #{k: v for k,v in sorted(word_collection.items(), key=lambda item: item[1])}
  y = sorted(word_collection.items(), key=operator.itemgetter(1))
  y.reverse()
  for item in y[:20]:
    print(item)
  #x = itertools.islice(word_collection.items(), 0, 20)
  #for key, value in x:
     # print("\'%s\', %d" % (key, value))
     
  #for x in range(20):
   # print(word_collection[x])

print_top_k(word_collection, 20)

"""
Output example:
('the', 190806)
('of', 116447)
('and', 102422)
('to', 89251)
('a', 72558)
('in', 56028)
('i', 45308)
('that', 39378)
('he', 38160)
('it', 34361)
('was', 33834)
('his', 28771)
('Ã¢', 28082)
('with', 25176)
('as', 25032)
('for', 23788)
('is', 22857)
('you', 22808)
('her', 21188)
('had', 20869)
"""
