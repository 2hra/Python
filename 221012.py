### 6주차

### 문자열
a = 'hello'
print(a[0])
print(a[-1])
print(a[1:3])

## Q. result에 값을 넣어서 일정 부분 출력하고 싶을 때
result = a[0]+a[-1]
print(result)

## 덧셈(이어붙이기), 곱셈(반복) 가능
print(a*2)
print(a+'hi')
b = '김태완'+'교수님'
print(b)
print(len(b)) ## len은 공백도 카운트

for i in range(0,len(b)):
    print(b[i], end='')

## 문자열 찾기 함수.
word = '공부가 너무 재미있어서 공부도 공부만 하고 싶어요'

## .count('검색할 단어') == 해당 단어가 몇 개인지 찾을 때
print(word.count('공부')) ## 3
print(word.count(' ')) ## 6

## .find('') == 해당 단어가 시작하는 인덱스를 찾을 때.
print(word.find('공부')) ## 왼쪽부터 찾아서 먼저 나오는 것. == 0
print(word.find('하하')) ## 없으면 -1
print(word.rfind('공부')) ## 오른쪽부터 찾아서 먼저 나오는 것. == 17

## .index('') == 리스트 내에 해당 단어 인덱스를 찾을 때.
x = ['DATA','SCIENCE','BLACK']
print(x.index('SCIENCE'))


## 문자열 공백 삭제
word = '      공부가 너무 재미있어서 공부도 공부만 하고 싶어요        '
print(word.strip()) ## 왼, 오 공백 삭제.
print(word.lstrip()) ## 왼 공백 삭제.
print(word.rstrip()) ## 오 공백 삭제.

 
## .replace('','') == 문자열 공백 변경
print(word.replace('공부','노래')) ## 앞 단어를 뒤 단어로 변경.


## .split() == 괄호 안이 비어있으면 띄어쓰기 단위, 어떠한 요소가 있으면 그 요소를 기준으로 분리.
word = '공부!가 너무 재미있!어서 공!부도 공부만 하!고 싶어요'
word_ = word.split() ## 띄어쓰기 단위로 음절 분석해서 리스트에 담음.
for i in word_:
    print(i)
# 공부가
# 너무
# 재미있어서
# 공부도
# 공부만
# 하고
# 싶어요
word1 = word.split('!')
print(word1) ## ['공부', '가 너무 재미있', '어서 공', '부도 공부만 하', '고 싶어요']


## .join() == 리스트내 요소 사이에 무엇을 넣고 하나의 문자열로 만들지
a = ['1','2','3','a','b','c']
print(''.join(a)) ## 123abc
print('*'.join(a)) ## 1*2*3*a*b*c
answer2 = '010''1234''5678'
print('-'.join(answer2))

## 예시)
answer = '010-1234-5678'
print(answer.replace('-',''))
answer1 = '010 1234 5678'
print(answer1.replace(' ','-'))
answer = 'A학생 결과를 다 처리했습니다.'
print(answer.replace('A','B'))

# if answer.find('-'):
#     ...    
# elif:
#     ... ## 이처럼 원하는 형태 하나로 통일하고 싶을 때 조건문으로 전처리.



### 함수

## 함수 이용 전
score=[90, 80, 90, 4, 15, 70, 55, 60, 88, 92]
avg = sum(score)/len(score)
print(avg)

## 함수 이용 후 == 동일한 코드 생략 가능.
def calculate_avg(list):
    average = sum(list)/len(list)
    return average

a = [90, 50, 40]
print(calculate_avg(a))

b = [100, 80, 40, 30, 60, 88]
print(calculate_avg(b))

## 예시)
def make_new_string(a):
    result = a[0] + a[-1]
    return result
a = 'school'
print(make_new_string(a))
b = 'university'
print(make_new_string(b))

def make_new_string1(a):
    result = a[0] + a[-1]
    print(result)
make_new_string1(a)
## 함수 내에 프린트 넣으면 함수 호출 시엔 이름(변수명)만.
## 리턴만 하면 프린트(함수(변수명))으로. 프린트 중복되지 않도록 주의.

b = ['010','1234','5678']
def phonenumber(x):
    result = '-'.join(x)
    return result
print(phonenumber(b)) ## 함수명 우클릭 >> go to definition, 함수 정의로 이동 가능.

def plus(num1, num2):  ## 괄호 안의 요소 갯수 중요. 정의 요소 갯수 == 입력 요소 갯수
    result = 0
    result = num1 + num2
    return result ## 반환할 거 없으면 리턴 안 넣음.
hap = 0
hap = plus(100,200)
print(hap)

def func3(): ## 입력 없이 함수 생성 가능. 반환값 여러개 설정 가능.
    result1 = 10
    result2 = 20
    return result1, result2
x, y = func3()
print(x,y)

def para2_func(n1,n2):
    result = 0
    result = n1+n2
    return result
def para3_func(n1,n2,n3):
    result = 0
    result = n1+n2+n3
    return result
hap = 0
print('2개의 합: %d'%para2_func(1,2))
print('3개의 합: %d'%para3_func(1,2,3))

