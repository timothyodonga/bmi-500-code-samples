#!/usr/bin/env python
# coding: utf-8
"""
    Author: Timothy Odonga
    This is a script that was used to analyze the frequencies of words, bigrams, trigrams in a document. 
    This code was part of a previous class undertaken on Natural Language Processisng. 

    The code used for counts using FreqDist(), word_tokenize() was adopted from Chapter 4 of Natural Language Processing
    with Python by Steven Bird, Ewan Klein and suited to the program.

"""

import sys
import nltk, re, pprint
import os, os.path

nltk.download("punkt")


# In[2]:


current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r"data")
if not os.path.exists(final_directory):
    os.makedirs(final_directory)


# In[3]:


# Open the text file
raw_file = sys.argv[1]
with open(raw_file, encoding="utf-8") as fp:
    text_lines = fp.readlines()


# In[4]:


# Remove any content in XML tags
text_lines = [re.sub("<.*>", "<>", text_line) for text_line in text_lines]


# In[5]:


# Convert all text to lowercase
text_lines = [text_line.lower() for text_line in text_lines]


# In[6]:


# Remove all characters other ASCII lowercase, space and carriage returns
text_lines_clean = [re.sub("[^a-z\n\r\ ]", "", text_line) for text_line in text_lines]


# In[7]:


with open("{}/all_clean_small.txt".format(final_directory), "w") as f:
    # with open('all_clean_small.txt', 'w',encoding='utf-8') as f:
    f.write("".join(text_lines_clean))


# In[8]:


# Read the all_clean_small.txt
# Open the text file
with open("data/all_clean_small.txt", encoding="utf-8") as fp:
    text_lines_small = fp.readlines()


# In[9]:


# Create a list for the characters in the string
lines_small_characters = []
for item in text_lines_small:
    lines_small_characters += list(item)


# In[10]:


# Create character bigrams
char_bigrams = nltk.bigrams(lines_small_characters)
fdist_bigrams = nltk.FreqDist(char_bigrams)
char_bigrams_list = [(k, v) for k, v in fdist_bigrams.items()]
char_bigrams_list = sorted(char_bigrams_list, key=lambda tup: tup[1], reverse=True)


# In[11]:


# Create character trigrams
char_trigrams = nltk.ngrams(lines_small_characters, 3)
fdist_trigrams = nltk.FreqDist(char_trigrams)
char_trigrams_list = [(k, v) for k, v in fdist_trigrams.items()]
char_trigrams_list = sorted(char_trigrams_list, key=lambda tup: tup[1], reverse=True)


# In[12]:


# Create a list for the words in the text
lines_small_words = []
# print(lines_small_words[0:5])
for item in text_lines_small:
    lines_small_words += nltk.word_tokenize(item)


# In[13]:


# Create word bigrams
word_bigrams = nltk.bigrams(lines_small_words)
fdist_bigrams_words = nltk.FreqDist(word_bigrams)
word_bigrams_list = [(k, v) for k, v in fdist_bigrams_words.items()]
word_bigrams_list = sorted(word_bigrams_list, key=lambda tup: tup[1], reverse=True)


# In[14]:


# Create word trigrams
word_trigrams = nltk.ngrams(lines_small_words, 3)
fdist_trigrams_words = nltk.FreqDist(word_trigrams)
word_trigrams_list = [(k, v) for k, v in fdist_trigrams_words.items()]
word_trigrams_list = sorted(word_trigrams_list, key=lambda tup: tup[1], reverse=True)


# In[15]:


char_trigram = [
    '"' + item[0][0] + "," + item[0][1] + "," + item[0][2] + "," + str(item[1]) + '"'
    for item in char_trigrams_list
]
char_trigram = [char.replace("\n", "\\n") for char in char_trigram]


# In[16]:


char_bigram = [
    '"' + item[0][0] + "," + item[0][1] + "," + str(item[1]) + '"'
    for item in char_bigrams_list
]
char_bigram = [char.replace("\n", "\\n") for char in char_bigram]


# In[17]:


word_trigram = [
    '"' + item[0][0] + "," + item[0][1] + "," + item[0][2] + "," + str(item[1]) + '"'
    for item in word_trigrams_list
]


# In[18]:


word_bigram = [
    '"' + item[0][0] + "," + item[0][1] + "," + str(item[1]) + '"'
    for item in word_bigrams_list
]


# In[19]:


with open("data/char_bigram.txt", "w", encoding="utf-8") as f:
    for item in char_bigram:
        raw_string = r"{}".format(item)
        f.write("%s" % raw_string)
        f.write("\n")


# In[20]:


with open("data/char_trigram.txt", "w", encoding="utf-8") as f:
    for item in char_trigram:
        raw_string = r"{}".format(item)
        f.write("%s" % raw_string)
        f.write("\n")


# In[21]:


with open("data/word_bigram.txt", "w", encoding="utf-8") as f:
    for item in word_bigram:
        raw_string = r"{}".format(item)
        f.write("%s" % raw_string)
        f.write("\n")


# In[22]:


with open("data/word_trigram.txt", "w", encoding="utf-8") as f:
    for item in word_trigram:
        raw_string = r"{}".format(item)
        f.write("%s" % raw_string)
        f.write("\n")
