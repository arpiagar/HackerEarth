
intervals = [(3,10),(4,20),(1,2),(6,8),(7,30),(35,40)]

sorted_interval = sorted(intervals, key = lambda intervals : intervals[0])

if len(sorted_interval):
    #start_val = sorted_interval[0][0]
    #max_end_val = sorted_interval[0][1]
    i = 0
    out = []
    while(i < len(sorted_interval)):
        start_val =  sorted_interval[i][0]
        max_end_val = sorted_interval[i][1]
        i += 1
        while( i < len(sorted_interval) and sorted_interval[i][0] < max_end_val):
            max_end_val = max(max_end_val, sorted_interval[i][1])
            i += 1
        out.append((start_val, max_end_val))
print out






