#2215641 백민정
n=int(input("정수를 입력하시오:"))
fac=1
for i in range(1,n+1):
    fac*=i
    print(i,"!=",fac)   #들여쓰기 하는 것과 아닌 것의 차이를 알아두기
