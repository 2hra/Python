##### 2022-2학기 데이터마이닝이해와실습 (데사B0002 3차 과제) #####
##### 학번 : 
##### 이름 :
##### 제출할 때 파일명을 학번.py로 변경해서 제출하시기 바랍니다.


### 1번 문제 ###
# answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

# A = ['hello', 62, 'umbrella', 145]
# B = ['September', 512.3, 'coffe', 39, 'keyboard','notebook', 0.5, 'f12']
# C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

# ### coding here ####
# return_list = input('리스트를 입력하세요 : ').upper()

# def ox_check(list, answer):
#     for i in list:
#         if i in answer:
#             print('O', end = '')
#         else:
#             print('X', end = '')
        
# if return_list == 'A':
#     return_list = A
#     ox_check(return_list, answer)
# elif return_list == 'B':
#     return_list = B
#     ox_check(return_list, answer)
# elif return_list == 'C':
#     return_list = C
#     ox_check(return_list, answer)
# else:
#     print('리스트에 없습니다.')



# ### 2번 문제 ###
# def find_capitalcity(capital, country):
#     #### coding here ####
#     for i in capital.keys():
#         if country == i:
#             return capital[i]

# capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이","덴마크":"코펜하겐"}

# print(find_capitalcity(capital, "대한민국"))
# print(find_capitalcity(capital, "덴마크"))



# ### 3번 문제 ###
# number = int(input('숫자를 입력하세요 : '))
# clap = 0
# rule = ['3','6','9']
# for i in range(1, number+1):
#     i = str(i)
#     for j in i:
#         if j in rule:
#             clap += 1
# print(clap)



# ### 4번 문제 ###
# import numpy as np
 
# def find_number(array, i, j, k):
#     #### coding here ####
#     n_arr = array[i-1:j]
#     n_arr = sorted(n_arr)
#     return n_arr[k-1]

# a = np.array([1, 5, 2, 6, 3, 7, 4])
# print(find_number(a, 2, 5, 3))



# ### 5번 문제 ###
# #### coding here ####
from PIL import Image

f = open('list.txt', 'r')

which_file = 'images/'

for i in range(1,10,2):
    filename = which_file + 'dog' + str(i) + '.jpg'
    img = Image.open(filename)
    img_rot = img.rotate(30, expand=True)
    new_name = filename.replace('dog','1204_rot_dog')
    img_rot.save(new_name)
    
for i in range(2,11,2):
    filename = which_file + 'dog' + str(i) + '.jpg'
    img = Image.open(filename)
    size_list = img.size
    img_crop = img.crop((size_list[0]*0.1, size_list[1]*0.2, size_list[0]*0.3, size_list[1]*0.5))
    new_name = filename.replace('dog', '1204_crop_dog')
    img_crop.save(new_name)

f.close()