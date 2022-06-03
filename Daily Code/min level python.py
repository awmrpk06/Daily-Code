from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
def minLevelSum(root):
    if root == None:
        return 0
    min_level = curr_level = 0
    min_sum = root.data
    q = deque()
    q.append(root)
    while(len(q) > 0):
        count = len(q)
        sum = 0
        while( count > 0):
            temp = q.popleft()
            sum = sum + temp.data
            if(temp.left != None):
                q.append(temp.left)
            if(temp.right != None):
                q.append(temp.right)
            count -= 1
        if min_sum > sum: min_level = curr_level
        curr_level += 1
    return min_level
root = Node(1)
root.left = Node(-3)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(-12)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)
 # Constructed Binary tree is:
    #              1
    #            /   \
    #          -9      3
    #        /  \      \
    #       4    -12      8
    #                 /   \
    #                6     7 
print( minLevelSum(root) ) 
        