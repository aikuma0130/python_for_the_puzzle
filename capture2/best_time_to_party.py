sched = [(6,8), (6,12), (6,7), (7,8), (7,10), (8,9), (8,10), (9,12), (9,10), (10,11), (10,12), (11,12)]
def bestTimeToParty(schedule):
    start = schedule[0][0]
    end = schedule[0][1]
    for c in schedule:
        start = min(c[0], start)
        end = max(c[1], end)
    count = celebrityDensity(schedule, start, end)
    maxcount = max(count[start:end + 1])
    time = count.index(maxcount)
    print('Best time to attend the party is at', time, 'o\'clock', ':', maxcount, 'celebrities will be attending!')

def celebrityDensity(schedule, start, end):
    count = [0] * (end + 1)
    for i in range(start, end + 1):
        for c in schedule:
            if c[0] <= i and c[1] > i:
                count[i] += 1
    return count

bestTimeToParty(sched)

sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0), (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
def bestTimeToPartySmart(schedule):
    times = []
    for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))
    sortList(times)
    maxcount, time = chooseTime(times)
    print('Best time to attend the party is at', time, 'o\'clock', ':', maxcount, 'celebrities will be attending!')

def sortList(tlist):
    for index in range(0, len(tlist)-1):
        index_min = index
        for i in range(index, len(tlist)):
            if tlist[index_min] > tlist[i]:
                index_min = i
        tlist[index], tlist[index_min] = tlist[index_min], tlist[index]

def chooseTime(times):
    count = maxcount = time = 0
    for t in times:
        if t[1] == 'start':
            count += 1
        elif t[1] == 'end':
            count -= 1
        if count > maxcount:
            maxcount = count
            time = t[0]
    return maxcount, time

bestTimeToPartySmart(sched2)