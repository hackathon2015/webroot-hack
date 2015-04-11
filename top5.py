import enronEmail
import os
import operator
import matplotlib.pyplot as pyplot

freq={}
f = open('1.txt','w')
path = os.getcwd();
rootDir = path+"\\email\\1"
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        #print('\t%s' % fname)
        if fname.endswith('.txt'):
            (headers,body)=enronEmail.parse_email(dirName+'\\'+fname)
            #if 'From' in headers.keys(): print(headers['From'].split('@', 1)[0])
            if 'To' in headers.keys():
                rec = headers['To'].split(', ')
                for addr in rec:
                    surfix = addr.split('@',1)[-1]
                    name = surfix.split('.',1)[0] 
                    if(name!='enron'):
                        if name in freq.keys():
                            freq[name]+=1
                        else:
                            freq[name]=1

sorted_freq = sorted(freq.items(),key=operator.itemgetter(1))
v=[];
l=[];
for i in range(1,6):
    t = sorted_freq[-i]
    l.append(t[0])
    v.append(t[1])

pyplot.axis("equal")
pyplot.pie(
        v,
        labels=l,
        autopct="%1.1f%%"
        )
pyplot.title("contact with other companies")
pyplot.show()
