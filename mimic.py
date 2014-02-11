#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  f=open(filename,'rU')
  file=f.read()
  f.close()
  
  #creating list
  filelist=file.split()
  #print (filelist)
  
  #creating empty dictionary and empty list for each dictionary
  dictword={}
  prev=''
  
  for w in filelist:
   if prev not in dictword:
    dictword[prev]=[w]   
   else:
    dictword[prev].append(w)
   prev=w
  
  #print (dictword)
  #for d in dictword.keys():
   #print (d,dictword[d])
   
  return dictword


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  kata=word
  kalimat=''
  for i in range(200):
   if kata in mimic_dict:
    katatambah=random.choice(mimic_dict[kata])
    kalimat=kalimat+' '+katatambah
    kata=katatambah
   else:
    katatambah=random.choice(mimic_dict[word])
    kalimat=kalimat+' '+katatambah
    kata=katatambah
  
  return kalimat


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print ('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  newkalimat=print_mimic(dict, '')
  print (newkalimat)


if __name__ == '__main__':
  main()
