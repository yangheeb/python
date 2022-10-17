#2215641 백민정 컵사이즈별 가격을 설정
size=input("사이즈를 입력하시오(S,L,X)=>")
price =0
if size.upper()=="S": #"S"or"s"로 사용해서넣어도 됨
    price=2000
else:
    if size.upper()=="L":
        price=3000
    else:
        if size.upper()=="X":
            price =4000
        else:
            print("조건에 맞는 컵사이즈가 없습니다")
print(size,price)



