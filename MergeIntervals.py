# There are a lot of problems that in some way
# need to merge intervals of array based on some criteria

# here is a classical question

#merge intervals

intervals = [[1,3],[2,6],[8,10],[15,18]]

# step by step reproduction

#sort by first item in case od 2*2 matrix

intervals.sort()
merged = [intervals[0]]

for i in range(len(intervals)):
    first =  intervals[i][0]
    second = intervals[i][1]

    if merged[-1][1] >= first:
        merged[-1][1] = max(merged[-1][1], second)
    else:
        merged.append([first, second])
print(merged)



# there are plenty of other variations but this is like the base of everything


#merge intervals
# first sort
intervals.sort() # it always sort based on first element

# second merge the intervals

merged = [intervals[0]]

for i in range(len(intervals)):
    first = intervals[i][0]
    second = intervals[i][1]

    if merged[-1][1] >= first:
        merged[-1][1] = max(merged[-1][1], second)
    else:
        merged.append([first,second])
print(merged)