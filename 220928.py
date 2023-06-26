## 4주차
### 변수
## 문자 입력 시 큰 따옴표, 작은 따옴표 상관없음.

# print(len("Hello World")) ## len 함수는 띄어쓰기도 갯수에 포함

### int 정수형
### float 실수형
### str 문자열
### bool 참, 거짓

# x = 24
# y = float(x)
# z = str(x)
# print(type(x)) ## type 함수는 어떤 자료형인지 반환
# print(type(y))
# print(type(z))
# print(y)
# print(x+y) ## int+float는 float으로 결과 나옴.

# answer = input("숫자 입력: ") ## input으로 변수에 값 저장하면 뒤에 활용 가능
# print(type(answer)) ## 결과: str >> input은 무조건 str로 들어옴. 숫자로 쓰려면 앞에 지정 필요.
# answer2 = int(input("숫자 입력하세요: "))
# print(type(answer2)) ## 결과: int

### 대입연산자: 오른쪽 연산 후 왼쪽에 대입
# num1, num2 = 8, 4 ## 이렇게 할 순 있지만 하지 말기
# num1 = 8
# num2 = 4 ## 이렇게 적어야 오류 안 생김

# num1 = "8"
# num2 = "4" ## 숫자여도 문자열로 사용 가능
# print(num1+num2) ## 결과: 84

### 복합 대입 연산자
# x = 5
# x += 3 ## 간단하지만 기존 값 저장 안 됨. 기존 값 활용해야 하면 새로 선언하기.
## 실수 안 하려면 x = x + 3처럼 풀어 적는 게 제일 좋음.
# print(x)
# x *= 3
# print(x)

### 비교연산자
# x = 5
# if x==5: ## if와 콜론 사이가 true일 때만 돌아감. 비교연산자 활용해서 조건 작성.
#     print("Hello")



### 리스트 = 대괄호로 묶인 여러개의 자료형.
# score = [100, 90, 40, 30, 70]
# print(len(score))
# print(score[0]) ## 리스트명[순서] 입력 시 값 불러옴. 순서는 0부터 시작.

# num = [0,0,0,0,0] ## 리스트 내부 값 직접 입력하려면 원하는 갯수 이상만큼 칸 지정 필요
# num[0] = int(input("숫자 입력: "))
# num[1] = int(input("숫자 입력: "))
# num[2] = int(input("숫자 입력: "))
# num[3] = int(input("숫자 입력: "))
# print(num)




# # 위에 문제 나오고 아래 실행결과대로 돌아가도록 coding here 아래에 코드 작성. 
# # 단순 반복 출력시키면 만점은 못 줘도 부분점수는 줄 예정. 그래도 하지 마라.
# # 파이썬 파일 제출하는 게 중간고사 시험.
### 예시 1)  
## 문제)
# greetings = ['안녕', '니하오', '하이', '곤니찌와', '올라', '싸와디캅', '봉쥬르']

### coding here ##
# for i in greetings: ## 리스트는 range 함수 안 써도 되고, 변수 i에 greetings 안의 값을 하나씩 넣고 반복함.
#     print(i)

## 아래처럼 해도 동일한 결과. 하지만 위 코드가 더 깔끔.
# greetings = ['안녕', '니하오', '하이', '곤니찌와', '올라', '싸와디캅', '봉쥬르']
# for x in range(0,len(greetings)): 
#     print(greetings[x])

## 실행 결과
# # 안녕
# # 니하오
# # 하이
# # 곤니찌와
# # 올라
# # 싸와디캅
# # 봉쥬르

# print(len(greetings)) ## len 함수로 몇 개의 값이 있는지 알아볼 수 있음. >> 결과: 7



### append 함수
# greetings = ['안녕', '니하오', '하이', '곤니찌와', '올라', '싸와디캅', '봉쥬르']
# a = [1,2,3,4]
#a.append(10)
# print(a) ## 마지막에 값 추가 >> 결과: [1, 2, 3, 4, 10]

## a 리스트에 greetings 리스트 값 추가하기
# for i in greetings: 
#     a.append(i) 
# print(a) ## 결과: [1, 2, 3, 4, 10, '안녕', '니하오', '하이', '곤니찌와', '올라', '싸와디캅', '봉쥬르']
# print(len(a))

