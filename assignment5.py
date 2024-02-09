import uuid

import networkx as nx
import matplotlib.pyplot as plt

from collections import defaultdict


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title=''):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    ax = plt.gca()
    ax.set_title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, ax=ax)
    plt.show()


def visualize_dfs(node, color=0, step=32):
    color_hex = f"#F050{color:02x}"

    node.color = color_hex

    if node.left:
        color = visualize_dfs(node.left, color + step)
    if node.right:
        color = visualize_dfs(node.right, color + step)

    return color


def visualize_bfs(node, color=0, step=32):
    def build_bfs_queue(cur_node, queue=[], visited=[], level=0):
        queue[level].append(cur_node)
        visited.append(cur_node)

        if cur_node.left and cur_node.left not in visited:
            build_bfs_queue(cur_node.left, queue, visited, level + 1)

        if cur_node.right and cur_node.right not in visited:
            build_bfs_queue(cur_node.right, queue, visited, level + 1)

        return queue

    ml_queue = build_bfs_queue(node, defaultdict(list))

    bfs_queue = []
    for i in range(0, len(ml_queue.keys())):
        bfs_queue += ml_queue[i]

    while bfs_queue:
        color_hex = f"#F050{color:02x}"
        color += step
        cur_node = bfs_queue.pop(0)
        cur_node.color = color_hex


if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева
    # draw_tree(root, "Відображення дерева")

    # Відображення DFS обходу
    visualize_dfs(root)
    draw_tree(root, "Відображення DFS обходу")

    # Відображення BFS обходу
    visualize_bfs(root)
    draw_tree(root, "Відображення BFS обходу")

    input()
