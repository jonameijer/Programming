def numLines(filename):
    infile = open(filename,'r')
    lineList = infile.readlines()
    infile.close()
    print('Deze file telt',len(lineList),'regels')

def biggestNum(filename):
    infile = open(filename,'r')
    content = infile.readlines()
    numlist = []
    for line in content:
        numlist.append(int(line.split(',')[0]))
    maximum = max(numlist)
    linemaximum = numlist.index(max(numlist))+1
    print('Het grootste kaartnummer is:',maximum,'en dat staat op regel',linemaximum)


input = input('Name of text file: ')
numLines(input)
biggestNum(input)