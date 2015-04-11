import enronEmail
import os
import operator
import networkx as nx
from math import *
import matplotlib.pylab as plt
import itertools as it
import shutil
from sets import Set

name_dict={}
id_count = 0;
f = open('1.txt','w')
path = os.getcwd();
rootDir = path+"\\email\\1"
dst1=path+"\\from_aol"
dst2=path+"\\to_aol"

def traverse():
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            #print('\t%s' % fname)
            if fname.endswith('.txt'):
                (headers,body)=enronEmail.parse_email(dirName+'\\'+fname)
                if 'From' in headers.keys():
                    surfix = headers['From'].split('@', 1)[-1]
                    name = surfix.split('.',1)[0]
                    if(name=='aol'):
                        #print fname
                         shutil.copyfile(rootDir+"\\"+fname,dst1+"\\"+fname)           
                        
                if 'To' in headers.keys():
                    rec = headers['To'].split(', ')
                    for addr in rec:
                        surfix = addr.split('@',1)[-1]
                        name = surfix.split('.',1)[0] 
                        if(name=='aol'):
                            #print fname
                            shutil.copyfile(rootDir+"\\"+fname,dst2+"\\"+fname)

traverse()
