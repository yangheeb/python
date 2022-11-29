#2215641 백민정 1~100까지 소수를 list로 생성
def prime(num):
    isPrime=True
    for i in range(2,num):
        if num%i==0:
            isPrime=False
            break
    return isPrime  #return 되는건 true 아님 false가 됨

alist=[]  #alist는 리스트 데이터구조로 선언

for i in range(2,100):
    if prime(i):
        alist.append(i)
print(alist)
print(len(alist))
print(sum(alist))

avg=sum(alist)/len(alist) #평균
hap=0
for i in range(len(alist)):
    hap+=(alist[i]-avg)**2
print("평균=%7.3f, 분산=%9.3f" %(avg, hap/len(alist)))
