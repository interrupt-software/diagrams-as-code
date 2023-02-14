# PyGraphviz
import pygraphviz as pgv
# diagram.py
from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

graph = pgv.AGraph("graph.dot")

nodes = graph.nodes()
edges = graph.edges()

nodes.sort()

dedges = []
dnodes = []

graph_attr = {
    "fontsize": "24",
    "bgcolor": "transparent",
    "labelloc": "t",
    "mode": "neato",
    "size": "16"
}

node_attr = {
    "fontsize": "10",
    "center": "true",
    "beautify": "true",
    "shape": "plaintext"
}

edge_attr = {
    "fontsize": "10",
    "bgcolor": "lightblue",
    "shape": "normal"
}

main_diagram = Diagram("HashiCat Deployment", show=False, direction="RL", filename="graph", outformat="svg", graph_attr=graph_attr, node_attr=node_attr)

with main_diagram:
    for node in nodes:
        node_name = node.get_name().split(' ')[1].replace(" ","")
        shape_attr = node.attr['shape']
        if shape_attr == "box":
            dnodes.append(Custom(node_name, "./icons/sample_01.svg"))
        elif shape_attr == "diamond":
            dnodes.append(Custom(node_name, "./icons/sample_02.svg"))
        elif shape_attr == "note":
            dnodes.append(Custom(node_name, "./icons/sample_03.svg"))
        else:
            dnodes.append(Custom(node_name, "./icons/sample_01.svg")) 
            continue

def find_node(node_list, label):
    for node in node_list:
        if label == node.label:
            return node
    print(label, " not found.")
    return None

for edge in edges:
    edge_01 = edge[0].get_name().split(' ')[1].replace(" ","")
    edge_02 = edge[1].get_name().split(' ')[1].replace(" ","")
    node1 = find_node(dnodes, edge_01)
    node2 = find_node(dnodes, edge_02)
    if not node1 or not node2: 
        print(node1, edge_01, "\t\t", node2, edge_02)
        continue;
    node1 >> node2

main_diagram.render()
