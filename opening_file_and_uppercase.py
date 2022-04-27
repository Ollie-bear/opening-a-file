fh = open('mbox-short.txt')

#rstrip() seperates spaces when opening a file

for cutemahim in fh :
    mahim = cutemahim.rstrip()
    print(mahim.upper())
