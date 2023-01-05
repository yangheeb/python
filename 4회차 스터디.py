#p.244 exercise


#01
def max(a,b):
    if a>b:
        result=a
    else:
        result=b
    return result


#02 (정답: 10)
def main():
    print(mistery(10,20))
    
def mistery(a,b):
    result=a
    if b<result:
        result=b
    return result
main()


#03
def sub(a,b,c,d):
    pass

<answer>
def sub(1,2,3,d=4)


#04
def mistery(a,b,min):
    min=a
    if b<min:
        min=b

min=0
mistery(20,10,min)
print(min)

#출력값
0


#05
x=10
def dec():
    global x
    x=x-1

print(x)
dec()
print(x)

#출력값
10
9
    

#06
x=int(input("정수를 입력하시오:"))
if x<0:
    y=10
print(y)

#if문에 해당하지 않을 경우에는(x<0가 아닐때는) y에 해당하는 값이 없다
#if문 밖에서 y에 관한 변수 설정을 해줘야한다

#07
def sub(a=2,b=3):
    print(a,b)

sub()  >> 2 3
sub(a=10) >> 10 3
sub(5,6) >> 5 6
sub(b=10) >> 2 10

#08 (정답:30 -10)
def sub(a,b):
    return a+b,a-b

x,y=sub(10,20)
print(x,y)

#09
global=0
def sub():
    local=1
    print(global)
    print(local)
    
sub()
print(global)
print(local)

#lobal은 예약어이기 때문에 변수로 사용할 수 없다
#local은 지역변수로 사용되기 때문에 오류 발생



#p.246 programming

#01

def get_peri(radius=5.0):
    area=2*radius*3.14
    return area
print(get_peri())
print(get_peri(4.0))


#02

x = int(input("첫 번째 정수를 입력하시오:"))
y = int(input("두 번째 정수를 입력하시오:"))

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("(", x, "+", y, ")=", plus(x, y))
print("(", x, "-", y, ")=", minus(x, y))
print("(", x, "*", y, ")=", multiply(x, y))
print("(", x, "/", y, ")=", divide(x, y))

#03

def calc(a,b):
    return a+b,a-b,a*b,a/b
x=int(input("첫 번째 정수를 입력하시오:"))
y=int(input("두 번째 정수를 입력하시오:"))
a,b,c,d=calc(x,y)
print(a,",",b,",",c,",",d,"이 반환되었습니다.")

#맨 마지막 print값 출력할때 "," 이거 필요 없는듯??


#04

def getGrade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
x=int(input("점수를 입력하시오:"))
print("성적은",getGrade(x),"입니다")

#주희 답이랑 비교


#06
def plus(a,b):
    return a+b
x=int(input("첫 번째 정수를 입력하시오:"))
y=int(input("두 번째 정수를 입력하시오:"))
a=plus(x,y)
print("정수",x,"+",y,"의 합은?",a)

#주희 답이랑 비교
