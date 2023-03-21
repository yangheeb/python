#2215641 백민정
#list와 tuple 자료구조에 대한 프로그램
a=[20,30,45,25,50,75,100] #리스트 데이터 구조
b=(10,15,23,8,10,18) #튜플 데이터 구조
print(a[2])
print(b[2])

#반복문을 이용한 데이터 원소를 출력하는 프로그램
#1. 인덱스를 이용한 출력 프로그램
for i in range(len(a)):
    print(a[i])
#2. for each로 출력하는 프로그램
for val in b:
    print(val,end=" ")

print("############")
data=[20,1,12,9,18]
for i in data:
    print("%2d"%i,"#"*i)


data1=sorted(data)
for i in data1:
    print("%2d"i,"#"*i)

