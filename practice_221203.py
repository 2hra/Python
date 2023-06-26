### 10주차 예제

## 예제 1)
a = [2,5,1,17,21]

import numpy as np

b = np.array(a)
result = b+1

print(result)


## 예제 2)
a = np.array([1,3,5,7,8,11])
b = a.reshape(2,3)

print(b)


## 예제 3)
res1 = np.add(10,30)
res2 = np.subtract(40,93)
res3 = np.multiply(55,71)
res4 = np.divide(250,25)

print(res1, res2, res3, res4)


## 예제 4)
a = np.random.random((10,10))
min_a = a.min()
max_a = a.max()
print(a)
print(min_a, max_a)



### 11주차

## 예시 1, PIL
from PIL import Image
f = open('list.txt', 'r')

lines = f.readlines()
directory_name = 'practice_last/images/'

for line in lines:
    filename = directory_name + line.strip()
    img = Image.open(filename)
    new_img = img.rotate(45, expand= True)
    new_name = filename.replace('dog', 'rot_1203_dog')
    new_img.save(new_name)

f.close()


## 예시 2)
which_name = 'practice_last/images/'

f = open('list.txt', 'r')
lines = f.readlines()

nf = open('practice_last/1203_summary.txt', 'w')

for line in lines:
    filename = which_name + line.strip()
    img = Image.open(filename)
    img_size = img.size
    nf.write(line.strip() + ' 이미지의 가로는 ' + str(img_size[0]) + ', 세로는 '+ str(img_size[1]) + '입니다.' + '\n')

nf.close()
f.close()


## 예시 3) OpenCV
import cv2

f = open('practice_last/list.txt', 'r')

lines = f.readlines()

which_name = 'practice_last/images/'

for i in lines:
    filename = which_name + i.strip()
    img = cv2.imread(filename)

    height, width, channel = img.shape
    matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
    n_img = cv2.warpAffine(img, matrix, (width, height))

    new_name = filename.replace('dog', 'cv2_rot_1203_dog')
    cv2.imwrite(new_name, n_img)

f.close()


## 예시 4)
f = open('practice_last/list.txt','r')

which_file = 'practice_last/images/'

names = f.readlines()

nf = open('practice_last/1203_cv2_summary.txt','w')

for i in names:
    filename = which_file + i.strip()
    img = cv2.imread(filename)
    height, width, channel = img.shape
    result = i.strip() + ' 이미지의 가로는 ' + str(img.shape[1]) + ', 세로는 ' + str(img.shape[0]) +'입니다.'
    nf.write(result + '\n')

f.close()
nf.close()



##### 10주차 타이핑 #####

### numpy

from mine import myfunction
myfunction.say_bye() ## __init__ 포함

from myfunction1109 import say_bye
say_bye

import numpy as np

a = [ , , ]
a_array = np.array(a)

np_array = np.array([ , , , ])

print(np_array[인덱싱])
print(np_array.size)
print(np_array.dtype)
print(np_array.shape)

a_arr = np.array([1,2,3])
b_arr = np.array([4,5,6])
print(a_arr + b_arr, a_arr * b_arr, ... ) ## 연산 가능

ab_arr = np.array([[1,2,3], [4,5,6]])
print(len(ab_arr)) ## 배열 개수
print(len(ab_arr[배열 인덱스])) ## 지정 배열 요소 개수
print(ab_arr[배열 순서, 요소 순서]) ## 이상:미만

z = np.zeros(개수)
o = np.ones(개수)
o = np.ones((r, c), dtype = 자료형)

rand = np.random.randint(이상, 미만, (r, c))
rand_sosu = np.random.rand()
rand_normal = np.random.normal(평균, 표준편차, (r, c))

x_arr = np.array([[1,2,3], [4,5,6]])
x_arr.reshape = (r, c)
x_arr.reshape = (-1, ) ## 한 줄 열거
x_arr.flatten() ## 상동

a_arr = np.array([1,2,3])
b_arr = np.array([4,5,6])
np.vstack((a_arr, b_arr)) ## 세로 붙이기
np.hstack((a_arr, b_arr)) ## 가로 붙이기

x = np.array([1,2,3,4,5,6,7,8])
print(np.sum(x))
print(x.sum())
print(x.min(), x.max())
print(x.argmin(), x.argmax()) ## 최소값 위치. y = x^2+1 == 1이지만 0으로 나옴.
print(x.mean(), np.var(x), np.std(x))



### pandas series

import pandas as pd

a = pd.Series([1,2,3,4])
print(a) ## 키 - 값 \n 자료형

from pandas import Series

dict = {'lee':100, 'kim':95, 'choi':90}
pd_dict = Series(dict)
print(type(pd_dict))

index_pd = ['lee', 'kim', 'choi']
data_pd = [100, 95, 90]
list_pd = Series(index = index_pd, data = data_pd)

print(list_pd['lee'], list_pd[0]) ## 값만, 이상:이하
print(list_pd[['lee']], list_pd[[0]]) ## 키 - 값