## 비어있는 b 리스트에 다른 리스트 값 넣어 주기.
# b=[] ## 빈 리스트 하나 선언해 줘야 append 함수 사용 가능.
# for i in greetings: 
#     b.append(i)
# print(b) ## ['안녕', '니하오', '하이', '곤니찌와', '올라', '싸와디캅', '봉쥬르']


### insert 함수 (잘 안 씀)
# a.insert(2,"hyora") ## 원하는 위치에 원하는 값 추가할 때 사용.
# print(a) ## 결과: [1, 2, 'hyora', 3, 4]


## append 안에 숫자, 문자 지정하면 그것만 반복해서 값 추가.
# numList = []
# for i in range(0,4):
#     numList.append(0)
# print(numList)

# numList1 = []
# for j in range(0,4):
#     numList1.append(j) ## 반복문 변수로 지정하면 숫자 증가함.
# print(numList1)


## 100칸까지 2의 배수 리스트 만들기.
# aa = []
# for i in range(100):
#     aa.append(2*i)
# print(aa)

## aa의 역순으로 리스트 만들기.
# bb = []
# print(len(aa))
# for i in range(0,len(aa)): ## 0부터 aa의 길이까지
#     bb.append(aa[99-i])
# print(bb)



### 리스트 값 접근
# a = [1,2,3,4]
# print(a[0])
# a[3]=5 ## 양수로 몇 번째인지 불러와서 값 변환 가능
# print(a)
# print(a[-2]) ## 뒤에서 두 번째. 마이너스는 뒤에서 카운트.
# print(a[0:2]) ## [이상:미만:간격]
# print(a[1:]) ## 미만 없으면 끝까지 다 출력
# print(a[::2]) ## 2칸씩 건너뛰어서 출력. 많이 쓰는 기능 아님.



### 리스트 연산
# a=[1,2,3,4]
# b=['a','b']
# print(a+b) ## 리스트 두 개 이어붙임
# print(a*2) ## 리스트명* == 반복

## 리스트 내의 값을 연산하고 싶다면?
# b = [] ## 신규 리스트에 넣고 싶으면 선언
# for i in a:
#     b.append(2*i) ## 연산 진행
# print(b) ## 값 추가된 새로운 리스트 출력. 그냥 값 출력만 하려면 반복문 내에 append 대신 print만 사용.



### 리스트 값 삭제
# A = [1,5,11,-3]

## del 함수
# del(A[1:3]) ## 값 순서 넣기
# print(A)

## remove 함수
# A.remove(11) ## 원하는 값 넣기
# print(A)

## pop 함수
# A.pop() ## 마지막 요소 하나 없어짐.
# print(A)



# a = [1,2,10,3,4]

### sort 함수
# a.sort() ## 순서대로 정렬. 이 아래로는 정렬된 순서로 사용해야 함.
# # print(a)
# a.sort(reverse=True) ## 역순 정렬
# print(a)
# a.reverse() ## 리스트 순서 거꾸로 뒤집기
# print(a)


### count 함수
# print(a.count(10)) ## 찾는 값이 리스트에 몇 개 들어있는지


### copy 함수
# a.reverse()
# b = a.copy ## copy 함수는 위에 빈 리스트 선언 안 해도 됨.
# print(b)



### 2차원 리스트
# aa = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(aa)
# print(aa[1][1]) ## 리스트명[행(리스트 순서)][열(리스트 내부 요소 순서)]
# print(aa[2][2]) ## 순서는 모두 0부터 시작한다.

# for i in range(0,3):
#     for j in range(0,4):
#         print(aa[i][j], end=" ") ## i는 리스트 순서, j는 i번째 리스트 내부 요소 순서
#         ## aa[0][0] -> aa[0][1] -> aa[0][2] -> aa[0][3] -> aa[1][0] -> ... 으로 반복
#     print("") ## 리스트별로 줄 바꿈 하고 싶으면


### 2차원 리스트 예시
# a = []
# b = []
# val = 0
# for i in range(0,4):
#     for j in range(0,5):
#         a.append(val) ## 0부터 값 추가 5번씩 반복
#         val += 3
#     b.append(a) ## a 리스트 값을 b 리스트에 추가
#     a = [] ## 리스트 비워 주고 새로운 값 또 추가
# print(b)



