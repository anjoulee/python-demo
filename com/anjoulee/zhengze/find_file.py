def find_start_anjoulee(fname):
    f = open(fname)

    for line in f:
        if line.startswith('Anjoulee'):
            print line


find_start_anjoulee('anjoulee.txt')


def find_in_anjoulee(fname):
    f = open(fname)

    for line in f:
        if line.startswith('Anjoulee') and line.endswith('Anjoulee'):
            print line


find_in_anjoulee('anjoulee.txt')
