import numpy as np
from scipy.sparse import csr_matrix
#from sklearn.linear_model import LogisticRegression
from math import log
import collections
from collections import OrderedDict
import itertools
import operator

def generate_word_collection(file_name):
  '''
  @input:
    file_name: a string. should be either "training.txt" or "texting.txt"
  @return:
    word_collection: a list of all words in the given file, sorted in the alphabetical order.
          Note1: This is slightly different from the interface in Question 2(c).
          Note2: Assuming you have a word collection ['c', 'ab', 'd'], your output should be a sorted list as ['ab', 'c', 'd'].
  '''
  f = open(file_name, encoding='ISO-8859-1')
  #Step1: Generate word_collection
  word_collection = OrderedDict()
  for line in f:
    for word in line.split(' '):
      if(not any(i.isdigit() for i in word)):     
        if word in word_collection:
          word_collection[word] += 1
        else:
          word_collection[word] = 1
        
  f.close()
  # len(word_collection) = 10001
  # Step2: Sort your word_collection alphabetically.
  #TODO
  word_collection = OrderedDict(sorted(word_collection.items(), key=lambda t: t[0]))

  return word_collection
  
# Note that len(word_collection) == 10001. For varifying your code.
word_collection = generate_word_collection("training.txt")
#print(len(word_collection))
#print(word_collection['age'])

"""
Sample result:
['a', 'aa', 'aad', 'ab', 'abandon', 'abandoned', 'abashed', 'abbey', 'abide', 'abiding', ...]

Note: No output are required. Just for varifying your code. Only first few words are printed for reading convenience.
"""


# Question 2(a)
def bag_of_word_encoding(sentence, word_collection):
  """
  @input:
    sentence: a string. Stands for "D" in the problem description. 
              One example is "wish for solitude he was twenty years of age ".
    word_collection: a list. Refer to the output of generate_word_collection(file_name).
  @output:
    encoded_array: a sparse vector based on library scipy.sparse, csr_matrix.
  """
  encoded_array = np.zeros(len(word_collection)).reshape(1, len(word_collection))
  words = sentence.split()
  words.sort()
  for word in words:
    encoded_array[0, tuple(word_collection).index(word)] += 1
   
  encoded_array = csr_matrix(encoded_array)
  
  return encoded_array
  
sentence = "wish for solitude he was twenty years of age "
encoding_array = bag_of_word_encoding(sentence, word_collection)
print(encoding_array)

"""
Sample output:
  (0, 223)	1.0
  (0, 3497)	1.0
  (0, 4086)	1.0
  (0, 5975)	1.0
  (0, 8141)	1.0
  (0, 9234)	1.0
  (0, 9623)	1.0
  (0, 9811)	1.0
  (0, 9963)	1.0
"""

# Question 2(b)
def N_Gram(sentence, N):
  """
  @input:
    sentence: a string. Stands for "D" in the problem description. 
              One example is "wish for solitude he was twenty years of age ".
    N: an integer. Length of N-Gram
  @output:
    collection: a list of all N-grams in the given sentence.
  """
  words = sentence.split()
  
  collection = []
  for i in range(len(words)-N+1):
    str = ""
    for j in range(N):
      if(j < N-1):
        str += words[j+i] + " "
      else:
        str += words[j+i]
    collection.append(str)
  return collection

sentence = "wish for solitude he was twenty years of age "
print(N_Gram(sentence, 3))

"""
Sample output:
['wish for solitude', 'for solitude he', 'solitude he was', 'he was twenty', 'was twenty years', 'twenty years of', 'years of age']
"""

# Question 2(c)
def get_TF(term, document):
  """
  @input:
    term: str. a word (e.g., cat, dog, fish, are, happy)
    document: str. a sentence (e.g., "wish for solitude he was twenty years of age ").
  @output:
    TF: float. frequency of term in the document.
  """
  words = document.split()
  map = OrderedDict()
  for word in words:
    if word in map:
      map[word] += 1
    else:
      map[word] = 1

  num = map[word]
  den = len(words)
  TF = num/den
  return TF

#TF = get_TF("a", "wish for solitude he was twenty years of age a a a b b b a")
#print(TF)

def get_IDF(term, file_name):
  """
  @input:
    term: str. a word (e.g., cat, dog, fish, are, happy)
    file_name: a string. should be either "training.txt" or "texting.txt"
  @output:
    IDF: float. IDF = log_e(Total number of documents / Nmber of documents with term t in it)
  """
  f = open(file_name, encoding='ISO-8859-1')
  total_files = 0
  file_count = 0
  for line in f:
    for word in line.split(' '):
      if(not any(i.isdigit() for i in word)):
        if(term == word):
          file_count += 1
          break
    total_files += 1

  f.close()
  IDF = np.log(total_files/file_count) #TODO
  return IDF

#print(get_IDF("c", "test.txt"))

def get_TF_IDF(term, document, filename):
  """
  @input:
    term: str. a word (e.g., cat, dog, fish, are, happy)
    document: str. a sentence (e.g., "wish for solitude he was twenty years of age ").
    file_name: a string. should be either "training.txt" or "texting.txt"
  @output:
    TF_IDF: float. Equal to TF*IDF.
  """
  TF_IDF =  get_TF(term, document)*get_IDF(term, filename)#TODO
  return TF_IDF

#print(get_TF_IDF("age", "wish for solitude he was twenty years of age ", "training.txt"))

def TF_IDF_encoding(word_collection, filename, document):
  """
  @input:
    word_collection: a list. Refer to the output of generate_word_collection(file_name).
    file_name: a string. should be either "training.txt" or "texting.txt"
    document: str. a sentence (e.g., "wish for solitude he was twenty years of age ").
  @output:
    encoded_array: a sparse vector based on library scipy.sparse, csr_matrix. Contain the TF_IDF_encoding of a given document 
                   (or a single line in the training.txt or testing.txt).
  """
  encoded_array = np.zeros(len(word_collection)).reshape(1, len(word_collection))
  words = document.split()
  words.sort()
  for word in words:
    TF_IDF = get_TF_IDF(word, document, filename)
    if word in word_collection:
      encoded_array[0, tuple(word_collection).index(word)] = TF_IDF

  encoded_array = csr_matrix(encoded_array)
    
  return encoded_array

sentence = "wish for solitude he was twenty years of age "
print(TF_IDF_encoding(word_collection, "training.txt", sentence))

"""
Sample output:
  (0, 223)	0.20907601963956024
  (0, 3497)	0.0002595621997275229
  (0, 4086)	0.008943027879187394
  (0, 5975)	0.00011116670373151355
  (0, 8141)	0.3972834187563259
  (0, 9234)	0.2057232748482032
  (0, 9623)	0.006560282292642595
  (0, 9811)	0.18511202932472162
  (0, 9963)	0.11087359839644073
"""