a_dict = {'lee':100, 'kim':95, 'choi':90}
a_pd = Series(a_dict)
b_dict = {'lee':100, 'kang':80, 'baek':60}
b_pd = Series(b_dict)
print(a_pd + b_pd) ## 공통 키만 계산, 나머지 NaN

data = ['apple', 'bear', 'chic', 'apple', 'dear', 'bear']
sr_data = Series(data)
print(sr_data.unique()) ## 중복값 삭제
print(sr_data.value_counts()) ## == summary
print(sr_data.inin(['값'])) ## 일치 인덱스에 True



### pandas dataframe

from pandas import DataFrame

dict_df = {'나이':[24,20,16], '이름':['lee','kim','choi'], '등급':['A','B','C']}
new_df = DataFrame(data = dict_df, index = ['1st','2nd','3rd'])

list_df = DataFrame([[24,'lee','A'],[20,'kim','B'],[16,'choi','C']], index = ['1st','2nd','3rd'], columns=['나이','이름','등급'])

## 제목 바꾸기
new_df.index = ['1','2','3']
new_df.columns = ['age', 'name', 'grade']
new_df.rename(columns={'나이':'Age', '이름':'Name', '등급':'Grade'}, inplace=True)

new_df.drop('lst', inplace=True)
new_df.drop('나이', axis=1, inplace=True)

print(new_df.loc['1st']) ## 키 - 값, 인덱스, 자료형
print(new_df.iloc[0]) ## 상동



##### 11주차 타이핑 #####

### matplotlib pyplot

import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=12
matplotlib.rcParams['axex.unicode_minus']=False ## 마이너스 오류 수정

x = [-1, 2, 3]
y = [-4, 5, 6]
plt.plot(x, y, label = '선의 범례')
## 선 매개변수: linewidth, linestyle, color
## 점 매개변수: marker, markersize, markeredgecolor, markerfacecolor
## bx-, ro:

plt.legend(loc=범례 위치)

plt.title('그래프 제목')
plt.xlabel('x축 제목')
plt.ylabel('y축 제목')

plt.xticks([ , , ]) ## 축 구간 설정
plt.yticks([ , , ])

plt.figure(figsize = (가로, 세로), dpi = 해상도)

plt.savefig('파일명.확장자', dpi = 해상도)

for idx, txt in enumerate(y):
    plt.text(x[idx], y[idx], + 텍스트 상하 위치, txt, ha = 좌우 위치, color = )



### Pillow PIL

from PIL import Image, ImageFilter, ImageEnhance, ImageOps

img = Image.open('파일명.확장자')
img.size
img.format ## 확장자
img.save('파일명.확장자')
img.show()

img.mode ## RGB 형식 확인
r, g, b = img.split() ## 분리

img.transpose(Image.FLIP_LEFT_RIGHT)
img.transpose(Image.FLIP_TOP_BOTTOM)

img.rotate(45, expand = True)

img.resize([가로, 세로])
img.crop((x1,y1,x2,y2좌표))

img.paste(병합할 이미지, (붙이기 시작할 x1,y1,x2,y2좌표))

img_밝게 = ImageEnhance.Brightness(img).enhance(1.0~5.0)
img_어둡 = ImageEnhance.Brightness(img).enhance(0.0~1.0)

img_흑백 = ImageOps.grayscale(img)
img_엠보싱 = img.filter(ImageFilter.EMBOSS)
img_스케치 = img.filter(ImageFilter.CONTOUR)
img_경계선 = img.filter(ImageFilter.FIND_EDGES)
img_흐리게 = img.filter(ImageFilter.BLUR)



### OpenCV cv2

import cv2

img = cv2.imread('파일명.확장자', cv2.IMREAD_COLOR)
img_resize = cv2.resize(img, dsize = (가로, 세로))

cv2.imshow('창 이름', img)
cv2.waitKey(0)
cv2.destroyAllWindows

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 가로)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 세로)
while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow('창 이름'.frame)
capture.release()
cv2.destroyAllWindows()

cv2.flip(img, 0) ## 상하 반전
cv2.flip(img, 1) ## 좌우 반전
cv2.flip(img, -1) ## 상하좌우 반전

height, width, channel = img.shape
matrix = cv2.getRotationMatrix2D((height/2, width/2), 각도, 1) ## (중심점, 각도, 비율)
img_rot = cv2.warpAffine(img, matrix, (가로, 세로))

img_crop = img[높이1:높이2, 너비1:너비2].copy()

img_blur1 = cv2.blur(img, (5,5))
img_blur2 = cv2.GaussianBlur(img, (5,5), 0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BG2GRAY)
sobel = cv2.Sobel(img_gray, cv2.CV_8U, 1, 0, 3)
laplican = cv2.Laplacian(img_gray, cv2.CV_8U, ksize = 3)
canny = cv2.Canny(img, 100, 255)

r, g, b = cv2.split(img)
inverse = cv2.merge((r,g,b))