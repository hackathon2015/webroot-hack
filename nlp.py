import enronEmail
import os
import operator
import nltk
import random
from nltk.corpus import brown

path = os.getcwd();
rootDir = path+"\\to_aol"
"""
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        print fname
        """
def analyze(fname):
    (headers,body)=enronEmail.parse_email(rootDir+'\\'+fname)
    text = nltk.word_tokenize(body)
    for item in nltk.pos_tag(text[150:850]):
        if item[1]=='RB' and (item[0] not in RB_u):
            if item[0] in RB.keys():
                RB[item[0]]+=1
            else:
                RB[item[0]]=1

VB={}
NN={}
JJ={}
RB={}
VB_u=[]
NN_u=[]
JJ_u=[]
RB_u=[]

brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
for (word,tag) in brown_news_tagged:
    #print word+" "+tag
    
    if tag=='NOUN' : NN_u.append(word)
    elif tag=='ADJ': JJ_u.append(word)
    elif tag=='ADV': RB_u.append(word)
    elif tag=='VERB' : VB_u.append(word)

size=50

for dirName, subdirList, fileList in os.walk(rootDir):
    """
    for i in range(size):
        fname = random.choice(fileList)
        print fname
        analyze(fname)
    """
    for fname in fileList:
        print fname
        analyze(fname)

print VB

    
