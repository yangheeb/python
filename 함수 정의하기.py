#2215641 백민정 함수프로그램 1
#함수 정의하기
def get_area(r):
    area=3.14159*r**2
    return area


#함수 사용(호출)하기
result=get_area(7) #호출할 때 7이라는 값을 r에 넣어준다
print(result)
print(get_area(15))
