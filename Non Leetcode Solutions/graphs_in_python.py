def addEdges(graph):
    edges=[]
    for node in graph:
        for neighbours in graph[node]:
            edges.append((node,neighbours))
    return edges

def find_path(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath=find_path(graph,node,end,path)
            if newpath:
                return newpath
    return None
    
def shortest_path_bw(graph,start,end,path=[]):
    path+=[start]
    if start==end:
        return path
    if not start in graph:
        return None
    shortest_path=None
    for node in graph[start]:
        if node not in path:
            newpath=shortest_path_bw(graph,node,end,path)
            if newpath:
                if not shortest_path or len(shortest_path)<len(newpath):
                    shortest=newpath
    return shortest

def find_cycle_one_node(graph,start):
    for node in graph[start]:
        if node==start:
            return 1
    return 0

def find_all_paths(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return [path]
    if start not in graph:
        return []
    found_path=[]
    for node in graph[start]:
        if node not in path:
            newpath=find_all_paths(graph,node,end,path)
            if newpath:
                for new in newpath:
                    found_path.append(new)
    return found_path
                
def isolated(graph):
    iso=[]
    for node in graph:
        if len(graph[node])==0:
            iso.append(node)
    return iso

def add_edge(graph,n1,n2):
    if n1 in graph:
        graph[n1].append(n2)
        if n2 in graph:
            graph[n2].append(n1)
        else:
            graph[n2]=[n1]
    else:
        graph[n1]=[n2]
        if n2 in graph:
            graph[n2].append(n1)
        else:
            graph[n2]=[n1]
    return graph

def find_degree(graph,node):
    nei=[]
    c=0
    for i in graph[node]:
        nei.append(i)
        c+=1
    print(nei)
    return c


def graph_connected(graph,start=None,seen_node=None):
    if seen_node==None:
        seen_node=set()
    nodes=list(graph.keys())
    if not start:
        start=nodes[0]
    seen_node.add(start)
    if len(seen_node)<len(nodes):
        for node in graph[start]:
            if node not in seen_node:
                if graph_connected(graph,node,seen_node):
                    return True
    else:
        return true
    return False

graph={'A': ['B','A','C'], 'B': ['C','A'], 'C': ['A', 'D','B'],'D':['C'],'G':[],'P':[]}
'''for i in range(n):
    u,v=input().split()
    if u not in graph:
        graph[u]=[]
    graph[u].append(v)
print(graph)'''

edges=addEdges(graph)
print("The edges of the graph are",edges)

print(find_path(graph,'A','D',path=[]))
print(shortest_path_bw(graph,'A','D',path=[]))

x=find_cycle_one_node(graph,'A')
if x:
    print("Yes it has a cycle")
else:
    print("No cycle")

#Find all paths in the graph
print(find_all_paths(graph,'A','C',path=[]))

#Find all isolated nodes
print(isolated(graph))

#Adding edge
graph=add_edge(graph,'A','E')
print(graph)

#find degree
print(find_degree(graph,'A'))

#isgraph connected
print(graph_connected(graph))

    
    
