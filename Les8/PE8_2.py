import random

def monopolyworp():
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    worp1 = []
    worp1.append(a)
    worp1.append(b)
    if a != b:
        print(a,'+',b,'=',sum(worp1))
    if a == b:
        print(a,'+',b,'=',sum(worp1),'(dubbel)')
        c = random.randrange(1, 7)
        d = random.randrange(1, 7)
        worp2 = []
        worp2.append(c)
        worp2.append(d)
        if c != d:
            print(c,'+',d,'=',sum(worp2))
        if c == d:
            print(c,'+',d,'=',sum(worp2),'(dubbel)')
            e = random.randrange(1, 7)
            f = random.randrange(1, 7)
            worp3 = []
            worp3.append(e)
            worp3.append(f)
            if e != f:
                print(e,'+',f,'=',sum(worp3))
            if e == f:
                print(e,'+',f,'=','(direct naar gevangenis')

monopolyworp()