#2215641 백민정 연산자 프로그램
#n1=eval(input("수1=>"))
#n2=eval(input("수2=>"))
n1,n2=10,3
print("나누기",n1/n2)
print("몫",n1//n2)
print("나머지",n1%n2)
print("제곱",n1**n2)

x,y= 10,30
x+=y #x=x+y와 같다
print("x=%d,y=%d"%(x,y))
x*=y #x=x*y와 같다
print("x=%d,y=%d"%(x,y))
