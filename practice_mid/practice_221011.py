## 2주차 예시 복습

## 예시 1)
# 문제)
# coding here #
password = input('비밀번호를 입력해 주세요 : ').lower()
if password == 'data':
    print('correct')
else:
    print('fail!')

## 예시 2)
# 문제)
# coding here #
num = int(input('숫자를 입력해 주세요 : '))
if num < 0:
    print('0보다 큰 숫자를 입력해 주세요.')
else:
    if num%2==0:
        print('입력하신 숫자는 짝수 입니다.')
    else:
        print('입력하신 숫자는 홀수 입니다.')

## 예시 3)
# 문제)
# coding here #
score = int(input())
if 100 <= score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
elif score < 60:
    print('E')
else:
    print('오류입니다.')

## 예시 4)
# 문제)
# coding here #
telecom = input('고객님께서 사용 중이신 통신사를 입력해 주세요 : ').upper()
tel3 = ['SKT', 'KT', 'LG']
if telecom in tel3: ## 3대 통신사에 해당될 경우
    answer = 0 ## 통신사 저장할 변수 초기화
    for i in tel3: ## 리스트 중 어떤 통신사에 해당되는지
        if telecom == i:
            if telecom == 'SKT':
                answer = 'SK 텔레콤'
            elif telecom == 'LG':
                answer = 'LG U+'
            else:
                answer = telecom
        else:
            pass
    print('고객님께서 사용 중이신 통신사는 %s 입니다.'%answer)
else: ## 통신사 해당되지 않을 경우
    print('잘못 입력하셨습니다.')

## 예시 5)
# 문제)
# coding here #
age = int(input('고객님의 나이를 입력해 주세요 : '))
ten = int(age/10)
if age > 0:
    if age >= 70:
        ten = '60대 이상'
    elif age < 10:
        ten = '10대 미만'
    else:
        ten = '%d대'%(ten*10)
    print('고객님의 연령대는 %s 입니다.'%ten)
else:
    print('입력 오류입니다.')

## 예시 6)
# 문제)
# coding here #
num = int(input('2 이상의 숫자를 입력해 주세요 : '))
fac = 1
for i in range(1,num+1):
    fac*=i
print(fac)

## 예시 7)
# 문제)
# coding here #
num = int(input('구구단 몇 단을 계산할까요? : '))
for i in range(1,10):
    print('%d x %d = %d'%(num,i,num*i))

## 예시 8)
# 문제)
# coding here #
for i in range(2,10):
    print('--- %d단 ---'%i)
    for j in range(1,10):
        print('%d x %d = %d'%(i,j,j*i))
    print('')

## 예시 9)
# 문제)
# coding here #
for i in range(1,6):
    print('*'*10)

i=0
while i != 5:
    print('*'*10)
    i+=1

## 예시 10)
# 문제)
# coding here #
money = 1000
year = 0
while money < 2000:
    money = money*1.07
    year += 1
print('%d년'%year)

# 예시 11)
문제)
coding here #
i=1
cnt=0
while i<31:
    if(30%i==0 and 75%i==0):
        cnt = i
    i+=1
print(cnt)

cnt = 0
for i in range(1,31):
    if 30%i==0 and 75%i==0:
        cnt = i
        i+=1
print(cnt)


## 3주차 예시 복습

## 예시 1)
# 문제)
greetings = ['안녕', '니하오', '하이','곤니찌와','올라','싸와디캅','봉쥬르']
# coding here #
for i in greetings:
    print(i)

i = 0
while i<=int(len(greetings)-1):
    print(greetings[i])
    i+=1


## 예시 2)
# 문제)
a = ['alpha','bravo','charlie','delta','echo','foxtrot','golf','cat','school','hotel','india']
# coding here #
b = []
for i in a:
    if len(i)==5:
        b.append(i)
    else:
        pass
print(b)

b = []
i = 0
while i<len(a):
    if len(a[i]) == 5:
        b.append(a[i])
    else:
        pass
    i += 1
print(b)


## 예시 3)
# 문제)
words = {'사과':'apple', '컴퓨터':'computer','학교':'school','책상':'desk','의자':'chair'}
# coding here #
for i in words.keys():
    answer = input('%s에 해당되는 영어 단어를 입력해주세요 : '%i).lower()
    if answer == words[i]:
        print('정답입니다!')
    else:
        print('틀렸습니다!')

i = 0
keys = list(words.keys())
while i<=len(keys)-1:
    answer = input('%s에 해당되는 영어 단어를 입력해주세요 : '%keys[i]).lower()
    if answer == words[keys[i]]:
        print('정답입니다!')
    else:
        print('틀렸습니다!')
    i += 1


## 예시 4)
# 문제)
scores = {'김예진': 90, '박영진':95, '김소희':84}
# coding here #
sum = 0
for i in scores:
    sum += scores[i]
    print('%s : %d'%(i,scores[i]))
avg = sum/len(scores)
print('합계 : %d, 평균 : %.2f'%(sum,avg))

i = 0
sum = 0
keys = list(scores.keys())
while i <= len(scores)-1:
    sum += scores[keys[i]]
    print('%s : %d'%(keys[i], scores[keys[i]]))
    i += 1
avg = sum/len(scores)
print('합계 : %d, 평균 : %.2f'%(sum,avg))