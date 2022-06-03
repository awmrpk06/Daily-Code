from collections import deque
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
def maxPath( root):
    sum_max = 0
    q = deque()
    if root != None : q.append(root)
    while(len(q) > 0):
        temp = q.popleft()
        if(temp.left != None):
            q.append(temp.left)
            sum_l = temp.data + temp.left.data
            if sum_l > sum_max: sum_max = sum_l
        if(temp.right != None):
            q.append(temp.right)
            sum_r = temp.data + temp.right.data
            if sum_r > sum_max: sum_max = sum_r
        
    return sum_max
root = Node(1)
root.left = Node(9)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(12)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)
 # Constructed Binary tree is:
    #             1
    #           /   \
    #          9     3
    #         /  \    \
    #       4    12   8
    #                 / \
    #                6   7 
print(maxPath(root))