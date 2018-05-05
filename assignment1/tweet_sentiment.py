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
          resscore=0.0
          #encode text
          encode_str = unicode_str["text"].encode('utf-8')
          #replace !, ?, . and ,
          encode_str = encode_str.replace('!',"")
          encode_str = encode_str.replace('?',"")
          encode_str = encode_str.replace('.',"")
          encode_str = encode_str.replace(',',"")
          #lower and split text
          words = encode_str.lower().split()
          for word in words:
          #check dictionary
            if word in scores:
              resscore+=scores[word]
              #convert to float
              resscore+=0.0
          print str(resscore)
      else:
        print 0.0

if __name__ == '__main__':
    main()
