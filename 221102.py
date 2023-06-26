## 기말고사 코딩테스트 안 할 예정
## 시험지 내에 코딩 문제는 있을 것
## 23년도 1학기 수강신청 > 2월 둘째주. 2/6(월, 4학년)~9(목)
## 23년도 1학기 위시리스트 1/26~27
## 9일, 24일에 인원 많이 열릴 예정.


### 중간고사 풀이
##### 1번 문제 #####
for i in range(1,11):
    if i % 2 == 0:
        print("%d는 짝수입니다."%i)
    else:
        print("%d는 홀수입니다."%i)


#### 2번 문제 #####
i = 1
while i<=30:
    if i%2 == 0 or i%3 == 0:
        i += 1
        continue ## 이 부분 틀림
    else:
        print(i)
        i += 1


#### 3번 문제 #####
def rem(a,b):
    result = a%b
    print(result) ## 함수 내에서 출력했으니 리턴은 안 하는 것.

rem(9,3) #0
rem(7,5) #2


#### 4번 문제 #####
word = input("영단어를 입력해주세요:")
result = word[0] + str(len(word)) + word[-1]
print(result)


#### 5번 문제 ##### (txt파일은 제출할 필요 없음)
f = open('name.txt','w')
name = ['Alex','Emma','Smith','Jane','Ava','Charlotte','Evelyn']

for i in name:
    if len(i) == 4:
        f.write(i+'\n') ## 출력 내용이 약간 다름

f.close()


#### 6번 문제 #####
score = {'국어': 90, '영어':95,'수학':77, '미술':68, '과학': 82}
sum = 0
average = 0.0
for i in score.keys():
    sum += score[i]
    print("%s 과목의 점수는 %d 입니다."%(i, score[i]))
average = sum/len(score)
print("전체 평균은 %d 입니다."%average)


#### 7번 문제 #####
def check_number(string):
    result = []
    for i in string:
        if i=='3' or i=='6' or i=='9': ## i in ['3','6','9']
            result.append('x')
        else:
            result.append(i)
    print(result)

check_number("010-9012-3569")


#### 8번 문제 #####
answer = input("학번을 입력해 주세요:")

# coding here ##
id = answer[2:4] ## 문자열 처리
print("당신은 %s학번 입니다."%id)


#### 9번 문제 #####
visit = ['영국','일본','미국','프랑스','폴란드','칠레','캐나다','이탈리아']
wish = ['브라질', '독일', '캐나다', '호주', '영국']
result = []

# coding here ##
for i in wish:
    if i in visit:
        result.append(i)
print(result)


#### 10번 문제 #####
# coding here ##
f = open('20211648.txt','w')
for i in range(6,0,-1): ## 범위를 다르게 적음
    f.write((str(i)+' ')*i + '\n')

f.close()


### 과제 풀이
# ## 1. 교과목 정보 출력 ##
# number = input("학수번호를 입력하세요 :")
# #### coding here ####
# if number == '데사B0002': ## 반복 간소화를 안 할 경우
#     print('데이터마이닝이해와실습, 숭의관1호')
# elif number == '문공A0015':
#     print('R프로그래밍, 인문관2호')
# elif number == '문공A0016':
#     print('기초선형대수학, 대학원3호')
# else:
#     print('없습니다.')


# ## 2. 숫자 맞추기 게임 ##
# answer = 25
# #### coding here ####
# num = 0
# while answer != num: ## 1로 무한 루프가 아니라 조건을 적을 수도 있다.
#     num = int(input('숫자를 입력하세요 : '))
#     if num > answer:
#         print('DOWN !')
#     elif num < answer:
#         print('UP !')
#     else:
#         print('정답 !')


# ## 3. 물건 값 계산하기 ##
# sum = 0

# for i in str(3**79): ## list 안 붙여도 된다.
#     sum += int(i)

# print(sum)


# ## 4. while문 이용 문제 ##
#### coding here ####
# i = 7 ## 처음부터 7로 변수 선언
# while i > 0:
#     print('*' * i)
#     i -= 2

# i = 0 ## 0으로 변수 선언
# while i < 8:
#     print('*' * (7-i))
#     i += 2


## 5. 상수도 요금 문제 ##
#### coding here ####
quantity = int(input('물의 사용량을 입력해 주세요: '))
price = 0
if quantity >= 31:
    price = 20*430 + 10*570 + (quantity-30)*840
elif quantity >= 21:
    price = 20*430 + (quantity-20)*570
else:
    price = quantity*430
print(price)


def price(quantity): ## 함수 활용 시
    price = 0
    if quantity >= 31:
        price = 20*430 + 10*570 + (quantity-30)*840
    elif quantity >= 21:
        price = 20*430 + (quantity-20)*570
    else:
        price = quantity*430
    return price
print(price(35))