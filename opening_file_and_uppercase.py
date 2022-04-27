fh = open('mbox-short.txt')

for cutemahim in fh :
    mahim = cutemahim.rstrip()
    print(mahim.upper())