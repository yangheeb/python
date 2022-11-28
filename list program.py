#2215641 백민정 list program

a=[30,40,15,20,80,25]  #리스트
b=(5,7,10,7,5,10)  #튜플


#리스트원소를 index로 접근함,, 인덱싱!!
for i in range(len(a)):
    print(a[i],end=" ")
print()

#리스트원소를 for~each로 접근
for val in a:
    print(val,end=" ")
print()

#튜플원소를 index로 접근
for i in range(len(b)):
    print(b[i],end=" ")
print()

#합과 평균 구하
hap=0
for i in range(len(a)):
    hap+=a[i]
print("합=",hap,"평균=",hap/len(a))
