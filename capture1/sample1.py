cap1 = ['F','F','B','B','B','F','B','B','B','F','F','B','F']
cap2 = ['F','F','B','B','B','F','B','B','B','F','F','F','F']
cap3 = ['F','F','B','H','B','F','B','B','B','F','H','F','F']
def pleaseConformOnepass(caps):
    caps = caps + ['END']
    start = 0
    for i in range(1, len(caps)):
        if caps[i] != caps[start]:
            if caps[start] != caps[0]:
                if start != i-1:
                    print('peple in positions', start, 'through', i-1, 'flip your caps!')
                else:
                    print('person at position', start, 'flip your cap!')
            start = i

def pleaseConform(caps):
    start = forward = backward = 0
    intervals = []
    caps = caps + ['END']
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            if caps[start] != 'H':
                intervals.append((start, i-1, caps[start]))
                if caps[start] == 'F':
                    forward += 1
                else:
                    backward += 1
            start = i
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[0] != t[1]:
                print('peple in positions', t[0], 'through', t[1], 'flip your caps!')
            else:
                print('person at position', t[0], 'flip your cap!')

if __name__ == '__main__':
    pleaseConform(cap1)
    #pleaseConform(cap2)
    print("")
    pleaseConformOnepass(cap1)
    #pleaseConformOnepass(cap2)
    print("")
    pleaseConformOnepass([])
    print("")
    pleaseConform(cap3)