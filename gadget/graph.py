import networkx as nx
from enum import Enum
from outlines import models, generate
from outlines.samplers import greedy, Sampler

class SearchMethod(Enum):
    DFS = "dfs"
    BFS = "bfs"
    BEAM = "beam"
    DIJKSTRA = "dijkstra"
    ASTAR = "astar"

class GraphTool():
    def __init__(self, nodes: pd.DataFrame, edges: pd.DataFrame, sampler: Sampler  = greedy()):

        self.nodes = nodes
        self.edges = edges
        self.sampler = sampler

    def update_graph(self, nodes: pd.DataFrame, edges: pd.DataFrame):
        self.G = self.G.update(nodes, edges)

    def query_graph(self, prompt):

    def choose_search_method(self, prompt):
        generator = generate.choice(self.model, SearchMethod, self.sampler)
    
        method = generator(prompt)

        if method == SearchMethod.BFS:
            return nx.bfs_tree(G, source=start_node)
        elif method == SearchMethod.DFS:
            return nx.dfs_tree(G, source=start_node)
        elif method == SearchMethod.DIJKSTRA:
            return nx.dijkstra_path(G, source=start_node, target=end_node)
        elif method == SearchMethod.ASTAR:
            return nx.astar_path(G, source=start_node, target=end_node)
        else:
            raise ValueError(f"Invalid search method: {method}")

    def add_node(self, node: Component):


