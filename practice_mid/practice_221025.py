# password = 'data'
# answer = input('비밀번호를 입력해 주세요: ')
# if password == answer:
#   print('correct')

# num  = int(input('숫자를 입력해 주세요 : '))
# if num <0:
#   print('0보다 큰 숫자를 입력해 주세요')
# else:
#   if num%2==0:
#     print('짝')
#   else:
#     print('홀')

# score = int(input('점수: '))
# if score >= 90:
#   print('a')
# elif score >= 80:
#   print('b')
# else:
#   print('f')

# answer = input('통신사 : ').upper()
# telecom = 0
# tel3 = ['SKT','SK','SK텔레콤','SK 텔레콤','KT','LG', 'LG U+', 'LG 유플러스']
# if answer in tel3:
#   if answer in (tel3[0:3]):
#     telecom = 'SK 텔레콤'
#   elif answer in (tel3[5:7]):
#     telecom = 'LG U+'
#   else:
#     telecom = 'KT'
#   print('고객님 통신사는 %s 입니다.'%telecom)
# else: 
#   print('오류')

# age = int(input('연령: '))
# ten = 0
# if age >= 60:
#   ten = '60대 이상'
# elif age >= 50:
#   ten = '50대'
# elif age >= 40:
#   ten = '40대'
# else:
#   ten = '30대 이하'
# print('고객님 연령대는 %s 입니다.'%ten)

# total = 1
# for i in range(1,8):
#   total *= i
# print(total)

# total = 1
# i = 1
# while i<=7:
#   total*=i
#   i+=1
# print(total)

# num = int(input('구구단 : '))
# for i in range(2,10):
#   print('%d x %d = %d'%(num,i,num*i))

# num = int(input("구구단?: "))
# i = 1
# while i<=9:
#   print("%d x %d = %d"%(num,i,num*i))
#   i+=1

# for i in range(2,10):
#   for j in range(1,10):
#     print("%d x %d = %d"%(i,j,i*j))

# i =2
# j =1
# while i<=9:
#   while j<=9:
#     print('%d x %d = %d'%(i,j,i*j))
#     j+=1
#   j =1
#   i+=1

# i = 0
# while i<5:
#   print('*'*10)
#   i+=1

# for i in range(0,5):
#   print('*'*10)

# money = 1000
# year =0
# while money <= 2000:
#   money*=1.07
#   year += 1
# print('%d년'%year)

# num = 0
# for i in range(1,31):
#   if 30%i==0 and 75%i==0:
#     num = i
# print(num)

# num = 0
# i = 1
# while i<=30:
#   if 30%i==0 and 75%i==0:
#     num = i
#   i+=1
# print(num)

# greetings = ['안녕','니하오','헬로']
# for i in greetings:
#   print(i)

# a = ['aaaaa','bbb','ccccc']
# b=[]
# for i in a:
#   if len(i)==5:
#     b.append(i)
# print(b)

# words = {'사과':'apple','컴퓨터':'computer','책상':'desk'}
# for i in words.keys():
#   answer = input('%s를 뜻하는 영어: '%i)
#   if answer == words[i]:
#     print('O')
#   else:
#     print('X')

# scores = {'김':90, '박':95, '이':84}
# sum = 0
# for i in scores:
#   sum+= scores[i]
#   print('%s : %d'%(i,scores[i]))
# print('합: %d, 평균: %d'%(sum, sum/len(scores)))

# def tae(s):
#   print(s)
# tae('hello')

# def n_plus_1(n):
#   result = n+1
#   # return result
#   print(result)
# # print(n_plus_1(4))
# n_plus_1(4)

# def make_url(str):
#   print('www.'+str+'.com')
# make_url('naver')

# def make_list(str):
#   print(list(str))
# make_list('naver')

# def make_list_no(str):
#   a = []
#   for i in list(str):
#     if i in a:
#       pass
#     else:
#       a.append(i)
#   print(a)
# make_list_no('facebook')

# def picknum(num):
#   a = []
#   for i in num:
#     if i % 2 == 0:
#       a.append(i)
#   print(a)
# picknum([3,4,5,6,7,8])

# def average(list):
#   result = sum(list)/len(list)
#   print(result)
# average([0,10,20,30,40,50,60,70,80,90,100])

# f = open('a.txt','r')
# line = f.readline()
# print(line)
# f.close()

# f = open('aaa.txt','r')
# while 1:
#   line = f.readline()
#   if not line:
#     break
#   print(line)
# f.close()

# f = open('even_number.txt','r')
# lines = f.readlines()
# for i in lines:
#   print(i)
# f.close()

# f = open('even_number.txt','r')
# lines = f.readlines()
# for i in lines:
#   print(i.strip())
# f.close()

# f = open('even_number.txt','r')
# lines = f.read()
# print(lines)
# f.close()

# f = open('even_number_221026.txt','w')
# for i in range(1,31):
#   if i%2==0:
#     f.write('%s\n'%str(i))
# f.close()
# f = open('even_number_221026.txt','r')
# read = f.read()
# print(read)
# f.close()

# star = open('star_221026.txt','w')
# for i in range(1,7):
#   star.write('%s\n'%('*'*i))
# star.close()
# star = open('star_221026.txt','a')
# for i in range(1,7):
#   star.write('%s\n'%('*'*(7-i)))
# star.close()
# star = open('star_221026.txt','r')
# read = star.read()
# print(read)
# star.close()

# f1 = open('test_221026.txt','w')
# f1.write('Life is too short')
# f1.close()
# f2 = open('test_221026.txt','r')
# print(f2.read())
# f2.close()