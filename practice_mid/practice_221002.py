### 2주차 복습

### 조건문

### 예시 1)
# answer = input('비밀번호를 입력해 주세요 : ')
# answer = answer.lower()
# if answer == 'data':
#     print('correct')
# else:
#     print('fail!')


### 예시 2)
# num = int(input('숫자를 입력해 주세요 : '))
# if num<0:
#     print('0보다 큰 숫자를 입력해 주세요.')
# else:
#     if num%2==0:
#         print('입력하신 숫자는 짝수입니다.')
#     else:
#         print('입력하신 숫자는 홀수입니다.')


### 예시 3) tip - 큰 수부터 내려가기.
# score = int(input())
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')


### 예시 4)
# tel = input('고객님께서 사용 중이신 통신사를 입력해 주세요 : ')
# tel = tel.upper()
# if tel == 'SKT':
#     print('고객님께서 사용 중이신 통신사는 SK텔레콤 입니다.')
# elif tel == 'KT':
#     print('고객님께서 사용 중이신 통신사는 KT 입니다.')
# elif tel == 'LG':
#     print('고객님께서 사용 중이신 통신사는 LG 입니다.')
# else:
#     print('통신사 오류입니다. 다시 진행해 주세요.')


### 예시 5)
# age = int(input('고객님의 나이를 입력해 주세요 : '))
# if age >= 60:
#     print('고객님의 연령대는 60대 이상 입니다.')
# elif age >= 50:
#     print('고객님의 연령대는 50대 입니다.')
# elif age >= 40:
#     print('고객님의 연령대는 40대 입니다.')
# elif age >= 30:
#     print('고객님의 연령대는 30대 입니다.')
# elif age >= 20:
#     print('고객님의 연령대는 20대 입니다.')
# elif age >= 10:
#     print('고객님의 연령대는 10대 입니다.')
# elif age >= 0:
#     print('고객님의 연령대는 10대 미만 입니다.')
# else:
#     print('입력 오류입니다. 알맞은 숫자를 넣어 주세요.')



### 반복문

### 예시 6) 팩토리얼 구하기
# num = int(input('2 이상의 숫자를 입력해 주세요 : '))
# sum = 1
# for i in range(1,num+1):
#     sum *= i
# print(sum)


### 예시 7)
# num = int(input('구구단 몇 단을 계산할까요? : '))
# for i in range(1,num+1):
#     print('%d x %d = %d'%(num,i,num*i))


### 예시 8)
# for i in range(2,10):
#     print('%d단'%i)
#     for j in range(1,10):
#         print('%d x %d = %d'%(i,j,i*j))
#     print('')


### 예시 9)
# cnt = 0
# while 1:
#     print('*'*10)
#     cnt+=1
#     if cnt == 5:
#         break


### 예시 10)
# money = 1000
# year = 0
# while 1:
#     money = money*1.07
#     year += 1
#     if money >= 2000:
#         break
# print('%d년'%year)


### 예시 11)
## while문
# i = 1
# num = 0
# while i < 31:
#     if 30 % i == 0 and 75 % i == 0:
#         num = i
#     i += 1
# print(num)


## for문
# for i in range(1,31):
#     if 30 % i == 0 and 75 % i == 0:
#         num = i
#     i += 1
# print(num)

## 답지(while)
# i = 1
# gcm = 0
# while i < 31:
#         if 75 % i == 0 and 30 % i == 0: ## 30과 75의 최대공약수. 동시에 조건 달성되어야 함.
#                 gcm = i
#         i += 1 ## 들여쓰기 if문 안에 들어가지 않아도 실행될 수 있도록 주의
# print(gcm)

## 답지(for)
# for i in range(1,31):
#         if 75 % i == 0 and 30 % i == 0:
#                 gcm = i
# print(gcm)



### 4주차 복습

### 리스트

### 예시 1)
## 문제
# greetings = ['안녕', '니하오', '하이', '곤니찌와', '올라', '싸와디캅', '봉쥬르']

## coding here ##
# for i in greetings:
#     print(i)

## 실행결과
# # 안녕
# # 니하오
# # 하이
# # 곤니찌와
# # 올라
# # 싸와디캅
# # 봉쥬르


### 예시 2)
## 문제
# a = ['alpha','bravo','charlie','delta','ehco','foxtrot','golf','cat','school','hotel','india']

## coding here ##
# b = []
# for i in a:
#     if len(i)==5:
#         b.append(i)
# print(b)

## 실행결과
# # ['alpha', 'bravo', 'delta', 'hotel', 'india']



### 딕셔너리

### 예시 3)
## 문제
# words = {'사과':'apple','컴퓨터':'computer','학교':'school','책상':'desk','의자':'chair'}

## coding here ##
# print('-> 실행 결과')
# for i in words:
#     answer = input('%s에 해당하는 영어 단어를 입력해주세요: '%i)
#     if answer == words[i]:
#         print('정답입니다!')
#     else:
#         print('틀렸습니다!')

## 실행결과
# # -> 실행 결과
# # 사과에 해당하는 영어 단어를 입력해주세요: apple
# # 정답입니다!
# # 컴퓨터에 해당하는 영어 단어를 입력해주세요: com
# # 틀렸습니다!
# # 학교에 해당하는 영어 단어를 입력해주세요: school
# # 정답입니다!
# # 책상에 해당하는 영어 단어를 입력해주세요: tesk
# # 틀렸습니다!
# # 의자에 해당하는 영어 단어를 입력해주세요: chaaar
# # 틀렸습니다!

### 예시 4)
## 문제
# print('-> 실행 결과')
# scores = {'김예진': 90, '박영진': 95, '김소희': 84}
# sum = 0
# for i in scores:
#     sum += scores[i]
#     print('%s : %d'%(i,scores[i]))
# avg = sum/len(scores)
# print('합계 : %d, 평균 %.2f'%(sum,avg))

## 실행결과
# # -> 실행 결과
# # 김예진 : 90
# # 박영진 : 95
# # 김소희 : 84
# # 합계 : 269, 평균 89.67