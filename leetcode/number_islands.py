class Solution:
    def printIsland(self, top, bottom, left, right, center):
        list = [top, bottom, left, right]
        numOfZero = 0
        numOfOne = 0
        #print(list)
        #print(f"  {top}  ")
        #print(f"{right}   {center}  {left}")
        #print(f"  {bottom}  ")
        #print(end="\n")
        for i in list:
            if i is not None:
                if int(i) == 1:
                    numOfOne += 1
                if int(i) == 0:
                    numOfZero += 1
        #print("0 :"+str(numOfZero), "1 : "+str(numOfOne))
        if numOfZero > numOfOne:
            return 1
        else:
            return 0

    def numIslands(self, grid):
        print(grid, end="\n\n")
        numberOfIslands = 0
        for i in range(len(grid)):
            #print(grid[i], end="\n\n")
            #print("number of islands equal :" + str(numberOfIslands) + " and the grid is "+ str(i))
            for j in range(len(grid[i])):
                center = grid[i][j]
                #print(i == 0 and j == len(grid[i][j]) - 1)
                #print(len(grid[i]))
                ONE_ISLAND = '1'
                if center == ONE_ISLAND:
                    #print(i, j, end="\n")
                    first_element_first_grid = i == 0 and j == 0
                    last_element_first_grid = i == 0 and j == len(grid[i]) - 1
                    first_element_last_grid = i == len(grid) - 1 and j == 0
                    last_element_last_grid = i == len(grid) - 1 and j == len(grid[i]) - 1

                    if first_element_first_grid:
                        top = 0
                        left = 0
                        right = grid[i][j + 1] if j + 1 < len(grid[i]) else None
                        bottom = grid[i + 1][j] if i + 1 < len(grid) else None
                        numberOfIslands += self.printIsland(top, bottom, left, right, center)
                    if last_element_first_grid:
                        top = 0
                        left = grid[i][j - 1] if grid[i][j - 1] else None
                        right = 0
                        bottom = grid[i + 1][j] if i + 1 < len(grid) else None
                        numberOfIslands += self.printIsland(top, bottom, left, right, center)
                    if first_element_last_grid:
                        top = grid[i - 1][j] if grid[i - 1][j] else None
                        bottom = 0
                        left = 0
                        right = grid[i][j + 1] if j + 1 < len(grid[i]) else None
                        numberOfIslands += self.printIsland(top, bottom, left, right, center)
                    if last_element_last_grid:
                        top = grid[i - 1][j] if grid[i - 1][j] else None
                        bottom = 0
                        right = 0
                        left = grid[i][j - 1] if grid[i][j - 1] else None
                        numberOfIslands += self.printIsland(top, bottom, left, right, center)

                    bottom = grid[i + 1][j] if i + 1 < len(grid) else None
                    top = grid[i - 1][j] if grid[i - 1][j] else None
                    left = grid[i][j - 1] if grid[i][j - 1] else None
                    right = grid[i][j + 1] if j + 1 < len(grid[i]) else None
                    numberOfIslands += self.printIsland(top, bottom, left, right, center)
        return numberOfIslands


solution = Solution().numIslands(
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
)

print(solution, end="\n\n\n")
#
solution_two = Solution().numIslands(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
)

print(solution_two)

#================================================================
#LINK LEETCODE PROBLEM : https://leetcode.com/problems/number-of-islands/
#================================================================