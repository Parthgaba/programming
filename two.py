class Problem:
    def __init__(self):
        self.problemId = 0
        self.problemStatement = self.problStatement()
        self.problemSetter = "Uber"

    def problStatement(self):
        return """
        Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

        For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
        """

    def solve(self):
        # this is the solution to the problem 2
        mul = 1
        for i in range(int(input())):
            n = int(input())
            lis = list(map(int,input().split()))
            for j in range(n):
                mul *= lis[j]
            res = [mul]*n
            for x in range(n):
                res[x] //= lis[x]
            print( *res )

    def __str__(self):
        return self.problemName


if __name__ == "__main__":
    P = Problem()
    P.solve()