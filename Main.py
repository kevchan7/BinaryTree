
from tree_node import tree_node

def test_btrees(x,y):
    assert x==y


rooted = tree_node(1)
rooted.left = tree_node(4)
rooted.right = tree_node(2)
rooted.right.right = tree_node(3)
print(rooted.preorder_traversal(rooted))
test_btrees(rooted.preorder_traversal(rooted), [1, 4, 2, 3])
print(rooted.postorder_traversal(rooted))
test_btrees(rooted.postorder_traversal(rooted), [4, 3, 2, 1])
print(rooted.inorder_traversal(rooted))
test_btrees(rooted.inorder_traversal(rooted), [4, 1, 2, 3])
rooted.level_order_traversal(rooted)
rooted.inorderiterative(rooted)  # given up

# Setting up a bst
bst = tree_node(8, tree_node(4), tree_node(12))
bst.left.left = tree_node(2, tree_node(1), tree_node(3))
bst.left.right = tree_node(6, tree_node(5), tree_node(7))
bst.right.left = tree_node(10, tree_node(9), tree_node(11))
bst.right.right = tree_node(14, tree_node(13), tree_node(15))

# trying out my bsts
bst.binarysearchtreesearch(rooted, 3)
