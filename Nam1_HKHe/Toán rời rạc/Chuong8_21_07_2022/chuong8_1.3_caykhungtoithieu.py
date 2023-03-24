import networkx as nx 
g = nx.Graph() 
g.add_node('TP.HCM') 
g.add_node('Dong Nai') 
g.add_node('Ba Ria Vung Tau') 
g.add_node('Lam Dong') 
g.add_node('Can Tho') 
g.add_node('Long An') 
g.add_node('Tien Giang') 
g.add_edge('TP.HCM', 'Dong Nai', weight = 50) 
g.add_edge('TP.HCM', 'Ba Ria Vung Tau', weight = 120) 
g.add_edge('TP.HCM', 'Long An', weight = 40) 
g.add_edge('Dong Nai', 'Lam Dong', weight = 230) 
g.add_edge('Dong Nai', 'Ba Ria Vung Tau', weight = 60) 
g.add_edge('Tien Giang', '29') # lệnh gõ nhầm 
g.remove_edge('Tien Giang', '29') # xóa lệnh gõ nhầm 
g.add_edge('Tien Giang', 'Long An') #lệnh gõ thiếu chiều dài (trọng số, weight) 
g.remove_edge('Tien Giang', 'Long An') # xóa lệnh gõ thiếu chiều dài 
g.add_edge('Tien Giang', 'Long An', weight = 29) 
g.add_edge('Tien Giang', 'Can Tho', weight = 200) 
g.add_edge('Long An', 'Dong Nai', weight = 70) 
# g.remove_edge('Tien Giang', '29') # lệnh sẽ báo lỗi vì cạnh này đã được xóa trước đó. 
print(g.nodes())
g.remove_node('29') 
print(g.nodes())
print(sorted(g.edges(data=True)))
T = nx.maximum_spanning_tree(g)
print(sorted(T.edges(data=True)))