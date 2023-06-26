# ### 조건문, 반복문

# # 학점은 3.7 이상이면 평타. 학점보다 공모전 수상 등 다른 부분에 신경쓰기
# # 코드 직접 짜 보고 남의 코드 비교해서 잘 짠 코드 분석하고 알아보는 것도 중요
# # 주석처리, 예외처리가 코드에서 가장 중요함. 둘을 잘해야 실력, 퀄리티가 좋아짐.
# # 개발자 원하면 c언어 자료구조 수업 꼭 듣기. 코테의 90%가 자구에서 나옴.

# # ctrl + k + c
# # ctrl + k + u 주석 해제



# ### if문
# a = 1
# if a > 0:
#     print("a가 0보다 큽니다.") 
# # f9 디버그 브레이크 포인트, f5 디버그 실행, f10 한 줄씩 실행, 조사식에 변수명 추가: 값이 뭔지 나옴
# # 브레이크 포인트 실행 안 되면 그 코드가 오류인 거니까 확인하기 쉬움

# # 예제 1번)
# password = "data" ## 대소문자 모두 구분 필요
# answer = input("비밀번호를 입력해 주세요 : ") ## input은 무조건 str로 받음. 
# if answer == password:
#     print("correct")

# # 예제 1-1번) else
# password = "data"
# answer = input("비밀번호를 입력해 주세요 : ")
# if answer == password:
#     print("correct")
# else:
#     print("false!!")

# # 예제 2번) 여러 숫자를 입력해 보면서 모든 경우 옳은 답이 나오는지 테스트하기
# answer = int(input("숫자를 입력해 주세요 :")) ## input 받기 전에 출력할 문구 꼭 괄호 안에 넣기
# if answer < 0 :
#     print("0보다 큰 숫자를 입력해 주세요.") ## 파이썬은 음수 양수 구분 안 하고 다 나머지 구할 수 있기 때문에.
# else:
#     ## answer > 0
#     if answer % 2 == 0: ## 중첩 if문
#         ## even number
#         print("입력하신 숫자는 짝수입니다.")
#     else: ## else가 아닌 if 중복 코드도 가능. if, else는 둘 중 하나만 실행됨. if 두 개는 모든 코드 다 거쳐야 하므로 비효율적
#         ## odd number
#         print("입력하신 숫자는 홀수입니다.")

# # 한 줄로 조건문 완성(잘 사용하지 않음)
# answer = int(input("숫자를 입력해 주세요 :"))
# message = "짝수" if answer % 2 == 0 else "홀수" # (True일 때 출력할 것) if 조건문 else (False일 때 출력할 것)
# print(message)

# # 예제 3번)
# score = int(input("점수를 입력하세요: "))
# if score >= 90: ## if, else만 사용하는 방법
#     print("A",end="")
# else:
#     if score>=80:
#         print("B",end="")
#     else:
#         if score>=70:
#             print("C",end="")
#         else:
#             if score>=60:
#                 print("D",end="")
#             else:
#                 print("F",end="")
# print("학점입니다.")

# score = int(input("점수를 입력하세요: "))
# if score >= 90:
#     print("A",end="")
# elif score>=80: ## elif 위에 무조건 if 있어야 함. else는 없어도 됨
#     print("B",end="")
# elif score>=70:
#     print("C",end="")
# elif score>=60:
#     print("D",end="")
# else:
#     print("F",end="")
# print("학점입니다.")

# # 예제 4번)
# telecom = input("고객님께서 사용 중이신 통신사를 입력해 주세요: ")
# telecom = telecom.upper()
# if telecom == "SKT":
#     print("고객님께서 사용 중이신 통신사는 SK텔레콤 입니다.")
# elif telecom == "KT":
#     print("고객님께서 사용 중이신 통신사는 KT 입니다.")
# elif telecom == "LG":
#     print("고객님께서 사용 중이신 통신사는 LG U+ 입니다.")
# else:
#     print("다시 입력해 주세요.")

# # 예제 5번)
# age = int(input("고객님의 나이를 입력해 주세요 : "))
# if age >= 60:
#     print("고객님의 연령대는 60대 이상 입니다.") ## 큰 숫자부터 if 시작하기
# elif age >= 50:
#     print("고객님의 연령대는 50대 입니다.")
# elif age >= 40:
#     print("고객님의 연령대는 40대 입니다.")
# elif age >= 30:
#     print("고객님의 연령대는 30대 입니다.")
# elif age >= 20:
#     print("고객님의 연령대는 20대 입니다.")
# elif age >= 10:
#     print("고객님의 연령대는 10대 입니다.")
# elif age > 0:
#     print("고객님의 연령대는 10대 이하 입니다.")
# else:
#     print("고객님의 나이는 0보다 커야 합니다.") ## 오류 관련 조건문도 같이 작성해 주기



# ### 반복문
# ### for문
# # range(시작값, 끝값+1, 증가값)
# for i in range(10): ## python, c는 0부터 시작. r은 1부터 시작. 
#     ## range(3) == range(0, 3, 1) == [0,1,2] >> 0, 1, 2 세 번 반복.
#     ## 값이 하나만 적혀 있으면 0부터 적힌 값 -1까지 반복.
#     print("i 값은 %d 입니다." % i)
#     # i 값은 0 입니다.
#     # i 값은 1 입니다.
#     # i 값은 2 입니다.

