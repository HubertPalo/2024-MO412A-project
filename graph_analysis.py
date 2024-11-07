import pandas as pd
import networkx as nx

df = pd.read_csv('votacoes.csv')

B = nx.Graph()

parlamentares = set(df['Parlamentar'])
keys          = set(df['KEY'])


B.add_nodes_from(parlamentares, bipartite=0, type='Parlamentar')
B.add_nodes_from(keys, bipartite=1, type='KEY')

for _, row in df.iterrows():
    parlamentar = row['Parlamentar']
    key = row['KEY']
    voto = row['Voto']
    B.add_edge(parlamentar, key, vote=voto)

parlamentar_graph = nx.bipartite.projected_graph(B, parlamentares)

nx.write_gexf(parlamentar_graph, 'parlamentar_graph.gexf')

