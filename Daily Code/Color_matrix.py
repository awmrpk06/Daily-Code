from collections import deque
def C_matrix(matrix, index, color):
    rows = len(matrix)
    cols = len(matrix[0])
    i_color = matrix[index[0]][index[1]]
    q = deque()
    q.append((index[0], index[1]))
    while len(q) > 0 :
        temp = q.popleft()
        if matrix[temp[0]][temp[1]] == i_color :
            matrix[temp[0]][temp[1]] = color
            if temp[0] + 1 < rows:
                q.append( (temp[0] + 1, temp[1] ))
            if temp[1] + 1 < cols: 
                q.append( (temp[0] , temp[1] + 1))
            if temp[0] - 1 >= 0 :
                q.append( (temp[0] - 1, temp[1] ))
            if temp[1] - 1 >= 0 : 
                q.append( (temp[0] , temp[1]- 1 ))           
    return matrix
matrix = [
    ['B', 'B', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['B', 'B' ,'B'] 
]
print(C_matrix(matrix, [2,2], 'G'))