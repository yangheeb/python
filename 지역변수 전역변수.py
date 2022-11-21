#2215641 백민정

def add(*p):  #매개변수에 가변인자로 정의,, tuple형태
    hap=0
    for n in p:
        hap+=n
    return hap

#print(add(3,5,9,10))
#print(add(1,10,11,15,19,20,10))

##지역변수와 전역변수
x=100  #전역변수(함수 밖에서 선언)
def myfunc():
    global y #전역변수로 선언하는 것
    y=77
    x=25  #함수 내 선언 및 초기화 된 지역변수x 
    print(x)
myfunc()
print(x)
print(y)


#소수를 구하는 함수
def prime(num):
    isPrime=True  #true면 소수
    for i in range(2,num):
        if num%i==0:
            isPrime=False
            break
    return isPrime

for i in range(2,51):
    print(i,"소수"if prime(i)else "합성수")

i=2
while i<=100:
    if prime(i):
        print(i,end=" ")
    i+=1

#200~500까지 소수를 구하는 프로그램을 for문으로 작
print()
for i in range(200,501):
    if prime(i):
        print(i,end=" ")
