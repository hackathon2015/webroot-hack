import enronEmail
import os
import operator
import networkx as nx
from math import *
import matplotlib.pylab as plt
import itertools as it
from sets import Set

name_dict={}
id_count = 0;
f = open('1.txt','w')
path = os.getcwd();
rootDir = path+"\\email\\1"

def draw_circle_around_clique(clique,coords):
    dist=0
    temp_dist=0
    center=[0 for i in range(2)]
    color=colors.next()
    for a in clique:
        for b in clique:
            temp_dist=(coords[a][0]-coords[b][0])**2+(coords[a][1]-coords[b][1])**2
            if temp_dist>dist:
                dist=temp_dist
                for i in range(2):
                    center[i]=(coords[a][i]+coords[b][i])/2
    rad=dist**0.5/2
    cir = plt.Circle((center[0],center[1]),   radius=rad*1.3,fill=False,color=color,hatch=hatches.next())
    plt.gca().add_patch(cir)
    plt.axis('scaled')
    # return color of the circle, to use it as the color for vertices of the cliques
    return color

def traverse():
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            #print('\t%s' % fname)
            if fname.endswith('.txt'):
                (headers,body)=enronEmail.parse_email(dirName+'\\'+fname)
                if 'From' in headers.keys():
                    surfix = headers['From'].split('@', 1)[-1]
                    name = surfix.split('.',1)[0]
                    if(name=='enron'):
                        #print headers['From']
                        #print(headers['From'].split('@', 1)[0])
                        usr = headers['From'].split('@', 1)[0] 
                        if usr in name_dict.keys():
                            name_dict[usr]+=1
                        else:
                            name_dict[usr]=1
                        
                if 'To' in headers.keys():
                    rec = headers['To'].split(', ')
                    for addr in rec:
                        surfix = addr.split('@',1)[-1]
                        name = surfix.split('.',1)[0] 
                        if(name=='enron'):
                            usr = addr.split('@',1)[0]
                            if usr in name_dict.keys():
                                name_dict[usr]+=1
                            else:
                                name_dict[usr]=1
def gen_edge():
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            #print('\t%s' % fname)
            if fname.endswith('.txt'):
                (headers,body)=enronEmail.parse_email(dirName+'\\'+fname)
                s_id=0
                if 'From' in headers.keys():
                    surfix = headers['From'].split('@', 1)[-1]
                    name = surfix.split('.',1)[0]
                    if(name=='enron'):
                        usr = headers['From'].split('@', 1)[0] 
                        if usr in name_dict.keys():
                            s_id = name_dict[usr]
                        else:
                            continue
                else:
                    continue
                r_id=0        
                if 'To' in headers.keys():
                    rec = headers['To'].split(', ')
                    for addr in rec:
                        surfix = addr.split('@',1)[-1]
                        name = surfix.split('.',1)[0] 
                        if(name=='enron'):
                            usr = addr.split('@',1)[0]
                            if usr in name_dict.keys():
                                r_id = name_dict[usr]
                                if ((s_id,r_id) in edge)==0 and ((r_id,s_id) in edge)==0:
                                    edge.append((s_id,r_id))
                                    
global colors, hatches
colors=it.cycle('bgrcmyk')# blue, green, red, ...
hatches=it.cycle('/\|-+*')
top=20    
traverse()
sorted_name_dict = sorted(name_dict.items(),key=operator.itemgetter(1))
sorted_name_dict = sorted_name_dict[-top-1:-1]
name_dict={}
label={}
edge = []
for t in sorted_name_dict:
    name_dict[t[0]]=id_count
    label[id_count]=t[0]
    id_count+=1
gen_edge()
G=nx.Graph()
for i in range(top):
    G.add_node(i)
G.add_edges_from(edge)
# remember the coordinates of the vertices
coords=nx.spring_layout(G)

# remove "len(clique)>2" if you're interested in maxcliques with 2 edges
cliques=[clique for clique in nx.find_cliques(G) if len(clique)>5]

#draw the graph
#nx.draw(G,pos=coords)
nx.draw_networkx(G,pos=coords,labels=label)
#nx.draw_networkx_edges(G,pos=coords,edgelist=edge)
clique_id=0
for clique in cliques:
    print "Clique "+str(clique_id)+": ",[label[c] for c in clique]
    nx.draw_networkx_nodes(G,pos=coords,nodelist=clique,node_color=draw_circle_around_clique(clique,coords))
    clique_id+=1

plt.show()  




    
