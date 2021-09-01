class Problem:
    def __init__(self):
        self.problemId = 0
        self.problemStatement = self.problStatement()
        self.problemSetter = "Facebook"

    def problStatement(self):
        return """
        Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

        For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

        You can assume that the messages are decodable. For example, '001' is not allowed.
        """

    def solve(self):
        n = int(input())
        string = input()
        res = self.helper(string, n)
        print(res)

    def helper(self, string: str, k: str) -> int:
        if k == 0:
            return 1

        if string[k - 1] == "0":
            return 0

        result = self.helper(string, k - 1)
        if k >= 2:
            if int(string[k - 2 : k]) < 27:
                result += self.helper(string, k - 2)

        return result

    def __str__(self):
        return self.problemName


if __name__ == "__main__":
    P = Problem()
    P.solve()
