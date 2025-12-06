from pathlib import Path
import time
import logging

class BaseSolution():

    _day: int

    def __init__(self):
        self.whattodohere = "nothing really"

    def solve1(self, data: list[str]):
        raise NotImplementedError

    def solve2(self, data: list[str]):
        raise NotImplementedError

    def read_data(self, test: bool = False) -> list[str]:

        input_file = Path(
            "days",
            f"{self._day:02}",
            # either the real input or the test input
            "test.txt" if test else "input.txt",
        )
        # fname: str = "test.txt" if test else "input.txt"
        with open(input_file, 'r') as f:
            data: list[str] = f.readlines()

        data = list(map(lambda x: x.rstrip("\n"), data))
        
        return data
    
    def timer(self, f, data, repeats=20) -> tuple[int, float]:
        total_time = 0
        result = 0
        for _ in range(repeats):
            start = time.time_ns()
            result = f(data)
            total_time += time.time_ns() - start
        duration = total_time/repeats
        return (result, duration)

    def test(self) -> None:
        data: list[str] = self.read_data(test=True)
        print(f"Problem 1: {self.solve1(data)}")
        print(f"Problem 2: {self.solve2(data)}")

    def run(self) -> None:
        data: list[str] = self.read_data()
        print(f"Problem 1: {self.solve1(data)}")
        print(f"Problem 2: {self.solve2(data)}")  

    def bench(self) -> None:
        data: list[str] = self.read_data()   
        (result1, t1) = self.timer(self.solve1, data)
        (result2, t2) = self.timer(self.solve2, data)
        print(f"Problem 1: {result1}\tin {t1/1e6:.2f}ms")
        print(f"Problem 2: {result2}\tin {t2/1e6:.2f}ms")          
