#2215641 백민정
#if~elif
su1=int(input("점수를 입력=>"))
su2=int(input("점수를 입력=>"))
avg=(su1+su2)/2
if avg>=90:
    print("최우수")
elif avg>=80:
    print("우수")
elif avg>=70:
    print("노력")
else:
    print("과락")