cap1 = ['F','F','B','B','B','F','B','B','B','F','F','B','F']
cap2 = ['F','F','B','B','B','F','B','B','B','F','F','F','F']
def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                print('peple in positions', i, end='')
            else:
                print(' through', i, 'flip your caps!')

def pleaseConform(caps):
    start = forward = backward = 0
    intervals = []
    caps = caps + ['END']
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
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
            print('peple in positions', t[0], 'through', t[1], 'flip your caps!')

if __name__ == '__main__':
    pleaseConform(cap1)
    #pleaseConform(cap2)
    print("")
    pleaseConformOnepass(cap1)
    #pleaseConformOnepass(cap2)