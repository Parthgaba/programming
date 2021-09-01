class Problem:
    def __init__(self):
        self.problemId = 0
        self.problemStatement = self.problStatement()
        self.problemSetter = "Stripe"

    def problStatement(self):
        return """
        Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
        
        For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
        
        You can modify the input array in-place.
        """

    def solve(self):
        # Time Complexity O(n)
        # Space Complexity O(1)
        n = int(input())
        lis = list(map(int,input().split()))
        j = 0
        for i in range(n):
            if lis[i] <= 0:
                lis[i], lis[j] = lis[j], lis[i]
                j += 1
        for _ in range(n):
            if (abs(lis[_]) - 1 < n and lis[abs(lis[_]) - 1] > 0):
                lis[abs(lis[_]) - 1] = -lis[abs(lis[_]) - 1]
        for x in range(n):
            if lis[x] > 0 :
                print(x+1)
                break
        else:
            print(n+1)

    def __str__(self):
        return self.problemName


if __name__ == "__main__":
    P = Problem()
    P.solve()