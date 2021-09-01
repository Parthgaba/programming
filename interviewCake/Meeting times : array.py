# NOTE - we can do this by sorting which will take O(nlogn) time complexity.

meetings = []
for _ in range(int(input())):
    start, end = map(int, input().split())
    meetings.append([start, end])
time_bound = [False] * 48
for i in range(len(meetings)):
    for j in range(meetings[i][0], meetings[i][1] + 1):
        time_bound[j] = True
final_meetings = []
tempTuple = tuple()
for x in range(len(time_bound)):
    if x == 0 and time_bound[x] == True:
        tempTuple += (x + 1,)
        continue
    if x == 0 and time_bound[x] == False:
        continue
    if x == len(time_bound) - 1 and time_bound[x] == True:
        tempTuple += (x,)
        final_meetings.append(tempTuple)
        tempTuple = tuple()
        break
    elif x == len(time_bound) - 1:
        break
    if time_bound[x - 1] == False and time_bound[x] == True:
        tempTuple += (x,)
    if time_bound[x + 1] == False and time_bound[x] == True:
        tempTuple += (x,)
        final_meetings.append(tempTuple)
        tempTuple = tuple()
print(final_meetings)
