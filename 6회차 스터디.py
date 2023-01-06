#p.213 lab 문제

#원의 면적을 계산하는 함수 정의
def area(r):
    return r**2*3.14


#함수 호출하고 값 출력
print("20cm 피자 2개의 면적:",area(20)+area(20))
print("30cm 피자 1개의 면적:",area(30))

#p.221 lab 문제

#display 함수 정의
def display(msg,count=1):
    for i in range(5):
        print("환영합니다.")
        
msg=int("환영합니다.") 
display(msg,5)

#p.222

#함수 정의
def f(x):
    return(x**2-x-1)

def bisection_method(a, b, error) :
    if f(a)*f(b) > 0:
        print("구간에서 근을 찾을 수 없습니다.")
    else:
        while (b-a)/2.0 > error:
            midpoint = (a+b)/2.0
            if f(midpoint)==0:
                return(midpoint)
            elif f(a)*f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return midpoint

answer = bisection_method(1, 2, 0.0001)
print("x**2-x-1의 근:", answer)


#p.223 lab 문제

def weeklypay(rate,hour):
    if hour<=30:
        return rate*hour
    else:
        return rate*1.5*(hour-30)+rate*30

rate=int(input("시급을 입력하시오:"))
hour=int(input("근무 시간을 입력하시오:"))

print("주급은",weeklypay(rate,hour))

#p.227 lab 문제

def information(name,age):
    print("이름은",name,"이고 나이는",age,"살입니다")
   
name=input("이름:")
age=int(input("나이:"))
information(name,age)
import turtle as t
t.shape("turtle")
t.speed(0)

def f(x):
    return x**2+1

t.goto(200, 0)
t.goto(0, 0)
t.goto(200, 0)
t.goto(0, 0)

for x in range(150):
    t.goto((x, int(0.01*f(x)))

t.bye()


#p.241 lab 문제
