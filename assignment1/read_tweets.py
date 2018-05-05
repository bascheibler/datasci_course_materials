import sys
import json

def main():

# Define Dictionary
    afinnfile = open ("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items()

    tweets = open(sys.argv[2])
    for line in tweets:
    #convert the line from file into a json object
      unicode_str = json.loads(line)
      #check language
      if 'lang' in unicode_str.keys() and unicode_str["lang"]=='en':
        #check text
        if 'text' in unicode_str.keys():
          print unicode_str["text"].encode('utf-8')

if __name__ == '__main__':
    main()
