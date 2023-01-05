#p.174 1~n까지 합계
n=int(input("숫자를 입력하시오:"))
hap=0
a=1
while a<n+1:
    hap+=a
    a+=1
print(hap)

#p.176 구구단 출력 while문
dan=int(input("원하는 단은:"))
i=1
while i<10:
    print("%2d*%2d=%2d"%(dan,i,dan*i))
    i+=1
    
#p.176 중간점검 1번
#for문과 while문 조건식이 같다면 어떻게 작동하는지?? [반복 구조 차이]
    
#for문은 반복의 횟수를 미리 아는 경우에 사용한다.
#힝목들을 모아 놓은 시퀀스라는 객체가 있고 여기에서 항목을 하나씩 가져와서 반복함
#시퀀스에 더 이상 항목이 없다면 반복 종료
    
#while문은 어떤 조건이 만족되는 동안 계속 반복
#조건이 거짓이면 반복 종료 (조건 반복=while문)

#p.177 도전문제
#구구단 출력 while문
#구구단 출력 for문

#p.184 주사위 2개의 합이 n인 경우
for a in range(1,7):
    for b in range(1,7):
        if a+b==6:
            print("첫 번째 주사위=%d, 두 번째 주사위=%d"%(a,b))
            
#p.185 도전문제
people=["Kim","Park","Lee","Choi"]
restaurants = [ "Korean" , "American" ,"French" , "Chinese" ]
locations= ["서울","부산","대전"]
for a in people:
    for b in restaurants:
        for c in locations:
            print("%s이 %s에 있는 %s 식당을 방문"%(a,c,b))

#p.189 중간점검 1번
#break문이 반복문에서 실행되면 반복문을 빠져 나온다.
            
#p.189 중간점검 2번
for i in range(1,10,1):
    if i%3==0:
        break
    print(i)

#출력 값
1
2
