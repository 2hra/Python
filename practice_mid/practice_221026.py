# f = open('result.txt','r')
# line = f.read()
# print(line)
# f.close()

# f = open('result.txt','r')
# lines = f.readline()
# print(lines)
# f.close()

# f = open('result.txt','r')
# while 1:
#     lines = f.readline()
#     print('%s'%lines, end='')
#     if not lines:
#         break    
# f.close()

# f = open('result.txt','r')
# liness = f.readlines()
# for i in liness:
#     print(i.strip())
# print(liness)

# f = open('test_221026.txt','w')
# for i in range(1,6):
#     f.write('%s\n'%('*'*int(6-i)))
# f.close()
# f1 = open('test_221026.txt','a')
# for i in range(1,6):
#     f1.write('%s\n'%('*'*i))
# f1.close()
# f2 = open('test_221026.txt','r')
# line = f2.read()
# print(line)
# f2.close()
# f3 = open('test_221026.txt','r')
# lines = f3.readline()
# print(lines)
# f3.close()
# f4 = open('test_221026.txt','r')
# while 1:
#     liness = f4.readline()
#     print(liness.strip())
#     if not liness:
#         break
# print(liness)
# f4.close()
# f5 = open('test_221026.txt','r')
# linesss = f5.readlines()
# print(linesss)
# f5.close()
# f6 = open('test_221026.txt','r')
# linessss = f6.readlines()
# for i in linessss:
#     print(i.strip())
# f6.close()

# data = {'데사B0002':'데이터마이닝이해와실습','문공A0015':'R프로그래밍', '문공A0016':'기초선형대수학'}
# answer = input('학수번호를 입력하세요 : ')
# if answer in data.keys():
#     if answer == '데사B0002':
#         place = '숭의관1호'
#     elif answer == '문공A0015':
#         place = '인문관2호'
#     else:
#         place = '대학원3호'
#     print('입력하신 과목은 %s 이며, 강의실은 %s 입니다.'%(data[answer],place))
# else:
#     print('입력하신 과목은 정보에 없습니다.')

# num = 25
# while 1:
#     answer = int(input('숫자를 입력하세요 : '))
#     if answer == num:
#         print('정답 !')
#         break
#     elif answer > num:
#         print('DOWN !')
#     else:
#         print('UP !')

# sum = 0
# for i in list(str(3**79)):
#     sum += int(i)
# print(sum)

# i = 1
# while i<=4:
#     print('%s'%('*'*(9-i*2)))
    # i += 1

# t = 35
# total = 0
# if t >= 31:
#     total = 20*430 + 10*570 + (t-30)*840
# elif t >= 21:
#     total = 20*430 + (t-10)*570
# else:
#     total = t*430
# print('%d원'%total)

# def no_(list):
#     new_list = []
#     for i in list:
#         if i in new_list:
#             pass
#         else:
#             new_list.append(i)
#     print(new_list)
# no_('happy together')

# def link(list):
#     print('www.'+list+'.com')
# link('happy')

# def para(v1,v2,v3=0):
#     result = 0
#     result = v1+v2+v3
#     return result
# print(para(1,2))