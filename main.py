from graph import Graph

g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }

G1 = Graph(g)
print(type(G1))
print(f"# of Vertices in the graph = {len(G1.all_vertices())}")
print(f" List of All Vertices in the Graph: \n {G1.all_vertices()}")
print(f"# of Edges in the graph = {len(G1.all_edges())}")
print(f" List of All Vertices in the Graph: \n {G1.all_edges()}")
G1.EdgeCounter()
