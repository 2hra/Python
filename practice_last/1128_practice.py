# ### 10주차 numpy 실습
# import numpy as np


# ### 10주차-1)
# a = [2,5,1,17,21]

# ## coding here
# b = np.array(a)
# result = b+1

# print(result)


# ### 10주차-2)
# a = np.array([1,3,5,7,8,11])

# ## coding here
# b = a.reshape(2,3)

# print(b)


# ### 10주차-4)
# res1 = np.add(10,30)
# res2 = np.subtract(40,93)
# res3 = np.multiply(55,71)
# res4 = np.divide(250,25)

# print(res1, res2, res3, res4)


# ### 10주차-5)
# a = np.random.random((10, 10))

# min_a = a.min()
# max_a = a.max()

# print(a)
# print(min_a, max_a)



# ### 11주차 Pillow, OpenCV 실습

# ### 11주차-1) Pillow
# from PIL import Image

# ### 11주차-1-1)
# f = open('list.txt', 'r')
# lines = f.readlines()
# directory_name = 'images/'

# for line in lines:
#     file_name = directory_name + line.strip()
#     img = Image.open(file_name)
#     img_rot = img.rotate(45, expand = True)
#     new_name = file_name.replace('dog','rot_dog')
#     img_rot.save(new_name)

# f.close()


# # # file_name = directory_name +line.strip()
# # # img = Image.open(file_name)
# # # rotate_image = img.rotate(45, expand=True)
# # # new_name = file_name.replace('dog', 'rot_dog')
# # # rotate_image.save(new_name)


# ### 11주차-1-2)
# f = open('list.txt', 'r')
# lines = f.readlines()
# directory_name = 'images/'
# fw = open('summary_cv2_1128.txt', 'w')

# for line in lines:
#     file_name = directory_name + line.strip()
#     img1 = Image.open(file_name)
#     size_list = img1.size
#     fw.write(line.strip() + ' 이미지의 가로는 ' + str(size_list[0]) + ', 세로는 ' + str(size_list[1]) + '입니다.'+'\n')

# fw.close()
# f.close()


# # # from PIL import Image
# # # f = open('list.txt','r')
# # # lines = f.readlines()
# # # directory_name = 'images/'

# # # fw = open('summary.txt','w')
# # # for line in lines:
# # #     filename = directory_name + line.strip()
# # #     img = Image.open(filename)
# # #     # print(img.size)
# # #     result = line.strip() + ' 이미지의 가로는 ' + str(img.size[0]) + ', 세로는 ' + str(img.size[1]) + '입니다.'
# # #     # print(result)
# # #     fw.write(result + '\n')

# # # fw.close()
# # # f.close()


# ### 11주차-2) OpenCV
# import cv2

# ### 11주차-2-1)
# f = open('list.txt', 'r')
# lines = f.readlines()
# directory_name = 'images/'

# for i in lines:
#     file_name = directory_name + i.strip()
#     src = cv2.imread(file_name)

#     height, width, channel = src.shape
#     matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
#     src_rot = cv2.warpAffine(src, matrix, (width, height))

#     new_name = file_name.replace('dog', 'cv2_rot_dog')
#     cv2.imwrite(new_name, src_rot)

# f.close()


# # # for line in lines:
# # #     filename = directory_name + line.strip()
# # #     # print(filename)
# # #     img = cv2.imread(filename)

# # #     height, width, channel = img.shape
# # #     matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1) ## 이 줄, 아랫줄을 알아야 함.
# # #     dst = cv2.warpAffine(img, matrix, (width, height))

# # #     new_name = filename.replace('dog','rot_dog')
# # #     cv2.imwrite(new_name, dst) ## 저장하는 방법. cv2.imwrite(내용)

# # # f.close()


# ### 11주차-2-2)
# f = open('list.txt', 'r')
# lines = f.readlines()
# directory_name = 'images/'
# fw = open('summary_cv2_1128.txt', 'w')

# for i in lines:
#     file_name = directory_name + i.strip()
#     src = cv2.imread(file_name)
#     height, width, channel = src.shape
#     result = i.strip() + ' 이미지의 가로는 ' + str(width) + ', 세로는 ' + str(height) + '입니다.'
#     fw.write(result + '\n')

# fw.close()
# f.close()


# # # for line in lines:
# # #     filename = directory_name + line.strip()
# # #     img = cv2.imread(filename)
# # #     height, width, channel = img.shape
# # #     result = line.strip() + ' 이미지의 가로는 ' + str(width) + ', 세로는 ' + str(height) + '입니다.'
# # #     fw.write(result + '\n')