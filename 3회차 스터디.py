#p.196 exercise

#02
for i in range(0,10,2):
    print(i)
    
#출력 값
0
2
4
6
8


#03 for문
for i in range(-2,-6,-1):
    print(i,end=" ")

#출력 값
-2 -3 -4 -5


#03번 while문
i=-2
while i>-6:
    print(i,end=" ")
    i+=-1



#04 (while문으로 전환)
sum=0
i=0
while i<100:
    sum+=1
    i+=1



#05
for x in range(10):
    if x>5:
        continue
    if x>8:
        break
    print("Hellow World")

#출력 횟수: 6번 --> x=5일때까지 출력
#x=6,7,8일때부터는 밑으로 못 내려가고 그저 반복만
#continue는 다음 반복을 즉시 시작하게 하는 키워드
#x=9일때는 반복문이 아예 깨짐
    
Hellow World x=0
Hellow World x=1
Hellow World x=2
Hellow World x=3
Hellow World x=4
Hellow World x=5


#06 (잘못된 점: i의 증감식을 넣어주지 않아 i=0인 상태 계속 반복됨)
i=0
while i<10:
    print(i)

#오류를 수정하기 위해서는 print(i) 밑에 줄에 i+=1을 넣어야 한다


#07 (소스 코드 반복 횟수 : 11번)
i=0
while i<=10:
    print("Hi!")
    i+=1


#08
x=0
while(x<100):
    x+=2       #x가 100이 되면 조건문이 거짓이 되기 때문에 무한루프 탈
print(x)

#출력값 100

#10
numbers=[10,20]
items=["TV","Phone"]

for x in numbers:
    for y in items:
        print(x,y)

#출력
10 TV
10 Phone
20 TV
20 Phone

#p.198 programming

#01
for i in range(2,51):
    if i%2==0:
        print(i,end=" ")

#01번 while문
i=2
while i<=50:
    if i%2==0:
        print(i,end=" ")
    i+=1

#02
myList=[11,22,23,99,81,93,35]
hap=0
for i in myList:
    hap+=i
print("정수들의 합은",hap)

#03 for문
hap=0
for i in range(0,101):
    if i%3==0:
        hap+=i
print("1부터 100 사이의 모든 3의 배수의 합은 %d"%hap)

#03 while문
hap=0
i=0
while i<101:
    if i%3==0:
        hap+=i
        i+=1

print("1부터 100 사이의 모든 3의 배수의 합은 %d"%hap)

#04
x=int(input("정수를 입력하시오:"))
print("약수:",end=" ")
for i in range(1,x+1):
    if x%i==0:
        print(i,end=" ")

#05 for문
x=int(input("정수를 입력하시오:"))
for i in range(1,

#05 while문
x=int(input("정수를 입력하시오:"))
i=1
while x!=i:
    print(i,end=" ")
    i+=1
    print()

#10 for문
x=int(input("n의 값을 입력하시오:"))
hap=0
for i in range(1,x+1):
    hap+=i**2
print("계산값은 %d 입니다."%hap)

#10 while문
x=int(input("n의 값을 입력하시오:"))
i=1
while i<n+1:
    m
    i+=1
