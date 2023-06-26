# ## 2주차 예시 복습

# ## 1)
# password = input('비밀번호를 입력해 주세요 : ')
# if password == 'data':
#     print('correct')
# else:
#     print('fail')


# ## 2)
# num = int(input('숫자를 입력해 주세요 : '))
# if num > 0:
#     if num%2==0:
#         print('짝수입니다.')
#     else:
#         print('홀수입니다.')
# else:
#     print('0보다 큰 숫자를 입력해 주세요.')


# ## 3)
# score = int(input('점수를 입력해 주세요 : '))
# hak = 0
# if score >= 90:
#     hak = 'A'
# elif score >= 80:
#     hak = 'B'
# elif score >= 70:
#     hak = 'C'
# elif score >= 60:
#     hak = 'D'
# else:
#     hak = 'F'
# print('당신의 학점은 %s입니다.'%hak)


# ## 4)
# tel3 = ['SKT', 'SK', 'LG','KT']
# answer = input('고객님께서 사용 중이신 통신사를 입력해 주세요 : ').upper()
# if answer in tel3:
#     if answer == 'SKT' or answer == 'SK':
#         answer = 'SK 텔레콤'
#     elif answer == 'LG':
#         answer = 'LG U+'
#     else: pass
#     print('고객님께서 사용 중이신 통신사는 %s 입니다.'%answer)
# else:
#     print('입력 오류입니다.')


# # 5)
# age = int(input('고객님의 나이를 입력해 주세요 : '))
# n = 0
# for i in (1,age):
#     if age > 60:
#         n = '60대 이상'
#     if age >= 60:
#         n = '60대'
#     elif age >= 50:
#         n = '50대'
#     elif age >= 40:
#         n = '40대'
#     elif age >= 30:
#         n = '30대'
#     elif age >= 20:
#         n = '20대'
#     elif age >= 10:
#         n = '10대'
#     elif age < 10:
#         n = '10대 미만'
#     else:
#         print('입력 오류입니다.')
#         break
# print('고객님의 연령대는 %s 입니다.'%n)


# ## 6)
# fac = int(input('2 이상의 숫자를 입력하세요 : '))
# total = 1
# if fac < 2:
#     print('오류입니다.')
# else:
#     for i in range(1,fac+1):
#         total *= i
# print(total)

# fac = int(input('2 이상의 숫자를 입력하세요 : '))
# i = 1
# total = 1
# while i<=fac:
#     total*=i
#     i+=1
# print(total)


# ## 7)
# dan = int(input('구구단 몇 단을 계산할까요? : '))
# for i in range(1,10):
#     print('%d x %d = %d'%(dan, i, i*dan))

# dan = int(input('구구단 몇 단? : '))
# i = 1
# while i<10:
#     print('%d x %d = %d'%(dan, i, dan*i))
#     i+=1


# ## 8) 
# for i in range(2,10):
#     for j in range(1,10):
#         print('%d x %d = %d'%(i,j,i*j))
#     print('')

# dan = 2
# while dan<10:
#     n = 1
#     while n<10:
#         print('%d x %d = %d'%(dan, n, dan*n))
#         n += 1
#     dan += 1
#     print('')


# ## 9)
# for i in range(1,6):
#     print('*'*10)

# star = 0
# while star<5:
#     print('*'*10)
#     star += 1


# ## 10)
# money = 1000
# year = 0
# while money < 2000:
#     year+=1
#     money *= 1.07
# print('%d년'%year)

# money = 1000
# for i in range(0,999):
#     if money < 2000:
#         money *= 1.07
#     else:
#         break
# print('%d년'%i)


# ## 11)
# cnt = 0
# for i in range(1,31):
#     if 30%i==0 and 75%i==0:
#         cnt = i
# print(cnt)

# cnt = 0
# i = 1
# while i<31:
#     if 30%i==0 and 75%i==0:
#         cnt = i
#     i += 1
# print(cnt)



# ## 4주차

# ## 1)
#  greetings = ['안녕','니하오','하이','곤니찌와','올라','싸와디캅','봉쥬르']

# for i in greetings:
# #     print(i)

