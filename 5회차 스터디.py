#p.247 programming

#09
def gcd(a,b):
    i=0 
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i
        
a=int(input("첫 번째 정수:"))
b=int(input("두 번째 정수:"))
gcd(a,b)
print(gcd(a,b))


#global을 이용해서 전역변수 선언하기-> print(i)출력 가능함
def gcd(a,b):
    global i
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i
        
a=int(input("첫 번째 정수:"))
b=int(input("두 번째 정수:"))
gcd(a,b)
print(i)


#10
def testPrime(n):
    isPrime=True
    for i in range(2,n):
        if n%i==0:
            isPrime=False
            break
    return isPrime

for j in range(2,101):
    if testPrime(j):
        print(j,end=" ")
        

#12
def getSorted(x,y):
    x=int(input("첫 번째 정수:"))
    y=int(input("두 번째 정수:"))

    if x>y:
        print((y,x))
    elif x<y:
        print((x,y))

getSorted(30,20)
        
#16
def darw_line():
    t.forward(100)
    t.backward(100)

import turtle as t
t.shape("turtle")

for i in range(12):
    darw_line()
    t.left(30)


#Workbook 01

#01-1 (정답 : 1 2 4 5)
i=0
while i<6:
    i+=1
    if i%3==0:
        continue
    print(i, end=" ")


#01-2 (정답 : 합 = 55)
i=1
hap=0
while i <=10:
    hap+=i
    i+=1
print("합 =", hap) 


#02-1
#for문
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()

#while문
i=1 
while i<6:
    j=1 
    while j<i+1:
        print(j, end="")
        j+=1
    i+=1 
    print()


#02-2
#for문
    for i in range(10):
    for j in range(i, 10):
        print("*", end='')
    print()

#while문
i=0
while i<10:
    j=i
    while j<10:
        print("*", end='')
        j+=1
    i+=1
    print()


#02-3
n=int(input("숫자를 입력하세요:"))
i=1
hap=0
while i<=n :
    hap+=i**2
    i+=1
print("결과는 %d 입니다." %(hap))


#03-1
import turtle as t
t.circle(100) 
t.left(60) 
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.done()


#03-2
#while문으로 변경
import turtle as t
i=0
while i<6:
    t.circle(100)
    t.left(60)
    i+=1


#04-1
#for문
for i in range(2,101):
    for j in range(2, i + 1):
        if i==j: 
            print(i, end=" ")
        elif i%j==0:

#while문
i=2
while i<101: 
    j=2
    while j<i+1:
        if j==i: 
            print(i, end=" ") 
        elif i%j==0: 
            break
        j+=1
    i+=1


#04-2
#for문
for i in range(2,31):
    for j in range(2, i+1):
        if i==j:
            print("%2d : 소수" %i)
        elif i%j==0:
            print("%2d : 합성수" %i)
            break

#while문
i=2
while i<31:
    j=2
    while j<i+1:
        if j==i:
            print("%2d : 소수" %i)
        elif i%j==0:
            print("%2d : 합성수" %i)
            break
        j+=1
    i+=1
            break
t.done()



#Workbook 02

#01
def sum(v1, v2):
    result = v1+v2
    return result
print(sum(v1, v2))

#02
def func(v1, v2=0, v3=0):
    return v1+v2+v3
#print(func(1)) -> 1
#print(func(1, 2)) -> 3
#print(func()) ->오류발생


#03
a=0
def func1():
    print(a)
def func2():
    a=111
    print(a)
func1() (정답 : 0)
func2() 정답 : 111)


#04 (정답 : 30-10)
def sub(a, b):
    return a+b, a-b
x, y = sub(10, 20)
print(x, y)


#05 (정답 : 9)
x=10
def dec():
    global x
    x=x-1
dec()
print(x)



#06
def square(n):
    return n**2
print('3의 제곱은:', square(3))
print('4의 제곱은:', square(4))


#07
def draw_square(size) :
    for i in range(4) :
        t.fd(size)
        t.left(90)
        size += 5

import turtle as t
t.shape("turtle")
t.color("blue")

for i in range(8) :
    draw_square(i*20+5)
t.done()


#08 BMI
def cal_bmi(weight,height):
    height*=0.01
    bmi=(weight/(height**2))
    if bmi<18.5:
        print("저체중입니다.")
    elif 18.5<=bmi<25.0:
        print("표준입니다.")
    elif 25.0<=bmi<30:
        print("과체중입니다.")
    else :
        print("비만입니다.")

weight=eval(input("몸무게(kg) : "))
height=eval(input("키(cm) : "))
cal_bmi(weight, height)
    
                  
