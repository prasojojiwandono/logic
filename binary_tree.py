import ipdb
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def menjabar_node(root):
    if root is None:
        return []
    stack = []
    urutan = []
    stack.append(root)
    while len(stack)>0:
        current = stack.pop()
        urutan.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return urutan

def menjabar_node2(root):
    if root is None:
        return []
    left_branch = menjabar_node2(root.left)
    right_branch = menjabar_node2(root.right)
    return [root.val] + left_branch + right_branch

def breadth_first_values(root):
    if root is None:
        return []
    queue = []
    urutan = []
    queue.append(root)
    while queue:
        current = queue.pop(0)
        urutan.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return urutan
        
def search_value_in_tree(value, root):
    if root is None:
        return False
    elif root.val == value:
        return True
    
    if search_value_in_tree(value, root.left) or search_value_in_tree(value, root.right):
        return True

node1 = Node(5)
node2 = Node(11)
node3 = Node(3)
node4 = Node(4)
node5 = Node(2)
node6 = Node(1)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

def tree_sum(root):
    if root is None:
        return 0
    sum = root.val + tree_sum(root.right) + tree_sum(root.left)
    return sum

def tree_minimum(root):
    if root is None:
        return None
    left_branch = tree_minimum(root.left)
    right_branch = tree_minimum(root.right)
    if left_branch is None and right_branch is None:
        return root.val
    elif left_branch is None:
        return min(root.val, right_branch)
    elif right_branch is None:
        return min(root.val, left_branch)
    else:
        return min(root.val, left_branch, right_branch)

def max_sum_root_leaf(root):
    if root is None:
        return 0
    left_branch = root.val + max_sum_root_leaf(root.left)
    right_branch = root.val + max_sum_root_leaf(root.right)
    return max(left_branch, right_branch)


aa = menjabar_node(a)
bb = menjabar_node2(a)
cc = breadth_first_values(a)
dd = search_value_in_tree('e',a)
ee = tree_sum(node1)
ff = tree_minimum(node1)
gg = max_sum_root_leaf(node1)
print(aa)
print(bb)
print(cc)
print(dd)
print(ee)
print(ff)
print(gg)