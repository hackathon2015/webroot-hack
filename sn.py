import enronEmail
import os

f = open('history.txt','w')
path = os.getcwd();
rootDir = path+"\\email"
print rootDir
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        #print('\t%s' % fname)
        if fname.endswith('.txt'):
            (headers,body)=enronEmail.parse_email(dirName+'\\'+fname)
            #print fname
            f.write(fname+'\n')
            if 'From' in headers.keys(): f.write(headers['From']+'\n')
            if 'To' in headers.keys(): f.write(headers['To']+'\n')
        

