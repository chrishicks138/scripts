import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import datetime
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
import urllib.request
from bs4 import BeautifulSoup
import time
#response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
#html = response.read()


bad_chars = ['[',']']

class Process():
    def __init__(self, html):
        time = str(datetime.datetime.now())
        
        soup = BeautifulSoup(html,'html5lib')
        
        self.text = soup.get_text(strip = False)
        self.tokens = self.text.split()
        joined_text = " ".join(self.tokens)
        
        self.stop_words = set(stopwords.words('english'))
        self.word_tokens = word_tokenize(self.text)
        
        filtered_sentence = [w for w in self.word_tokens if not w.lower() in self.stop_words]
        
    def parse(self):
        file = './dataset/'+time+'.txt'
        with open(file, "a") as f:
            for w in word_tokens:
                if w not in stop_words:
                    if w not in bad_chars:
                        filtered_sentence.append(w)
                        f.write(w+'')
    def filter(self):

#        fig = plt.figure(figsize = (10,4))
#        plt.gcf().subplots_adjust(bottom=0.15) # to avoid x-ticks cut-off
#        fdist = FreqDist(filtered_sentence)
#        fdist.plot(50, cumulative=False)
#        fig.savefig('freqDist_'+str(datetime.datetime.now())+'.png', bbox_inches = "tight")

