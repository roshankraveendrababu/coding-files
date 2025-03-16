from graphviz import Digraph

# Create the recursive tree using Graphviz
tree = Digraph("RecursiveTree")
tree.attr(rankdir="TB", size="10,10")
tree.attr('node', shape='box', style='rounded', fontsize='10')

# Add nodes for the recursive tree
tree.node("root", "dfs(0)")
tree.node("n1", "dfs(1) ['a']")
tree.node("n2", "dfs(2) ['a', 'a']")
tree.node("n3", "dfs(3) ['a', 'a', 'b'] (Add to res)")
tree.node("n4", "dfs(2) ['a', 'ab']")
tree.node("n5", "dfs(3) ['aa', 'b'] (Add to res)")
tree.node("n6", "dfs(3) ['aab']")

# Define edges for the tree
tree.edges([
    ("root", "n1"),  # dfs(0) -> dfs(1) with 'a'
    ("n1", "n2"),    # dfs(1) -> dfs(2) with 'a'
    ("n2", "n3"),    # dfs(2) -> dfs(3) with 'b'
    ("n1", "n4"),    # dfs(1) -> dfs(2) with 'ab'
    ("root", "n5"),  # dfs(0) -> dfs(1) with 'aa'
    ("root", "n6")   # dfs(0) -> dfs(1) with 'aab'
])

tree