def calculate_mul(a,b,c=1): ## 뒤의 값에 1 초기화 해 두면 아래 입력값 갯수 안 맞아도 답 추출 가능. c까지 입력하게 되면 덮어쓰기로 계산.
    result = 0
    result = a*b*c
    return result
res = calculate_mul(4,5)
print(res)
res = calculate_mul(4,5,7)
print(res)


## 예시 1)
def taewan(s,t):
    print(s,t)
taewan('hello','bye')
# taewan() ## 입력값 없다고 오류 발생.

## 예시 2)
def n_plus_1(n):
    result = n + 1
    return result
aaaaa = n_plus_1(3)
print(aaaaa)

## 예시 3)
def make_url(string):
    result = 'www.'+string+'.com'
    print(result) ## 프린트가 함수 밖에 있었다면 return을 써야 함.
make_url('naver') ## www.naver.com
make_url('facebook') ## www.facebook.com

## 예시 4)
def make_list(string):
    # print(list(string)) ## 이건 팁.
    list = []
    for i in string:
        list.append(i)
    print(list)
make_list('naver') ## ['n', 'a', 'v', 'e', 'r']
make_list('facebook') ## ['f', 'a', 'c', 'e', 'b', 'o', 'o', 'k']

# 4-1) 중복 없애기까지
def make_list(string):
    list = []
    for i in string:
        if i in list:
            continue
        else:
            list.append(i)
    print(list)
make_list('facebook') ## ['f', 'a', 'c', 'e', 'b', 'o', 'k']
make_list('astastast')

## 4-2)
def make_list(string):
    list = []
    for i in string:
        list.append(i)
        ## 중복 제거 함수 찾아보기
    print(list)
make_list('facebook')
make_list('astastast')

## 예시 5)
def pickup_even(items):
    new = []
    for i in items:
        if i%2==0:
            new.append(i)
    print(new)
pickup_even([3,4,5,6,7,8])

## 예시 6)
scores = [80,75,91,47,66,82,57,65,90,91,33,39,78,59,40,23,19,99,75,79,37,48,82,60,60,63,100,8,12,92,32,50,61,28,84,40,100,25,94,74,88,94,100,5,26]
def avergage(list):
    avg = sum(list)/len(list)
    return avg
print(avergage(scores))



### 파일 읽기
f = open('a.txt','r')

### 파일 쓰기
line = f.readline()
print(line)

### 파일 닫기 >> 무조건 작업 끝나면 닫아 줘야 한다!!
f.close() ## 변수명.close()


for i in range(1,100): ## 아래 돌리기 위한 예시
    name = str(i)
    filename = 'score'+name+'.txt'
    print(filename)

import os
for i in range(1,100):
    name = str(i)
    filename = 'score'+name+'.txt'
    # f = open(filename, 'r') ## 파일 돌아가면서 다 읽기. 현업에서 필수.
    if os.path.exists(filename): ## 위에서 좀 더 발전. 파일 있을 때만 열어라.
        f = open(filename, 'r')
        f.close() ## 안 닫으면 오류로 중단됨. 시험에서도 안 적으면 오답.


## 모든 줄 읽기(readlines 알아두기)
f = open('b.txt','r')
line = f.readlines()
print(line) ## ['1 2 3 4 5\n', 'a b c']
f.close()

f = open('b.txt','r')
while 1: ## 몇 줄인지 모르니 무한 반복 하다가
    line = f.readline()
    if not line : break ## 줄 없으면 중단
    print(line)
f.close()

f = open('b.txt','r')
lines = f.readlines() ## 줄줄이 리스트
for i in lines:
    print(i.strip()) ## strip()으로 엔터, 공백 등 제외 후 출력
f.close()


## 파일 쓰기 = open('파일','w') & 변수명.write >> 기존 파일 내용 지우고 새로 내용 입력
name = "taewan 20211648"
f = open("20211648.txt","w")
f.write(name)
f.close()

with open('aaa.txt','w') as f:
    f.write(name)

## 텍스트 파일에 별 피라미드 그리기
f = open('result.txt','w')
for i in range(1,11):
    a = '*'*i
    f.write(a+'\n')
f.close()

## 텍스트 파일에 별 피라미드 거꾸로 그리기
f = open('result.txt','w')
for i in range(1,11):
    a = '*'*(11-i)
    f.write(a+'\n')
f.close()


## 파일 쓰기 open('파일명','a') >> 기존 파일 맨 마지막에 추가.
f = open('result.txt','w')
for i in range(1,11):
    a = '*'*i
    f.write(a+'\n')
f.close()
f = open('result.txt','a')
for i in range(1,11):
    a = '*'*(11-i)
    f.write(a+'\n')
f.close()
f = open('result.txt','a')
f.write('today is 22/10/12')
f.close()



## 예제 7)
f = open('even_number.txt','w')
for i in range(1,31):
    if i%2==0:
        f.write(str(i)+'\n')
    else:
        continue
f.close()

## 예제 8)
f = open('star.txt','w')
for i in range(1,7):
    res = '*'*i+'\n'
    f.write(res)
f.close()

## 예제 9)
f1 = open('test.txt','w')
f1.write('Life is too short')
f1.close()
f2 = open('test.txt','r')
print(f2.read())