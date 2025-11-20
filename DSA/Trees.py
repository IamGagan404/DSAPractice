class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self,root=None):
        self.root = root


def get_node_data(node):
    left_val = input(f"Left value of {node.val}: ")
    if left_val != "NA":
        node.left = Node(left_val)
        get_node_data(node.left)
    
    right_val = input(f"Right value of {node.val}: ")
    if right_val != "NA":
        node.right = Node(right_val)
        get_node_data(node.right)

def build_tree():
    root_val = int(input("Root value: "))
    root = Node(root_val)
    get_node_data(root)
    return root

root = build_tree()

def inorder(node,arr):
    if node is None:
        return None
    inorder(node.left,arr)
    arr.append(node.val)
    inorder(node.right,arr)
    return arr
# print(inorder(root,[]))



def bottomView(root):
#your code goes here
    map = {}
    def helper(node,ind):
        if node == None:
            return
        map[ind] = node.val
        if node.left:
            map[ind-1] = node.left.val
        if node.right:
            map[ind+1] = node.right.val
        if node.left:
            helper(node.left,ind-1)
        if node.right:
            helper(node.right,ind+1)
    helper(root,0)
    print(map)
    return [map[key] for key in sorted(map.keys())]
print(bottomView(root))



