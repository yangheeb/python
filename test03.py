#2215641 백민정

hap1=0
hap2=0
for i in range(1,101):
    if i%2==0:
        hap1+=i
    else:
        hap2+=i
print("짝수의 합=",hap1)
print("홀수의 합=",hap2)

num=int(input("정수입력=>"))
ehap,ohap=0,0
for n in range(1,num+1):
    if n%2==0:
        ehap+=i
    else:
        ohap+=i
print("1~%d까지 짝수합=%d 홀수합=%d"%(num,ehap,ohap))
