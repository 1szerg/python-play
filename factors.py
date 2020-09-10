import time
def fullRange(a):
    b=[]
    max = int(a+1)
    for i in range(1, max):
        if a%i==0:
            b.append(i)
    return b
def halfRange(a):
    b=[]
    b.append(1)
    max = int(a/2)+1
    for i in range(2, max):
        if a%i==0:
            b.append(i)
    b.append(a)
    return b
def sqrRange(a):
    b=[]
    max = int(a**0.5)+1
    for i in range(1, max):
        if a%i==0:
            b.append(i)
            b.append(int(a/i))
    return sorted(b)
def testing(a, func, mess):
    print(mess)
    t = time.perf_counter()
    b = func(a)
    for i in b:
        print(str(i))
    print("Time - "+str(time.perf_counter()-t)+" sec")
    
while 1==1:
    aInp = input("Tell me what number you need factors for > ")
    if aInp.isdecimal():
        a = int(aInp)
        #testing(a, fullRange, "fullRange")
        #testing(a, halfRange, "halfRange")
        testing(a, sqrRange, "sqrRange")
    else:
        print("Let's try with numbers")
