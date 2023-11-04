import networkx as nx

# Create the map graph
G = nx.Graph()
G.add_edges_from([('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), ('NT', 'Q'), ('SA', 'Q'), ('SA', 'NSW'), ('SA', 'V'), ('Q', 'NSW')])

# Solve the map coloring problem
coloring = nx.greedy_color(G, strategy='largest_first')

print(coloring)
