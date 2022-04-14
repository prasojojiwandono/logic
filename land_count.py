
grid = [
    ['w','l','w','w','w'],
    ['w','l','w','w','w'],
    ['w','w','w','l','w'],
    ['w','w','l','l','w'],
    ['l','w','w','l','l'],
    ['l','l','w','w','w']
]

def evaluate_land(grid, row, column, visited):
    position = f'{row},{column}'
    if row < 0 or row >= len(grid):
        return False
    if column < 0 or column >= len(grid[0]):
        return False
    if grid[row][column] == 'w':
        return False
    if position in visited:
        return False
    visited.add(position)
    evaluate_land(grid, row-1,column, visited)
    evaluate_land(grid, row+1,column, visited)
    evaluate_land(grid, row,column-1, visited)
    evaluate_land(grid, row,column+1, visited)
    return True

def land_count(grid):
    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    count_land = 0
    for row in range(rows):
        for column in range(columns):
            position = f'{row},{column}'
            if position not in visited:
                if evaluate_land(grid, row, column, visited):
                    count_land += 1
    return count_land

print(land_count(grid))
