import matplotlib.pyplot as pyplots
import networkx

from pencariJalur import Astar, kamusBeban
from read_input import kamusKoordinat


def membuatGraph(start, goal):
    # Inisialisasi Graph
    G = networkx.Graph()
    # Initialize variables from PathFinder
    alur_terpendek = Astar(start, goal)
    # Jarak
    distance_sum = 0
    for i in range(len(alur_terpendek) - 1):
        distance_sum += kamusBeban[alur_terpendek[i]][alur_terpendek[i + 1]]
    # Bentuk semua nodes
    for nodes in kamusBeban:
        G.add_node(nodes, pos=(kamusKoordinat[nodes]['lat'], kamusKoordinat[nodes]['lng']))
    # Bentuk semua edges
    for nodes in kamusBeban:
        for children in kamusBeban[nodes]:
            G.add_edge(nodes, children, weight=kamusBeban[nodes][children])

    # Posisi
    pos = networkx.get_node_attributes(G, 'pos')
    # Bobot
    labels = networkx.get_edge_attributes(G, 'weight')
    networkx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # Mewarnai node yang dikunjungi
    node_color = []
    for node in G.nodes:
        if node in alur_terpendek:
            node_color.append("red")
        else:
            node_color.append("blue")

    networkx.draw(G, pos, with_labels=True, node_size=1200, node_color=node_color)
    for i in range(len(alur_terpendek)):
        if (i != len(alur_terpendek) - 1):
            print(f"{alur_terpendek[i]} ->", end=" ")
        else:
            print(alur_terpendek[i])
    print(f"Panjang lintasan adalah {distance_sum}")
    pyplots.show()
