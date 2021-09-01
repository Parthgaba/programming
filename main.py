import os
import sys
import glob
from pathlib import Path

class main:
    def __init__(self):
        self.id = 0
        self.id_list = []
        self.curr_problem_name = ""

    def getProblems(self):
        pass

    def getLatest(self):
        paths = sorted(glob.glob("*.py"), key=os.path.getmtime,reverse=True)
        latestPath = paths[len(paths)-1]
        latestfile = str(latestPath).split('.')[0]
        self.curr_problem_name = latestfile
        print(f'Executing Latest File {latestfile} ->')

    def setFile(self, file):
        self.curr_problem_name = file

    def invokeProblem(self):
        try:
            P = eval("__import__('" +self.curr_problem_name+"').Problem()")
            P.solve()
        except Exception as e:
            print(f'Error: {e}')

    def throwLatest(self):
        pass

    def throwFiles(self):
        pass

if __name__=="__main__":
    n = len(sys.argv)
    M = main()
    if n==1:
        file = M.throwLatest()
        print(file)
    elif n==2:
        if sys.argv[1] == "ls":
            filelist = M.throwFiles()
            print(filelist)
        elif sys.argv[1] == "exec":
            M.getLatest()
            M.invokeProblem()
        else:
            print(f'Error: Invalid command {sys.argv[1]}')
    else:
        if sys.argv[1] == "exec":
            M.setFile(sys.argv[2])
            M.invokeProblem()
        else:
            print(f'Error: Invalid command {sys.argv[0]}')
