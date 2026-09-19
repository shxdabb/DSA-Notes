# grid = [[1 for _ in range(3)] for i in range(4)]
# # print(grid)

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         print(grid[i][j])
#     # print(_)



# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         print(grid[i][j])




# for i in (grid):
#     for j in i:
#         print(j)

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == 8:
#             print(i,j)
#             break

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


i,j = 0,0

# print(grid[i-1][j],grid[i][j-1],grid[i+1][j],grid[i][j+1])

directions = [(-1,0),(1,0),(0,-1),(0,1)]

# for dr,dc in directions:
#     nr = i + dr
#     nc = j + dc
#     if 0<=nr<=len(grid) and 0<=nc<=len(grid[0]):
#         print(grid[nr][nc]) 

directions = [(-1,0),(1,0),(0,-1),(0,1)]

res = 0
def dfs(i,j):
    for dr,dc in directions:
        nr = i + dr
        nc = j + dc
        if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
            if grid[nr][nc]:
                res +=1
                dfs(nr,nc)

dfs(i,j)
print(res)