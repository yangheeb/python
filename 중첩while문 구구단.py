#2215641 백민정 중첩 while문 구구단
dan=2
while dan<=9:
    i=1
    while i<=9:
        print("%2d*%2d=%2d"%(dan,i,dan*i))
        i+=1
    dan+=1
    print()
