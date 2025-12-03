from solution import BaseSolution
import functools

class Solution(BaseSolution):

    _day = 2

    '''
    The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

    Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

    None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

    Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

    11-22 has two invalid IDs, 11 and 22.
    95-115 has one invalid ID, 99.
    998-1012 has one invalid ID, 1010.
    1188511880-1188511890 has one invalid ID, 1188511885.
    222220-222224 has one invalid ID, 222222.
    1698522-1698528 contains no invalid IDs.
    446443-446449 has one invalid ID, 446446.
    38593856-38593862 has one invalid ID, 38593859.
    The rest of the ranges contain no invalid IDs.
    Adding up all the invalid IDs in this example produces 1227775554.
    '''
    def solve1(self, data: list[str]) -> int:
        single_line = data[0]
        unparsed_ranges = single_line.split(',')

        ranges = list(map(lambda x: x.split('-'), unparsed_ranges))

        result = 0
        for range in ranges:
            # first have a look at the ranges
            # print(f"{range}")

            # take the first half (rounded down) of the digits (d1) of range start
            halfway_point = int((len(range[0])/2))
            # edgecase of single digit boundary
            if halfway_point == 0:
                halfway_point = 1
            
            first_half: int = int('1'*halfway_point)
            
            # while d1d1 isn't to large
            while int(str(first_half) + str(first_half)) <= int(range[1]):
                # and d1d1 isn't to small
                if int(str(first_half) + str(first_half)) >= int(range[0]):
                    # then add it to the result
                    # print(f"\t {str(first_half)}, {str(first_half)}")
                    result += int(str(first_half) + str(first_half))
                #d1 += 1
                first_half += 1
        return result
    
    def has_reapting_pattern(self, n: int) -> bool:
        
        n_as_str = str(n)
        halfway_point = int(len(n_as_str)/2)

        for i in range(halfway_point):
            seq = n_as_str[:i+1]
            # how often could seq fit in n?
            (q,r) = divmod(len(n_as_str),len(seq))
            if r > 0:
                continue
            if seq*q == n_as_str:
                return True

        return False

    '''
    Now, an ID is invalid if it is made only of some sequence of digits 
    repeated at least twice. So, 12341234 (1234 two times), 123123123 
    (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) 
    are all invalid IDs.

    From the same example as before:

    11-22 still has two invalid IDs, 11 and 22.
    95-115 now has two invalid IDs, 99 and 111.
    998-1012 now has two invalid IDs, 999 and 1010.
    1188511880-1188511890 still has one invalid ID, 1188511885.
    222220-222224 still has one invalid ID, 222222.
    1698522-1698528 still contains no invalid IDs.
    446443-446449 still has one invalid ID, 446446.
    38593856-38593862 still has one invalid ID, 38593859.
    565653-565659 now has one invalid ID, 565656.
    824824821-824824827 now has one invalid ID, 824824824.
    2121212118-2121212124 now has one invalid ID, 2121212121.
    Adding up all the invalid IDs in this example produces 4174379265.

    What do you get if you add up all of the invalid IDs using these new rules?
    '''
    def solve2(self, data: list[str]) -> int:
        single_line = data[0]
        unparsed_ranges = single_line.split(',')

        ranges = list(map(lambda x: x.split('-'), unparsed_ranges))
        ranges = list(map(lambda x: [int(x[0]), int(x[1])], ranges ))
        
        result = 0
        for r in ranges:
            for i in range(r[0], r[1]+1):
                if self.has_reapting_pattern(i):
                    result += i

        return result
