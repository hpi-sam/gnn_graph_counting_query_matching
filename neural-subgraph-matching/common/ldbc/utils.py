from neo4j import GraphDatabase
import networkx as nx
import pickle
import os

# Source from https://stackoverflow.com/questions/59289134/constructing-networkx-graph-from-neo4j-query-result
def graph_from_cypher(results):
    G = nx.Graph()
    nodes = list(results.graph()._nodes.values())
    for node in nodes:
        G.add_node(node.id, #, labels=node._labels, properties=node._properties
        )
    rels = list(results.graph()._relationships.values())
    for rel in rels:
        G.add_edge(rel.start_node.id, rel.end_node.id
        #,key=rel.id, type=rel.type, properties=rel._properties
        )
        #G.add_edge(rel.end_node.id,rel.start_node.id
        #,key=rel.id, type=rel.type, properties=rel._properties
        #)
    return G

def saveGraph(setName, graph, name):
    directory = os.path.dirname('./data/'+setName+'/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    pickle.dump(graph, open('./data/'+setName+'/' + name + '.pkl', 'wb'))

def loadGraph(setName, name):
    return pickle.load(open('./data/'+setName+'/' + name + '.pkl', 'rb'))
