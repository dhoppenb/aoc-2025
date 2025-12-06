from solution import BaseSolution
import logging

class Solution(BaseSolution):

    _day = 5

    # Can probably just try all ranges as there are only 174 with 1000 or so ingredient IDs
    # solves in avg 6.7ms...
    def solve1(self, data: list[str]) -> int:
        ranges: list[tuple[int, int]] = []
        result = 0
        for row in data:
            if "-" in row:
                split = row.split("-")
                ranges.append((int(split[0]), int(split[1])))
            elif len(row) == 0:
                continue
            else:
                for range in ranges:
                    if range[0] <= int(row) <= range[1]:
                        # Fresh!
                        result += 1
                        break
        return result

    # idea for 1 was, get all ranges
    # merge them until all overlap is removed
    # setup a binary like search per ingredient ID
    # this could use the same approach for range handling
    def solve2(self, data: list[str]) -> int:
        ranges: list[tuple[int, int]] = []
        
        for row in data:
            if "-" in row:
                split = row.split("-")
                ranges.append((int(split[0]), int(split[1])))    
            else:
                break
            
        # sort on range start
        sorted_ranges = sorted(ranges, key=lambda x: x[0])

        has_merged = True
        while has_merged:
            # print(sorted_ranges)
            has_merged = False

            for i in range(len(sorted_ranges)-1):
                r1 = sorted_ranges[i]
                r2 = sorted_ranges[i+1]
                if r1[1] > r2[0]-1:
                    # Merge, emphasis on the max... :P
                    new_range = (r1[0], max(r1[1],r2[1]))
                    sorted_ranges.pop(i)
                    sorted_ranges.pop(i)
                    sorted_ranges.insert(i, new_range)
                    has_merged = True
                    break

        # calculate number of fresh IDs
        result = 0
        for r in sorted_ranges:
            number_of_ids = (r[1]-r[0]+1)
            result += number_of_ids

        return result