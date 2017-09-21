infile = open('PE5_2.txt','r+')
for line in infile:
    line_list = line.split(',')
    line_list.reverse()
    print('{} heeft kaartnummer: {}'.format(line_list[0].replace('\n',''),line_list[1]))
infile.close()

