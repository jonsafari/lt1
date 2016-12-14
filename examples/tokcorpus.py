#!/usr/bin/python

import os
import sys
import nltk.data
from nltk.tokenize import WordPunctTokenizer

if len(sys.argv) < 3:
    sys.stderr("Syntax: tokcorpus.py inputfile outputfile\n")
    sys.exit(0)

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
wp_tokenizer = WordPunctTokenizer()

with open(sys.argv[1], "r") as inputfile:
    with open(sys.argv[2], "w") as outputfile:
        all_the_lines = ""
        for line in inputfile:
            all_the_lines += line

        sent_tokenized = sent_detector.tokenize(all_the_lines)
        
        wp_tokenized = [wp_tokenizer.tokenize(s) for s in sent_tokenized]

        total_words = 0
        for sentence in wp_tokenized:
            for word in sentence:
                outputfile.write(word.lower() + " ")
                total_words += 1
            outputfile.write("\n")

        print "Total number of lines: " + str(len(sent_tokenized))
        print "Total number of words: " + str(total_words)
