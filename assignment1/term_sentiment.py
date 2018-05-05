import sys
import json
import string

importar dicionário AFINN

elaborar dicionário Non_sentiment_words {term,[media_positiva, media_negativa]}

para cada tweet (com texto, em ingles):
  para cada palavra em non_sentiment_words:
    se a palavra estive no tweeet:
      se houver scores>0:
        média positiva += soma scores>0/contagem scores>0
      se houver scores<0:
        média negativa += soma scores<0/contagem scores<0
      print palavra, ' ', média positiva - média negativa

set punctuations = set(string.punctuation)


def cleanup(raw_text):
    cleaned_up = ""
    for char in raw_text:
       if char not in punctuations:
           cleaned_up = cleaned_up + char
    return cleaned_up

def main():

    # Importar dicionário AFINN
    afinnfile = open ("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    tweets = open(sys.argv[1])
    for line in tweets: #convert the line from file into a json object
      unicode_str = json.loads(line) #check language
      if 'lang' in unicode_str.keys() and unicode_str["lang"]=='en': #check text
        if 'text' in unicode_str.keys(): #encode text
          encode_str = unicode_str["text"].encode('utf-8') #remover pontuações
          encode_str = cleanup(encode_str)
          words = encode_str.lower().split() #lower and split text
          for word in words: #check dictionary
            if word in scores:
              resscore+=scores[word] #convert to float
              resscore+=0.0
          print str(resscore)
      else:
        print 0.0

if __name__ == '__main__':
    main()
