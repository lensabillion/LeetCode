
visited = set()
cnt = 0
def isValid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in visited
def dfs(i, j):
    global cnt
    direction = [(1,0),(0,1)]
    if i == len(grid) - 1 and j == len(grid[0]):
        cnt += 1
        visited.remove((i, j))
        return
    
    for direction in directions:
        next_i = i + direction[0]
        next_j = j + direction[1]
        if isValid(next_i, next_j):
            dfs(next_i, next_j)
            visited.add(next_i, next_j)
    return cnt