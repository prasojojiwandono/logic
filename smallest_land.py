
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
        return 0
    if column < 0 or column >= len(grid[0]):
        return 0
    if grid[row][column] == 'w':
        return 0
    if position in visited:
        return 0
    visited.add(position)
    value = 1 + evaluate_land(grid, row-1,column, visited) + evaluate_land(grid, row+1,column, visited) + evaluate_land(grid, row,column-1, visited) + evaluate_land(grid, row,column+1, visited)
    
    return value

def smallest_land(grid):
    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    small_land = 10**1000
    for row in range(rows):
        for column in range(columns):
            land_size = evaluate_land(grid, row, column, visited)
            if land_size <= small_land and land_size > 0:
                small_land = land_size
    if small_land == 10**1000:
        return 0
    return small_land

print(smallest_land(grid))
