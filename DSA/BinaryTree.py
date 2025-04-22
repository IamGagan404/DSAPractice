class Node:
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# root_val = int(input("Enter root: "))
# root = Node(root_val)

def populate(node):
    res = input("Left?")
    if res == "y":
        val = int(input("val? "))
        node.left = Node(val)
        populate(node.left)
    res = input("right?")
    if res == "y":
        val = int(input("val? "))
        node.right = Node(val)
        populate(node.right)
# populate(root)

######### BST ##############
class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 0

        def get_value(self):
            return self.value

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(value, self.root)

    def _insert(self, value, node):
        if node is None:
            return self.Node(value)

        if value < node.value:
            node.left = self._insert(value, node.left)
        elif value > node.value:
            node.right = self._insert(value, node.right)

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node

    def populate(self, nums):
        for num in nums:
            self.insert(num)

    def populate_sorted(self, nums):
        self._populate_sorted(nums, 0, len(nums))

    def _populate_sorted(self, nums, start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        self.insert(nums[mid])
        self._populate_sorted(nums, start, mid)
        self._populate_sorted(nums, mid + 1, end)

    def display(self):
        self._display(self.root, "Root Node: ")

    def _display(self, node, details):
        if node is None:
            return
        print(f"{details}{node.value}")
        self._display(node.left, f"Left child of {node.value}: ")
        self._display(node.right, f"Right child of {node.value}: ")

    def is_empty(self):
        return self.root is None

    def height(self, node):
        if node is None:
            return -1
        return node.height

    def balanced(self):
        return self._balanced(self.root)

    def _balanced(self, node):
        if node is None:
            return True
        return abs(self.height(node.left) - self.height(node.right)) <= 1 and self._balanced(node.left) and self._balanced(node.right)


bst = BST()
arr = [1,2,3,4,5,6,7,8]
bst.populate_sorted(arr)
bst.display()







