#2215641 백민정 함수와 모듈 프로그램

#함수 정의하기 
def get_area(r):  #원의 면적과 둘레를 구하는 함수
    area=3.14159*r**2
    c=3.14159*2*r
    return area,c #return은 면적과 둘레 2개를 한다

def fact(n=1): #매개변수 디폴트 값 1로 지정
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def hap(var):
    s=0
    for val in var:
        s+=val
    return s 

#함수 호출하기
#print("합=",hap([50,15,22,30,25]))
#print(fact(15))
#a,b=get_area(9)
#print("면적=",a,"둘레=",b)



    
