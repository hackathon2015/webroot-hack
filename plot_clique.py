import networkx as nx
from math import *
import matplotlib.pylab as plt
import itertools as it

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

global colors, hatches
colors=it.cycle('bgrcmyk')# blue, green, red, ...
hatches=it.cycle('/\|-+*')

# create a random graph
#G=nx.gnp_random_graph(n=7,p=0.6)
label={}
label[0]='0'
label[1]='1'
label[2]='2'
label[3]='3'
label[4]='4'


G=nx.Graph()
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
edge = [(0,1),(0,2),(0,3),(1,2),(2,3),(3,4)]
G.add_edges_from(edge)
# remember the coordinates of the vertices
coords=nx.spring_layout(G)

# remove "len(clique)>2" if you're interested in maxcliques with 2 edges
cliques=[clique for clique in nx.find_cliques(G) if len(clique)>2]

#draw the graph
#nx.draw(G,pos=coords)
nx.draw_networkx(G,pos=coords,labels=label)
#nx.draw_networkx_edges(G,pos=coords,edgelist=edge)
for clique in cliques:
    print "Clique to appear: ",clique
    nx.draw_networkx_nodes(G,pos=coords,nodelist=clique,node_color=draw_circle_around_clique(clique,coords))

plt.show()
