import networkx as nx
import matplotlib.pyplot as plt


def get_triples(file_name):
    triples = []
    file = open(file_name, 'r')
    for lines in file:  # a,b,c;d,e,f
        new_line = lines.rstrip()
        tri_list = new_line.split(';')  # ['a,b,c', 'd,e,f']
        for triple in tri_list:  # a,b,c
            single_triple = triple.split(',')
            triples.append(single_triple)
    return triples


def printGraph(triples):
    G = nx.DiGraph()
    for triple in triples:
        G.add_node(triple[0])
        G.add_node(triple[1])
        G.add_node(triple[2])
        G.add_edges_from([(triple[0], triple[1]),(triple[1],triple[2])])

    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw_networkx(G, pos, edge_color='black', width=1, linewidths=1,
                     node_size=500, font_size=8, node_color='seagreen',
                     alpha=0.8, arrows=True, arrowstyle='-|>', arrowsize=10,
                     labels={node: node for node in G.nodes()})
    plt.axis('off')
    plt.show()


def main():
    # change filename here
    triplets = get_triples('testtriple.txt')
    printGraph(triplets)


if __name__ == '__main__':
    main()
