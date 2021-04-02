import sys
import math


# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to insert a new node in BST
def insert(root, data):
    # 1. If the tree is empty, return a new,
    # single node
    if not root:
        return Node(data)

    # 2. Otherwise, recur down the tree
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)

    # return the (unchanged) node pointer
    return root


# Function to find the node with maximum value
# i.e. rightmost leaf node
def maxValue(root):
    current = root

    # loop down to find the rightmost leaf
    while (current.right):
        current = current.right
    return current.data


# Driver code
if __name__ == '__main__':
    root = None
    root = insert(root, 10)
    root = insert(root, 1)
    root = insert(root, 22)
    root = insert(root, 91)
    root = insert(root, 7)
    print("Maximum value in BST is {}".format(maxValue(root)))
