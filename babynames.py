#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  file=open(filename)
  fbaby=file.read()
  #for line in file:
   #print (line)
  #listpopularity=[]
  match=re.search(r'Popularity in (\d\d\d\d)',fbaby)
  popularity=match.group(1)
  babynamesrank=re.findall('<tr align="right"><td>([\w.-]+)</td><td>([\w.-]+)</td><td>([\w.-]+)</td>',fbaby,re.IGNORECASE)
  babynamelist=[]
  babynamelist.append(popularity)
  
  for i in range(len(babynamesrank)):
   babynamelist.append(babynamesrank[i][1]+' '+babynamesrank[i][0])
   babynamelist.append(babynamesrank[i][2]+' '+babynamesrank[i][0])
  
  #return babynamesrank
  #return popularity
  babysort=sorted(babynamelist)
  return babysort


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  #for filename in args:
    #names = extract_names(filename)

    # Make text out of the whole list
    #text = '\n'.join(names)

    #if summary:
      #outf = open(filename + '.summary', 'w')
      #outf.write(text + '\n')
      #outf.close()
    #else:
      #print (text)
	  
  for filename in args:
   finalprint=extract_names(filename)
  #print (finalprint[0][0])
  #print (len(finalprint))
  #print(finalprint)
  #for tuple in finalprint:
  for tuple in finalprint:
   print (tuple)
  
if __name__ == '__main__':
  main()
