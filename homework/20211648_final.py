##### 2022-2학기 데이터마이닝이해와실습 (데사B0002 3차 과제) #####
##### 학번 : 20211648
##### 이름 : 이효라
##### 제출할 때 파일명을 학번.py로 변경해서 제출하시기 바랍니다.



# ### 1번 문제 ###
# answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

# A = ['hello', 62, 'umbrella', 145]
# B = ['September', 512.3, 'coffe', 39, 'keyboard','notebook', 0.5, 'f12']
# C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

# ### coding here ####
# new_answer = input('리스트를 입력하세요 : ').upper()

# def check(x):
#     for i in new_answer:
#         if i in answer:
#             print('O', end='')
#         else:
#             print('X', end='')

# if new_answer == 'A':
#     new_answer = A
#     check(new_answer)
# elif new_answer == 'B':
#     new_answer = B
#     check(new_answer)
# elif new_answer == 'C':
#     new_answer = C
#     check(new_answer)
# else:
#     print('리스트에 없습니다.')



# ### 2번 문제 ###
# def find_capitalcity(capital, country):
#     #### coding here ####
#     for i in capital.keys():
#         if i == country:
#             return capital[i]

# capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이","덴마크":"코펜하겐"}

# print(find_capitalcity(capital, "대한민국"))
# print(find_capitalcity(capital, "덴마크"))



# ### 3번 문제 ###
# number = int(input('최대 숫자: '))
# rule = ['3','6','9']
# clap = 0
# for i in range(1,number+1):
#     x = str(i)
#     for j in x:
#         if j in rule:
#             clap += 1
# print(clap)



# ### 4번 문제 ###
import numpy as np

def find_number(array, i, j, k):
    ### coding here ####
    n_array = array[i-1:j]
    n_array = sorted(n_array)
    answer = n_array[k-1]
    return answer

a = np.array([1, 5, 2, 6, 3, 7, 4])
print(find_number(a, 2, 5, 3))



# ### 5번 문제 ###

#### coding here ####
# from PIL import Image

# f = open('list.txt', 'r')

# lines = f.readlines()
# directory_name = 'images/'

# for line in lines:
#     file_name = line.strip()
#     num = file_name.replace('dog','')
#     num = num.replace('.jpg','')

#     if int(num) % 2 != 0:
#         img = Image.open(file_name)
#         img = img.rotate(30, expand = True)
#         img.save('rot30_'+file_name)

#     else:
#         img = Image.open(file_name)
#         size_list = list(img.size)
#         x1 = size_list[0]*0.1
#         y1 = size_list[1]*0.2
#         x2 = size_list[0]*0.3
#         y2 = size_list[1]*0.5
#         img = img.crop((x1, y1, x2, y2))
#         img.save('crop_'+file_name)

# f.close()