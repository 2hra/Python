# ## 2주차 조건문

# ## 1)
# password = 'data'
# answer = input('비밀번호를 입력해 주세요 : ')
# if password == answer:
#     print('correct')
# else:
#     print('false!')

# ## 2)
# num = int(input('숫자를 입력해 주세요 : '))
# if num > 0:
#     if num%2==0:
#         print('짝수')
#     else:
#         print('홀수')
# else:
#     print('0보다 큰 숫자를 입력해 주세요.')

# ## 3)
# score = int(input('시험 점수 : '))
# if score >=90:
#     print('A')
# elif score >=80:
#     print('B')
# elif score >=70:
#     print('C')
# elif score >=60:
#     print('D')
# else:
#     print('F')

# ## 4)
# answer = input('고객님께서 사용 중이신 통신사를 입력해 주세요 : ').upper()
# if answer == ('SK' or 'SKT'):
#     answer = 'SK 텔레콤'
# elif answer == 'LG':
#     answer = 'LG U+'
# print('고객님께서 사용 중이신 통신사는 %s 입니다.'%answer)

# ## 5)
# age = int(input('고객님의 나이를 입력해 주세요 : '))
# ten = int(age/10)
# if ten >=6:
#     age = '60대 이상'
# elif ten<1:
#     age = '10대 미만'
# else:
#     age = '%d'%(ten*10)+'대'
# print('고객님의 연령대는 %s 입니다.'%age)



# ## 2주차 반복문

# # 1)
# fac = int(input('2 이상의 숫자를 입력해 주세요 : '))
# total = 1
# for i in range(1,fac+1):
#     total*=i
# print(total)

# # 1-1)
# num = int(input('숫자를 입력하세요 : '))
# i = 1
# total = 1
# while i<=num:
#     total*=i
#     i+=1
# print(total)

# ## 2)
# num = int(input('구구단 몇 단을 계산할까요? : '))
# for i in range(1,10):
#     print('%d x %d = %d'%(num,i,num*i))

# ## 2-1)
# num = int(input('구구단 몇 단? : '))
# i = 1
# while i<10:
#     print('%d x %d = %d'%(num,i,num*i))
#     i+=1

# ## 3)
# for i in range(2,10):
#     for j in range(1,10):
#         print('%d x %d = %d'%(i,j,i*j))
#     print('')

# ## 3-1)
# i = 2
# while i<10:
#     j = 1
#     while j<10:
#         print('%d x %d = %d'%(i,j,i*j))
#         j+=1
#     i+=1
#     print('')

# # 4)
# i=1
# while i<=5:
#     print('*'*10)
#     i+=1

# # 4-1)
# for i in range(1,6):
#     print('*'*10)

# # 5)
# money = 1000
# year = 0
# while money <= 2000:
#     money*=1.07
#     year += 1
# print('%d년'%year)

# ## 5-1)
# money = 1000
# year = 0
# for i in range(1,999):
#     if money<2000:
#         money*=1.07
#         year +=1
#     else:
#         break
# print('%d년'%year)

# ## 6)
# cnt = 0
# for i in range(1,31):
#     if 30%i==0 and 75%i==0:
#         cnt = i
# print(cnt)

# ## 6-1)
# i = 1
# cnt = 0
# while i<31:
#     if 30%i==0 and 75%i==0:
#         cnt = i
#     i+=1
# print(cnt)



# ## 4주차 복습

# ## 1)
# greetings = ['안녕','니하오','하이','곤니찌와','올라','싸와디캅','봉쥬르']
# for i in greetings:
#     print(i)

# ## 2)
# a = ['alpha','bravo','chalie','delta','echo','foxtrot','golf','cat','school','hotel','india']
# b=[]
# for i in a:
#     if len(i)==5:
#         b.append(i)
# print(b)

# # 3)
# words = {'사과':'apple','컴퓨터':'conputer','학교':"school",'책상':'desk','의자':'chair'}
# for i in words.keys():
#     answer = input("%s에 해당되는 영어 단어를 입력해주세요 : "% i)
#     if answer == words[i]:
#         print('정답입니다!')
#     else:
#         print('틀렸습니다!')

# ## 4) 
# scores = {'김':90,'박':95,'함':84}
# sum = 0
# for i in scores.keys():
#     print('%s : %d'%(i,scores[i]))
#     sum += scores[i]
# print('합계 : %d, 평균 : %.2f'%(sum,sum/len(scores)))

# ## 4-1)
# sum = 0
# i = 0
# nList = list(scores.keys())
# while i<len(scores):
#     print('%s : %d'%(nList[i], scores[nList[i]]))
#     sum += scores[nList[i]]
#     i += 1
# print('합계 : %d, 평균 : %.2f'%(sum, sum/len(scores)))



# ## 6주차 복습

# ## 1) 
# def df(s):
#     print(s)
# df('Hello')

# ## 2)
# def n_plus_1(n):
#     result=n+1
#     return result
# result = n_plus_1(3)
# print(result)

# ## 3)
# def make_url(str):
#     print('www.'+str+'.com')
# make_url('naver')

# ## 4)
# def make_list(str):
#     result = list(str)
#     print(result)
# make_list('naver')
# make_list('facebook')

# ## 5) 
# def make_list_notO(str):
#     a = []
#     for i in list(str):
#         if i in a:
#             pass
#         else:
#             a.append(i)
#     print(a)
# make_list_notO('facebook')

# ## 6)
# def pickup_num(n):
#     a = []
#     for i in n:
#         if i%2==0:
#             a.append(i)
#     print(a)
# pickup_num([3,4,5,6,7,8])

# ## 6-1)
# def pick_num(n):
#     b=[]
#     i=0
#     while i<len(n):
#         if n[i]%2==0:
#             b.append(n[i])
#         i+=1
#     print(b)
# pick_num([3,4,5,6,7,8])

# ## 7)
# scores = [80,75,91,47,66,82,57,65,90,91,33,39,78,59,40,23,19,99,75,79,37,48,82,60,60,63,100,8,12,92,32,50,61,28,84,40,100,25,94,74,88,94,100,5,26]
# def average(n):
#     return sum(n)/len(n)
# print(average(scores))

# ## 8)
# import os
# filename = 'tony.txt'
# if os.path.exists(filename):
#     f = open(filename,'r')
#     lines=f.readlines()
#     f.close()
# else:
#     print('%s 파일이 없습니다.'%filename) ## 시험은 x

# ## 9)
# f = open('even_number_221016.txt','w')
# for i in range(1,31):
#     if i%2==0:
#         f.write('%s\n'%str(i))
#     else: pass
# f.close()
# f = open('even_number_221016.txt','r')
# read=f.read()
# print(read)
# f.close()

# ## 10)
# f = open('star_221016.txt','w')
# for i in range(1,7):
#     f.write('%s\n'%('*'*i))
# f.close()

# ## 10-1)
# f = open('star_221016.txt','a')
# for i in range(1,7):
#     f.write('%s\n'%('*'*(7-i)))
# f.close

# ## 11)
# f1 = open('test_221016.txt','w')
# f1.write('Life is short')
# f1.close()
# f2 = open('test_221016.txt','r')
# print(f2.read())
# f2.close()