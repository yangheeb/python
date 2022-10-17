#2215641 백민정 중첩if문
score=int(input("점수입력=>"))
if score>=90:
    print(score,"A")
else:
    if score>=80:
        print(score,"B")
    else:
        print(score,"C")
    


print("##########")
if score>=90:
    print(score,"A")
elif score>=80:
    print(score,"B")
else:
    print(score,"C")
