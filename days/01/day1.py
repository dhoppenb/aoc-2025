from solution import BaseSolution

class Solution(BaseSolution):

    _day = 1

    def solve1(self, data: list[str]) -> int:
        num_zero = 0

        points_to = 50

        for instruction in data:
            direction = 1 if instruction[:1]=="R" else -1 
            steps = int(instruction[1:])
            
            points_to = (points_to + (direction * steps)) % 100

            if points_to==0:
                num_zero += 1

        return num_zero

    def solve2(self, data: list[str]) -> int:
        num_zero = 0
        points_to = 50

        for instruction in data:
            direction = 1 if instruction[:1]=="R" else -1 
            steps = int(instruction[1:])

            for _ in range(steps):
                points_to += direction
                if points_to == -1:
                    points_to = 99
                elif points_to == 100:
                    points_to = 0
                    num_zero += 1
                elif points_to == 0:
                    num_zero += 1
        return num_zero
