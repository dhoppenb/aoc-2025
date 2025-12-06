from solution import BaseSolution
import logging

class Solution(BaseSolution):

    _day = 4

    # why is this marked as an 'answer to someone else's input' 
    # because it was wrong..
    def solve1_huh(self, data: list[str]) -> int:
        # init neighbors
        neighbors: dict[tuple[int, int], int] = {}
        
        num_rows = len(data)
        for r, row in enumerate(data):
            num_cols = len(row)
            for c, char in enumerate(row):
                if char == "@":

                    #print(f"found @ {r},{c}")
                    # increment #neighbors of neighbors
                    for i in [-1,0,1]:
                        for j in [-1,0,1]:   
                            if i == 0 and j == 0:
                                continue
                            elif r+i < 0 or c+j < 0 or r+i >= num_cols or c+j >= num_rows or data[r+i][c+j] == ".":
                                continue
                            else:
                                n = neighbors.get((r+i, c+j), 0)
                                neighbors[(r+i, c+j)] = n+1
                                #print(f"\t{r+i},{c+j} from {n} to {n+1}")

        resultset = filter(lambda x: x < 4, neighbors.values())

        printable: list[list[int]] = []
        for _ in range(len(data)):
            printable.append([0]*len(data[0]))
        for _, (r,c) in enumerate(neighbors):
            printable[r][c] = neighbors.get((r,c),-1)

        temp: list[str] = []
        for row in printable:
            rowstring = "".join(map(lambda x: str(x) if 0 < x else ".", row))+'\n'


            temp.append(rowstring)
        with open("output.txt", 'w') as f:
            f.writelines(temp)
            f.close()


        return len(list(resultset))



    def get_neighbors(self, data: list[str], r: int, c: int):
        num_rows = len(data)
        num_cols = len(data[0])
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols:
                    yield nr, nc

    def solve1(self, data: list[str]) -> int:
        total = 0
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == "@":
                    neighbor_count = sum(data[nr][nc] == "@" for nr, nc in self.get_neighbors(data, row, col))
                    if neighbor_count < 4:
                        total += 1

        return total

    def solve2(self, data: list[str]) -> int:
        result = 0
        removed = 1

        # do rounds of removal
        # in each round a new_data is constructed with rolls removed
        # keep count of removals as stopping condition and to accumulate into the final result
        while removed > 0:
            
            removed = 0
            new_data: list[str] = []
   
            for row in range(len(data)):
                new_data.append(data[row])

                for col in range(len(data[row])):
                    if data[row][col] == "@":
                        neighbor_count = sum(data[nr][nc] == "@" for nr, nc in self.get_neighbors(data, row, col))
                        if neighbor_count < 4:
                            removed += 1
                            new_list_row = list(new_data[row])
                            new_list_row[col] = "."
                            new_data[row] = "".join(new_list_row)
            data = new_data
            result += removed
            # print(removed)

        return result