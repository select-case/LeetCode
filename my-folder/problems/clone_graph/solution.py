"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        dict_graph = {}
        stack = [node]
        while stack:
            current = stack.pop()
            if current:
                if current.val in dict_graph:
                    continue
                else:
                    dict_graph[current.val] = []
                    for i in current.neighbors:
                        dict_graph[current.val].append(i.val)
                        stack.append(i)
        print(dict_graph)
        new_nodes = {}
        for i in dict_graph:
            node = Node(i)
            new_nodes[i] = node
        print(new_nodes)

        for i in dict_graph:
            for j in dict_graph[i]:
                new_nodes[i].neighbors.append(new_nodes[j])
        
        return new_nodes[1]