# for i in range(10):
#     print(i) ## 뒤에 엔터 숨어있음.

# # 예제 6번) 팩토리얼 (!) 3! = 3*2*1, 10! = 10*9*8*...
# # 내 풀이
# number = int(input("2 이상의 숫자를 입력해 주세요 : "))
# fac = 1
# for i in range(1, number+1):
#     fac = fac*i
# print(fac)

# # 교수님 풀이 6-1) 3의 팩토리얼 구하기
# import math
# print(math.factorial(3)) ## factorial 괄호 안에 숫자 입력하면 함수 활용 가능.

# # 교수님 풀이 6-2) 3의 팩토리얼 구하기 >> 내 풀이와 유사
# n = 3
# result = 1 ## 곱하기는 1부터, 더하기는 0부터 시작
# for i in range(1,n+1): ## (이상, 미만)
#     result *= i ## result = result * i
# print(result)

# # 교수님 풀이 6-3) ## 다시 보기
# def factorial(n): 
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# factorial(3)

# # 교수님 풀이 6-4) 재귀함수. 함수 안의 함수. 3*2!로 흘러가는 것.
# def factorial(n):
#     return n * factorial(n-1) if n > 1 else 1
# print(factorial(3))

# # 반복문 안에서 연산하려면 변수 초기값 선언 먼저 필수
# res = 0 
# for i in range(1, 11, 1):
#     res += i
# print(res)

# # 반복문 안에 조건문 입력 가능
# res = 0 
# for i in range(1, 11, 1):
#     res += i
#     if i == 5: ## 원하는 중간값 확인하기
#         print(res) 
# print("1부터 10까지의 합 = %d" % res) ## 최종값 확인하기

# # 1000부터 2000까지의 수 중 홀수의 합
# res = 0
# for i in range(1000,2001):
#     if i % 2 != 0:
#         res += i
# print("1000부터 2000까지의 수 중 홀수의 합 : %d" % res)

# # 예제 7번)
# dan = int(input("구구단 몇 단을 계산할까요? : "))
# for i in range(1,10):
#     print("%d x %d = %d" % (dan, i, dan*i))

# # 중첩 for문
# for i in range(3):
#     for j in range(2):
#         print("i 값은 %d이고, j 값은 %d입니다." % (i,j))
#         print("%d%d"%(i,j))
#         # 바깥 for문 안에 중첩 for문 있으면 내부 for문 다 돌고 빠져나가야 바깥 for문 다시 실행
#         # 안쪽 for문부터 실행된다.
#         # i 값은 0이고, j 값은 0입니다.
#         # 00
#         # i 값은 0이고, j 값은 1입니다.
#         # 01
#         # i 값은 1이고, j 값은 0입니다.
#         # 10
#         # i 값은 1이고, j 값은 1입니다.
#         # 11
#         # i 값은 2이고, j 값은 0입니다.
#         # 20
#         # i 값은 2이고, j 값은 1입니다.
#         # 21

# # 예제 8번)
# for i in range(2,10):
#     print("%d단" % i) ## 내가 문제에 추가함(깔끔하게 보려고)
#     for k in range(1,10):
#         print("%d x %d = %d" % (i, k, i*k))
#     print('') ## 내가 문제에 추가함(깔끔하게 보려고)



# ### while문 (while문 코드 명시 안 되어있으면 for문이 더 쉬움)
# # 아래 for문과 동일한 while문 만들기
# for i in range(3):
#     print(i)
# # 풀이
# i = 0
# while i < 3: ## while 뒤가 참이 될 때까지 반복
#     print(i)
#     i += 1

# # while문 별 찍기
# i = 0
# while i < 5:
#     print("*"*10)
#     i += 1 ## 마지막에 조건 만들어 주기
# # **********
# # **********
# # **********
# # **********
# # **********

# # while문은 무한루프로 사용. ctrl + c로 강제 종료 안 하면 무한 반복. for문에서는 완전한 무한루프 불가.
# while 1:
#         print("*"*10)

# # break문: 반복문 탈출시키는 것
# for i in range(5):
#         print("*"*10)
#         if i == 2: ## 0,1,2 세 번만 반복하고 중단하겠다는 조건문 추가
#                 break

# # continue문: 아무것도 실행 안 하고 다시 반복 돌아가는 것
# res = 0
# for i in range(10):
#         if i % 2 == 1:
#                 continue
#         else: res += i

# # 예제 11번) 30과 75의 최대 공약수를 출력해 보세요. (문제에 while문 필수라고 하지 않으면 최대한 for문 사용하기.)
# # 11-1) while문 풀이
# i = 1
# gcm = 0
# while i < 31:
#         if 75 % i == 0 and 30 % i == 0: ## 30과 75의 최대공약수. 동시에 조건 달성되어야 함.
#                 gcm = i
#         i += 1 ## 들여쓰기 if문 안에 들어가지 않아도 실행될 수 있도록 주의
# print(gcm)

# # 11-2) for문 풀이
# for i in range(1,31):
#         if 75 % i == 0 and 30 % i == 0:
#                 gcm = i
# print(gcm)