from solution import BaseSolution
import itertools


class Solution(BaseSolution):

    _day = 3

    """
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    The batteries are arranged into banks; each line of digits in your input corresponds to a 
    single bank of batteries. Within each bank, you need to turn on exactly two batteries; the 
    joltage that the bank produces is equal to the number formed by the digits on the batteries 
    you've turned on. For example, if you have a bank like 12345 and you turn on batteries 
    2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

    You'll need to find the largest possible joltage each bank can produce. In the above example:

    In 987654321111111, you can make the largest joltage possible, 98, 
        by turning on the first two batteries.
    In 811111111111119, you can make the largest joltage possible 
        by turning on the batteries labeled 8 and 9, producing 89 jolts.
    In 234234234234278, you can make 78 
        by turning on the last two batteries (marked 7 and 8).
    In 818181911112111, the largest joltage you can produce is 92.
    The total output joltage is the sum of the maximum joltage from each bank, so in this example, 
    the total output joltage is 98 + 89 + 78 + 92 = 357.

    There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?
    """

    def solve1(self, data: list[str]) -> int:
        # input.txt contains banks of length 100
        # which is short enough to just try everything (5050 options)
        result = 0
        for bank in data:
            max = 0
            for i in range(0, len(bank) - 1):
                for j in range(i + 1, len(bank)):
                    if int(bank[i] + bank[j]) > max:
                        max = int(bank[i] + bank[j])
            result += max
        return result

    '''
    find a subset of length 12, maintaining order, that forms the largest number per bank
    #TODO this doesn't work, 100 choose 12 is way to large
    '''
    def solve2_lazy(self, data: list[str]) -> int:
        # remove newline
        data = list(map(lambda x: x.rstrip(), data))
        result = 0
        for k, bank in enumerate(data):
            print(f"starting on bank {k}")
            max = 0
            combs = itertools.combinations(bank,12)
            for comb in combs:
                subset = ''
                for i in comb:
                    subset += i
                value = int(subset)
                if value > max:
                    max = value
            result += max
        # test value:   3121910778619
        return result

    def solve2(self, data: list[str]) -> int:
        # remove newline
        data = list(map(lambda x: x.rstrip(), data))

        # look at digit 0
        # if digit 0 < digit 1 
        #   drop it
        # elif digit 0 == digit 1
        #   continue with digit 1 and add 1 to the drop count <- hidden choice here
        # else
        #   keep digit 0 and continue to digit 1

        return 0