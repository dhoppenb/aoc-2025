from solution import BaseSolution

class Solution(BaseSolution):

    _day = 7

    def solve1(self, data: list[str]) -> int:
        grid: list[list[str]] = list(map(lambda x: list(x), data))
        # start beam
        tachions = {grid[0].index('S')}

        width = len(grid[0])
        num_splits = 0

        # for rows 1..n
        for r, row in enumerate(grid):
            if r == 0:
                continue
            new_tachions: set[int] = set()
            # for each tachion from the previous row
            for tachion in tachions:
                if grid[r][tachion] == ".":
                    new_tachions.add(tachion)
                    grid[r][tachion] = '|'
                else: # cell == "^"
                    num_splits += 1
                    left = tachion-1 
                    right = tachion+1
                    if left >= 0:
                        new_tachions.add(left)
                    if right < width:
                        new_tachions.add(right)
            tachions = new_tachions
        
        # print
        # for r in grid:
        #    print(''.join(r))

        return num_splits

    def solve2(self, data:list[str]) -> int:
        grid:list[list[str]] = list(map(lambda x: list(x), data))
        height = len(grid)
        width = len(grid[0])

        S = grid[0].index('S')
        memoization: dict[tuple[int, int], int] = {}

        # DFS through all paths, memoization to keep it fast
        def beam(r: int, c: int, grid: list[list[str]]) -> int:
            # out of bounds
            if not 0 < c < width:
                return 0
            # beam made it till the end
            elif r >= height:
                return 1
            # just passing through
            elif grid[r][c] == ".":
                return beam(r+1, c, grid)
            else: # cell == ^
                if (r,c) in memoization:
                    return memoization[(r,c)]
                else:
                    sum = beam(r+1, c-1, grid) + beam(r+1, c+1, grid)
                    memoization[(r,c)] = sum
                    return sum

        return beam(1,S, grid) + 1

