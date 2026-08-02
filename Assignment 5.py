def dfs(grid, row, col, rows, cols):
    # Check boundary conditions
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return

    # Stop if water or already visited
    if grid[row][col] != '1':
        return

    # Mark current cell as visited
    grid[row][col] = '0'

    # Visit all four directions
    dfs(grid, row - 1, col, rows, cols)  # Up
    dfs(grid, row + 1, col, rows, cols)  # Down
    dfs(grid, row, col - 1, rows, cols)  # Left
    dfs(grid, row, col + 1, rows, cols)  # Right


def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j, rows, cols)

    return count


# Example Grid
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

print("Number of Islands:", num_islands(grid))