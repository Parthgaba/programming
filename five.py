class Problem:
    def __init__(self):
        self.problemId = 0
        self.problemStatement = self.problStatement()
        self.problemSetter = "Jane Street"

    def problStatement(self):
        return """
        cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
        
        Given this implementation of cons:
        
        def cons(a, b):
            def pair(f):
                return f(a, b)
            return pair
        Implement car and cdr.
        """

    def cons(self, a, b):
        def pair(f):
            return f(a, b)
        return pair

    def solve(self):
        fun = self.cons(4, 5)
        def ret(a, b):
            return a, b
        print(fun(ret))
        print(self.car(fun(ret)))
        print(self.cdr(fun(ret)))

    def car(self, fun):
        return fun[0]

    def cdr(self, fun):
        return fun[1]

    def __str__(self):
        return self.problemName


if __name__ == "__main__":
    P = Problem()
    P.solve()