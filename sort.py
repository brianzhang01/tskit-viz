"""msprime with lexicographic sort
"""
import msprime

# Great parameters! Save them
ts = msprime.simulate(sample_size=10, length=1e6, random_seed=1,
    mutation_rate=1e-8, recombination_rate=1e-6)

# ts.dump('example.trees')

print(ts.draw_text())

def helper(tree, node):
    children = tree.children(node)
    if len(children) == 0:
        return node, [node]
    if len(children) != 2:
        print("That's very interesting, node " + str(node) + " has " + len(children) + " children")
    # List comprehension for elegance
    children_return_values = [helper(tree, child) for child in children]
    children_return_values.sort()
    # print(children_return_values)
    min_lexi = []
    for element in children_return_values:
        min_lexi.extend(element[1])
    return children_return_values[0][0], min_lexi

def lexi(tree):
    """Given a tree, return a list of samples producing this tree that has
    minimum lexicographic order.
    """
    return helper(tree, tree.root)[1]

for tree in ts.trees():
    print(lexi(tree))
