import networkx as nx
import matplotlib.pyplot as plt

# Definición de los módulos principales
modules = ["Usuario", "Menú", "Pedido"]

# Relaciones entre módulos (Usuario -> Menú -> Pedido)
relations = [("Usuario", "Menú"), ("Usuario", "Pedido"), ("Menú", "Pedido")]

def draw_graph(G, title):
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2500, 
            font_size=10, font_weight="bold", edge_color="gray")
    plt.title(title, fontsize=12)
    plt.show()

# 1. Grafo dirigido (DiGraph)
DG = nx.DiGraph()
DG.add_nodes_from(modules)
DG.add_edges_from(relations)
draw_graph(DG, "1. Grafo dirigido (DiGraph)")

# 2. Grafo dirigido múltiple (MultiDiGraph)
MDG = nx.MultiDiGraph()
MDG.add_nodes_from(modules)
MDG.add_edges_from(relations + [("Usuario", "Menú")])  # ejemplo: relación duplicada
draw_graph(MDG, "2. Grafo dirigido múltiple (MultiDiGraph)")

# 3. Grafo no dirigido (Graph)
UG = nx.Graph()
UG.add_nodes_from(modules)
UG.add_edges_from(relations)
draw_graph(UG, "3. Grafo no dirigido (Graph)")

# 4. Grafo no dirigido múltiple (MultiGraph)
MUG = nx.MultiGraph()
MUG.add_nodes_from(modules)
MUG.add_edges_from(relations + [("Menú", "Pedido")])  # ejemplo: relación duplicada
draw_graph(MUG, "4. Grafo no dirigido múltiple (MultiGraph)")