### 예시 2)
## 문제) 리스트 값 중 길이가 5인 것만 출력
# a = ['alpha', 'bravo', 'chalie', 'delta','echo','foxtrot','golf','cat','school','hotel','india']
## print(b) 를 했을 때 답이 나오도록

## coding here ## 
# b = []
# for i in a:
#     if len(i)==5:
#         b.append(i) ## 답안지에 위 네 줄만 제출하면 됨.
# print(b) ## 최종 결과값 얻으려면 들여쓰기 없이.

## 실행결과
## ['alpha', 'bravo','delta','hotel','india'] 결과가 대괄호니까 리스트라고 연상하기.



### 딕셔너리 == {}
## 키와 값이 매칭되어있음. 키는 중복되면 안 됨.

# professor = {'학번':'20221234', '이름':'김태완', "부서":"데이터사이언스전공"} ## 따옴표 종류는 상관없으나 키-값은 같은 종류로 써야 함.
# print(professor)

# professor['나이'] = 39 ## 값 추가하기. 기입력된 키를 새로 추가하면 기존에 내용 덮어쓰기 됨.
# print(professor)

# professor['이름'] = '홍길동'
# print(professor)

# del(professor['학번']) ## del 함수에 키 값만 넣으면 값까지 같이 삭제됨.
# print(professor)

# print(professor['나이']) ## 값 출력 접근 시 대괄호 열고 키 입력

# print(professor.keys()) ## 결과: dict_keys(['이름', '부서', '나이'])
# print(professor.values()) ## 결과: dict_values(['홍길동', '데이터사이언스전공', 39])
# print(professor.get('부서')) ## 결과: 데이터사이언스 전공. >> 값 접근하는 또 다른 방법

### dict_keys || dict_values 값 활용하고 싶으면 앞에 list 붙이기.
# print(list(professor.keys()))
# print(list(professor.values()))

# print('학번' in professor) ## 해당 키가 있는지 확인.


### 딕셔너리 함수
# professor = {'학번':'20221234', '이름':'김태완', "부서":"데이터사이언스전공", '나이':'39'}
# for i in professor.keys(): ## 키 갯수만큼 반복. i에는 key가 순서대로 대입됨.
#     # print(i) ## 키 출력
#     # print(professor[i]) ## i 키에 맞는 값 접근.
#     print(i, professor[i]) ## 키 값 으로 순서대로 출력.

# for i in professor.keys(): ## 이 반복문 외워 두기.
#     print(i, professor[i])


### 예시 3)
## 문제) 딕셔너리로 영단어 퀴즈 제작
# words = {'사과':'apple', '컴퓨터':'computer','학교':'school','책상':'desk','의자':'chair'}

## coding here ##
# print('-> 실행 결과')
# for i in words.keys():
#     answer = input("%s에 해당되는 영어 단어를 입력해주세요: " % i)
#     if answer == words[i]:
#         print('정답입니다!')
#     else: print('틀렸습니다!')

## 실행결과
# # -> 실행 결과
# # 사과에 해당되는 영어 단어를 입력해주세요: apple 
# # 정답입니다!
# # 컴퓨터에 해당되는 영어 단어를 입력해주세요: comm
# # 틀렸습니다!
# # 학교에 해당되는 영어 단어를 입력해주세요: school
# # 정답입니다!
# # 책상에 해당되는 영어 단어를 입력해주세요: tesk
# # 틀렸습니다!
# # 의자에 해당되는 영어 단어를 입력해주세요: ch
# # 틀렸습니다!



### 예시 4) 시험 문제랑 유사. 빈칸 채우기 많이 나옴.
## 문제) 딕셔너리로 성적 합계/평균 구하기
scores = {'김예진':90, '박영진':95, '김소희':84}
sum = 0

for key in scores:
    sum += scores[key]
    print('%s : %d' % (key, scores[key]))
print('합계 : %d, 평균 : %.2f' % (sum, sum/len(scores)))

## 실행결과
# # 김예진 : 90
# # 박영진 : 95
# # 김소희 : 84
# # 합계 : 269, 평균 : 89.67