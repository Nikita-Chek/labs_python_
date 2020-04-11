import os
import argparse
import re
from collections import Counter
import statistics
from nltk import ngrams

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--k', type=int, help='top k', dest='k', default=10)
parser.add_argument('-n', '--n', type=int, help='n_grams',dest="n", default=4)
args = parser.parse_args()

def interface(_):
        switcher ={
        '1': words_statistic,
        '2': average,
        '3': average_median, 
        '4': top_k_ngrams,
        'exit': 'exit'
        }
        return switcher.get(_)

file = open('additional/for_nine.txt','r')
text = file.read()
file.close()

#1
words = re.findall(r'\w+', text)
words = [i.lower() for i in words]
words_statistic = Counter(words)

#2
sentences = re.split(r'\.', text)
words_in_sentence = []
for _ in sentences:
	words_in_sentence.append(_.count(' ') + 1)
average  = statistics.mean(words_in_sentence)

#3
average_median = statistics.median(words_in_sentence)

#4
all_ngrams = []
for __ in words:
	n_grams = ngrams(__, args.n)
	for _ in n_grams:
		all_ngrams.append(''.join(_))
top_k_ngrams = Counter(all_ngrams).most_common(args.k)

#interface
while True:
	face = input("Choese problem: 1,2,3,4 or type 'exit' to quit: ")
	if interface(face) == 'exit':
		break
	print(interface(face))

