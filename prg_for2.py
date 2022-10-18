#2215641 백민정 1~100합을 계산하는 프로그램
#for i in range(1,5,1):
#    print(2*i,end="  ")
hap=0
for i in range(1,101,1):  #1은 생략 가능
    hap+=i
print("합=",hap)

hap=0  #hap은 0이라고 다시 입력해주기  
for i in range(2,101,2):
    hap+=i
print("짝수의 합=",hap)

