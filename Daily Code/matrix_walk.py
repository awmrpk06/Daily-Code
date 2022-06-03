num_ways = 0
def Matrix_walk(arr, s_p, col, row, ways):
    if s_p == [col -1, row -1] :
        Matrix_walk.count += 1
        print(ways)
    if s_p[0] < col - 1:
        if  arr[ s_p[1] ][s_p[0] + 1 ] == 0 :
            m_right = [ s_p[0] + 1 , s_p[1] ]
            ways = ways + 'R'
            Matrix_walk(arr, m_right, col, row, ways)
            ways = ways[:-1]
    if s_p[1] < row - 1: 
        if  arr[ s_p[1] + 1  ][s_p[0]] == 0 :
            m_down = [ s_p[0]  , s_p[1] + 1]
            ways = ways + 'D'
            Matrix_walk(arr, m_down, col, row, ways)
    return Matrix_walk.count

matrix = [  [0, 0, 1],
            [0, 0, 1],
            [1, 0, 0]  ]
Matrix_walk.count = 0
if __name__ == "__main__":
    print(Matrix_walk( matrix, [0,0] , len(matrix[0]) ,len(matrix) , ''))
    