# i = 0
# while i<len(greetings):
#     print(greetings[i])
#     i+=1


# ## 2)
# a=['alpha','bravo','charile','delta','echo','foxtrot','golf','cat','school','hotel','india']

# b=[]
# for i in a:
#     if len(i)==5:
#         b.append(i)
# print(b)    

# i = 0
# b = []
# while i<=len(a)-1:
#     if len(a[i]) == 5:
#         b.append(a[i])
#     i+=1
# print(b)


# ## 3)
# words = {'사과':'apple','컴퓨터':'computer','학교':'school','책상':'desk','의자':'chair'}

# for i in words.keys():
#     answer = input('%s에 해당되는 영어 단어를 입력해주세요 : '%i)
#     if answer == words[i]:
#         print('정답입니다!')
#     else:
#         print('틀렸습니다!')

# i = 0
# list = list(words.keys())
# while i<len(words):
#     answer= input('%s에 해당되는 영어 단어를 입력해주세요 : '%list[i])
#     if answer == words[list[i]]:
#         print('정답입니다!')
#     else:
#         print('틀렸습니다!')
#     i+=1


# ## 4)
# scores = {'김예진':90, '박영진':95,'김소희':84}

# sum = 0
# for i in scores.keys():
#     sum+=scores[i]
#     print('%s : %d'%(i,scores[i]))
# avg = sum/len(scores)
# print('합계 : %d, 평균 : %.2f'%(sum, avg))

# sum = 0
# i = 0
# scoresKeyList = list(scores.keys())
# while i<len(scores):
#     sum += scores[scoresKeyList[i]]
#     print('%s : %d'%(scoresKeyList[i],scores[scoresKeyList[i]]))
#     i+=1
# avg = sum/len(scores)
# print('합계 : %d, 평균 : %.2f'%(sum, avg))



# ## 6주차

# ## 1)
# def t(s):
#     print(s)
# t('hello')
# # t() 정의와 다르면 호출 오류


# ## 2) 
# def n_plus_1(n):
#     result = n+1
#     return result # (2) 반환 넣어 주고
# n_plus_1(3)
# # print(result) # (1) 전역과 지역은 따로 선언 필요
# result = n_plus_1(3) # (3) 전역에 변수 선언해 주고
# print(result) # (4) 출력하기


# ## 3)
# def make_url(a):
#     print('www.'+a+'.com')
# make_url('naver')
# make_url('twitter')


# ## 4)
# def make_list(string):
#     n_list = list(string)
#     print(n_list)
# def make_list1(string):
#     n_list = []
#     base = list(string)
#     for i in base:
#         if i in n_list:
#             pass
#         else:
#             n_list.append(i)
#     print(n_list)

# make_list('naver')
# make_list('facebook') ## 그대로 출력
# make_list1('yellow window') ## 중복 제외 후 출력


# ## 5)
# def pickup_even(items):
#     new = []
#     for i in items:
#         if i%2==0:
#             new.append(i)
#     print(new)
# pickup_even([3,4,5,6,7,8])


# ## 6)
# def average(list):
#     return sum(list)/len(list)
# scores = [80,75,91,47,66,82,57,65,90,91,33,39,78,59,40,23,19,99,75,79,37,48,82,60,60,63,100,8,12,92,32,50,61,28,84,40,100,25,94,74,88,94,100,5,26]
# print(average(scores))


# ## 7)
# f = open('even_number_221014.txt','w')
# for i in range(1,31):
#     if i%2==0:
#         f.write('%s\n'%i)
#     else: pass
# f.close

# f = open('even_number_221014.txt','r')
# read = f.read()
# print(read)
# f.close()


# ## 8)
# f = open('star_221014.txt','w')
# for i in range(1,7):
#     f.write('*'*i+'\n')
# f.close()

# f = open('star_221014.txt','a')
# for i in range(1,7):
#     f.write('*'*(7-i)+'\n')
# f.close()


# ## 9)
# f1 = open('test_221014.txt','w')
# f1.write('Life is too short')
# f1.close()
# f2 = open('test_221014.txt','r')
# print(f2.read())
# f2.close()

# f = open('star_221014.txt','r')
# print(f.readlines())
# f.close()