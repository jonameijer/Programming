

def ticker(name):
    infiler = open('PE7_4.txt', 'r')
    lines = infiler.readlines()
    tickers = {}
    list = []
    for x in lines:
        if '\n' in x:
            list.append(x.replace('\n',''))
        else: list.append(x)
    split = []
    for x in list:
        split.append(x.split(':'))
    for x in split:
        tickers[x[0]]=(x[1])
    print('Company name:',tickers[name])

input = input('Enter Company name: ')
ticker(input)