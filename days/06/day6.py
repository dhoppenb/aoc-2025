from solution import BaseSolution
import re
import functools
import itertools

class Solution(BaseSolution):

    _day = 6

    def solve1(self, data: list[str]) -> int:
        numbers: list[list[int]] = []
        operators: list[str] = []
        for i in range(len(data)):
            if i == len(data)-1:
                pattern = re.compile(r"[+|*]")
                operators = pattern.findall(data[i])
            else:
                pattern = re.compile(r"\d+")
                row = data[i]
                numbers.append(pattern.findall(row))

        # tranpose and cast to int
        numbers_t: list[list[int]] = []
        num_rows = len(numbers)
        num_cols = len(numbers[0])
        for _ in range(num_cols):
            numbers_t.append([0]*num_rows)
        for r, row in enumerate(numbers):
            for c, col in enumerate(row):
                numbers_t[c][r] = int(numbers[r][c])

        result = 0
        for i, problem in enumerate(numbers_t):
            if operators[i] == "+":
                result += functools.reduce(lambda x, y: x+y, problem)
            elif operators[i] == "*":
                result += functools.reduce(lambda x, y: x*y, problem)
            

        return result

    # at least now the weird indentation in input has been cleared up...
    def solve2(self, data: list[str]) -> int:
        numbers = data[:-1]

        operators = data[-1]
        pattern = re.compile(r"[+|*]")
        operators = pattern.findall(operators)

        #transpose-ish to get numbers
        numbers_t = [''.join(s) for s in zip(*numbers)]
        # print(numbers_t)

        result = 0
        for operator in operators:
            numbers_str = itertools.takewhile(lambda x: not x.isspace(), numbers_t)
            numbers_t = list(itertools.dropwhile(lambda x: not x.isspace(), numbers_t))
            if len(numbers_t) > 0:
                # pop the whitespace in between number groups, unless we are done
                numbers_t.pop(0)

            numbers = list(map(lambda x: int(x), numbers_str))
            
            if operator == "+":
                result += functools.reduce(lambda x,y: x+y, numbers)
            elif operator == "*":
                result += functools.reduce(lambda x,y : x*y, numbers)

        return result