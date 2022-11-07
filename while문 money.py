#2215641 백민정 p.173 예제 변형
TARGET=2000  #상수정의
money=1000
rate=0.07
year=0
while money<TARGET:
    money+=money*rate
    year+=1
print(year,"년")
