import networkx as nx 
g = nx.Graph()
g.add_node('TP.HCM')
g.add_node('Dong Nai')
g.add_node('Ba Ria Vung Tau')
g.add_node('Lam Dong')
g.add_node('Can Tho')
g.add_node('Long An')
g.add_edge('TP.HCM', 'Ba Ria Vung Tau')
g.add_edge('TP.HCM', 'Long An')
g.add_edge('Dong Nai', 'Lam Dong')
g.add_edge('Dong Nai', 'Ba Ria Vung Tau')
print (g.number_of_nodes())
print (g.number_of_edges())
print (g.nodes())
print (g.edges())
print (g.degree('TP.HCM'))
print (g.degree())
print (list(g.neighbors('TP.HCM')))
g.has_edge('Lam Dong', 'Long An')
try:
    a = nx.shortest_path(g, 'Lam Dong', 'Long An') # đã có mạng lưới đường đi
    print(a)
except:
    print('No path between Lam Dong and Long An')
try:
    a1 = nx.shortest_path(g, 'Lam Dong', 'Can Tho') # hiện tại chưa xây dựng mạng đường đi
    print(a1)
except:
    print('No path between Lam Dong and Can Tho')
g.add_node('Tien Giang')
g.add_edge('Tien Giang', 'Long An')
g.add_edge('Tien Giang', 'Can Tho')
a3 = nx.shortest_path(g, 'Lam Dong', 'Can Tho')# hiện tại đã bổ sung thêm đường đi
print(a3) 
a4 = nx.shortest_path_length(g, 'Lam Dong', 'Ba Ria Vung Tau')
print(a4)
a5 = nx.shortest_path_length(g, 'Dong Nai', 'Ba Ria Vung Tau')
print(a5)
a6 = nx.shortest_path_length(g, 'Lam Dong', 'Long An')
print(a6)