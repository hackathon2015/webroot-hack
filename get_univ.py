import nltk
from nltk.corpus import brown

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
    
