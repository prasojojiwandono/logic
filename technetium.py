# for more information about this file you can check https://app.codility.com/programmers/task/max_path_from_the_left_top_corner/


grid = [
    [9,9,7],
    [9,7,2],
    [6,9,5],
    [9,1,2]
]
def technitium(grid, row=0, column=0, memo={}):
    if row < 0 or row >= len(grid):
        return ''
    if column < 0 or column >= len(grid[0]):
        return ''
    if row == len(grid)-1 and column == len(grid[0])-1:
        return str(grid[row][column])
    if memo.get(f'{row},{column}'):
        return memo.get(f'{row},{column}')
    bawah = str(grid[row][column]) + technitium(grid, row+1, column, memo)
    kanan = str(grid[row][column]) + technitium(grid, row, column+1, memo)
   
    if int(bawah) >= int(kanan):
        memo[f'{row},{column}'] = bawah
        return bawah
    if int(kanan)>= int(bawah):
        memo[f'{row},{column}'] = kanan
        return kanan

def sum_tech(grid):
    res = technitium(grid)
   
    return res

def technitium2(grid):
    row = len(grid)
    column = len(grid[0])
    position = '0,0'
    end_position = f'{row-1},{column-1}'
 
    if position == end_position:
        return str(grid[0][0])
    c_row = 0
    c_column = 0
    big_num = str(grid[0][0])
    while(position != end_position):
        kanan = bawah = None
        besar = ''
        print(position)
        if c_row>=0 and c_row<row and c_column+1>=0 and c_column+1<column:
            kanan = grid[c_row][c_column+1]
        if c_row+1>=0 and c_row+1<row and c_column>=0 and c_column<column:
            bawah = grid[c_row+1][c_column]
        
        if kanan is not None and bawah is not None and kanan <= bawah:
            besar = bawah
            c_row = c_row + 1
        elif kanan is not None and bawah is not None and kanan >= bawah:
            besar = kanan
            c_column = c_column + 1
            position = f'{c_row},{c_column}'
        elif kanan is None and bawah:
            besar = bawah
            c_row = c_row + 1
        elif bawah is None and kanan:
            besar = kanan
            c_column = c_column + 1
        position = f'{c_row},{c_column}'
        big_num = big_num + str(besar)
    return big_num

def solution(A):
    res = technitium2(A)
    return res

print(sum_tech(grid))
print(technitium2(grid))


    
