# # 1. 교과목 정보 출력 ##
# number = input("학수번호를 입력하세요 :") 
# #### coding here ####
# data = ['데사B0002', '문공A0015', '문공A0016']
# class_data = 0
# place = 0
# if number in data:
#     if number == '데사B0002':
#         class_data = '데이터마이닝이해와실습'
#         place = '숭의관1호'
#     elif number == '문공A0015':
#         class_data = 'R프로그래밍'
#         place = '인문관2호'
#     else:
#         class_data = '기초선형대수학'
#         place = '대학원3호'
#     print('입력하신 과목은 %s 이며, 강의실은 %s 입니다.'%(class_data, place))
# else:
#     print('입력하신 과목은 정보에 없습니다.')



# ## 2. 숫자 맞추기 게임 ##
# answer = 25
# #### coding here ####
# while 1:
#     num = int(input('숫자를 입력하세요 : '))
#     if num == answer:
#         print('정답 !')
#         break
#     else:
#         if num > answer:
#             print('DOWN !')
#         else:
#             print('UP !')

    

# ## 3. 물건 값 계산하기 ##
# sum = 0

# for i in  list(str(3**79)):
#     sum += int(i)

# print(sum)



# ## 4. while문 이용 문제 ##
# ### coding here ####
# i = 1
# while i<5:
#     print('*'*(9-i*2))
#     i+=1



# ## 5. 상수도 요금 문제 ##
# ### coding here ####
# t = 35
# total = 0

# if t >= 31:
#     total = (t-30)*840 + 10*570 + 20*430
# elif t >= 21:
#     total = (t-20)*570 + 20*430
# else:
#     total = t*430
# print('%d원'%total)