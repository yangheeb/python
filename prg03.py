#2215641 백민정 원의 면적과 둘레
r=eval(input("반지름=>")) #숫자형 데이터 변환 함수 : int(),float(),eval()
PI=3.141592 #3.14를 PI라는 상수로 지정
area=r*r*PI #면적
print("원의 면적:",area)
cir=2*r*PI #둘레
print("원의 둘레:%7.2f"%cir) #서식문자가 있는 프린트
v=(4/3)*PI*r*r #부피
print("구의 부피:%7.2f"%v) #서식문자가 있는 프린트
