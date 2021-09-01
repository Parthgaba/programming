class Problem:
    def __init__(self):
        self.problemId = 0
        self.problemStatement = self.problStatement()
        self.problemSetter = "Google"

    def problStatement(self):
        return """
        Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

        For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
        """

    def solve(self):
        # this is the solution to the problem 1
        self.solution_1()
        self.solution_2()

    def solution_1(self):
        # Time Complexity O(n)
        # Space Complexity O(n)
        for i in range(int(input())):
            n = int(input())
            lis = list(map(int,input().split()))
            k = int(input())
            hash_map = set()
            for i in range(n):
                if k-lis[i] in hash_map:
                    print(True)
                    break
                hash_map.add(lis[i])

    def solution_2(self):
        # Time Complexity O(n+k)
        # Space Complexity O(k)
        for i in range(int(input())):
            n = int(input())
            lis = list(map(int,input().split()))
            k = int(input())
            rem = [0]*k
            for i in range(n):
                if lis[i]<k:
                    rem[lis[i]%k]+=1
            for i in range(1,k//2):
                if (rem[i]>0 and
                        rem[k-i]>0):
                    print(True)
                    break
            if i>=k//2:
                if k%2==0:
                    if rem[k//2]>1:
                        print(True)
                    else:
                        print(False)
                else:
                    if (rem[k//2] > 0 and
                            rem[k - k // 2 ] > 0):
                        print(True)
                    else:
                        print(False)

    def __str__(self):
        return self.problemName


if __name__ == "__main__":
    P = Problem()
    P.solve()