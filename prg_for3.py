#2215641 백민정 turtle을 이용한 도형 그리기
import turtle as r  
r.shape("turtle")
r.color("orange")
#n=int(input("몇각형을 원하시나요=>"))  #n각형 변수로 받아 입력
n=int(r.textinput("2215641 백민정","몇각형?"))
for i in range(n):   #n번 반복
    r.fd(100)
    r.lt(360/n)

r.done()
