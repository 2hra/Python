### 10주차) 22.11.09 Numpy & Pandas

### 1교시-1) 모듈
### 모듈 호출 방법
## 1) import 모듈
import myfunction1109 ## 동일 폴더 내의 함수 전용 파일
myfunction1109.say_bye()


## 2) from 모듈 import 함수||변수
from myfunction1109 import say_hello
say_hello()

from myfunction1109 import a ## 변수
b = a + 3 ## 함수 파일에 a = 3으로 정의되어있음.
print(b)

from myfunction1109 import say_bye, say_hello


## 3) 위에 as 약자만 추가
import myfunction1109 as mf
mf.say_bye()

from myfunction1109 import say_hello as sh
sh()


### 파이썬 내부 모듈 활용
import math as m
a = m.cos(m.pi/3)
print(a)
b = m.pow(2,3) ## 2의 3승
print(b)

import random as rand
x = rand.randrange(3,9) ## 이상, 이하 중 랜덤
print(x)



### 1교시-2) 패키지 == 여러 모듈 존재하는 폴더
import mine.myfunction as mf ## import 패키지.모듈

## 다른 모듈 함수 중복 시 == import 패키지 \n 패키지.모듈.함수()

## __init__.py >> 패키지 내부에 init 파일 있다면 init 내부 전체 실행
import mine.myfunction
myfunction1109.say_bye()



### 1교시-3) 외부 라이브러리
## https://pypi.org/
## 위 사이트에서 서치 후 설치, 호출.



### 1교시-4) numpy
## 1차원 축(행): axis 0 > vector
## 2차원 축(열): axis 1 > matrix(행렬)
## 3차원 축(채널): axis 2 > tensor(3차원 이상)

import numpy as np

## np.array([ , , , ...]) 배열 선언
y = np.array([1,2,3]) 
print(y)
print(y.size) ## 배열 요소 개수
print(y.dtype) ## 자료형
print(y[2])

## type() class 반환
print(type(y))

## 리스트를 넘파이 배열로 변경
x = [4,5,6]
z = np.array(x)
print(z)
print(type(z))

## 배열 내부 자료형 지정
a = np.array([[1,2,3.5],[4,5,6.5]], dtype= int)
b = np.array([[1,2,3.5],[4,5,6.5]], dtype= float)
print(a)
print(b)



### 2교시-1) numpy vs list >> numpy는 연산 가능.
a = [1,2,3,4]
b = [5,6,7,8]
print(a+b)

c = np.array([11,12,13,14])
d = np.array([15,16,17,18])
print(c+d)
print(c-d)
print(c*2)
print(d/2)
print(c == 12)


## 1차원 배열 인덱스
a = np.array([1,3,5,7,9])
print(a[2])
print(len(a))
print(a[-4])



### 2교시-2) numpy 2차원 배열
## np.array([[,,],[,,]])
x = np.array([[1,2,3],[4,5,6]])
print(len(x)) ## 내부 배열 개수
print(len(x[1])) ## 인덱스[1] == 2번째 배열 요소 개수
print(x.shape) ## 행, 열


## 2차원 배열 인덱스 >> [n번째 배열, 배열내 요소] & 이상:미만
print(x[1,2]) ## x[1]인 [4,5,6]의 인덱스[2]
print(x[0,:]) 
print(x[:2,0])


### 배열 값 초기화 방법
## np.zeros() & np.ones()
a = np.ones(5)
print(a)

b = np.zeros((5,5)) ## 2차원 배열은 소괄호 두 번
print(b)

## np.random.randint(이상, 미만, 배열 형태) 랜덤 초기값
a = np.random.randint(0,10,(3,4))
print(a)

## np.random.rand() 랜덤 소수
b = np.random.rand()
print(b)

## np.random.normal(평균, 표준편차, 배열 형태)
c = np.random.normal(0, 1, (3,3))
print(c)


## 변수.reshape(,) 배열 구조 변경
a = np.array([1,2,3,4,5,6,7,8])
b = a.reshape(2,4)
print(a)
print(b)
c = b.reshape(-1,) ## 무조건 한 줄로
print(c)


## 변수.flatten() 한 줄로 변경
d = b.flatten()
print(d)


## np.concatenate([배열,배열]) 한 줄로 이어 붙임
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.concatenate([a,b])
print(c)


## np.vstack((배열,배열)), np.hstack((배열,배열))
d = np.vstack((a,b))
print(d)
e = np.hstack((a,b))
print(e)


## 여러 종류 함수
x = np.array([1, 2, 3, 4])
print(np.sum(x)) 
print(x.sum()) ## 결과 상동 
print(x.min())
print(x.max())
print(x.argmin()) ## 최소값 위치. y = x^2+1 == 1이지만 0으로 나옴.
print(x.argmax())
print(x.mean())
print(np.var(x))
print(np.std(x))



### 2교시-3) pandas series
import pandas as pd

a = pd.Series([1,2,3,4, np.nan])
print(a) ## 인덱스 - 값, 자료형 출력


## Series 생성 방법 1) 딕셔너리
from pandas import Series as sr
dict_data = {'이':95, '하':82, '박':79, '김':91}
sr_data = sr(dict_data)
print(type(sr_data)) ## 클래스 확인
print(sr_data)


## Series 생성 방법 2) 리스트
list_name = ['이','하','박','김']
list_score = [95,82,79,91]
new_sr = sr(index = list_name, data = list_score)
print(type(new_sr))
print(new_sr)


## Series 데이터 접근
list_name = ['이','하','박','김']
list_score = [95,82,79,91]
new_sr = sr(index = list_name, data = list_score)
print(new_sr['하']) ## 대괄호 1개: 값만 출력
print(new_sr[2])
print(new_sr['이':'박']) ## 이상:이하
print(new_sr[1:4])
print(new_sr[['김']]) ## 대괄호 2개: 키-값 동시 출력
print(new_sr[[0]])


## 두 개의 시리즈 공통 데이터만 산술 연산 가능
list_1 = ['lee', 'kim', 'baek', 'choi']
data_1 = [100, 95, 90, 85]
list_2 = ['lee', 'lim', 'baek', 'oh']
data_2 = [100, 80, 60, 40]

sr_1 = sr(data = data_1, index = list_1)
sr_2 = sr(data = data_2, index = list_2)

print(sr_1 + sr_2)


## 시리즈 변수.unique() 중복값 제외 후 반환
data = ['apple', 'bear', 'chic', 'apple', 'dear', 'bear']
sr_data = sr(data)
print(sr_data.unique())


## 시리즈 변수.values_counts() 종류별 개수, 자료형 반환
print(sr_data.value_counts())


## 시리즈 변수.isin([]) 일치하는 인덱스에 True
print(sr_data.isin(['apple']))



### 2교시-4) pandas dataframe

## 생성 방법 1) 딕셔너리
from pandas import DataFrame
dc_data = {'나이':[24,20,16], '성별':['F','F','M'], '학교':['A','B','C']}
new_df = DataFrame(data = dc_data, index = ['김','이','박'])
print(new_df)
print(type(new_df))


## 생성 방법 2) 리스트
new_df2 = DataFrame([[24,'F','A'],[20,'F','B'],[16,'M','C']], index = ['김','이','박'], columns = ['나이','성별','학교'])
print(type(new_df2))
print(new_df2)


## df 변수명.index(), df 변수명.columns() 요소 바꾸기
new_df2.index = ['학생1','학생2','학생3']
new_df2.columns = ['Age', 'Gender', 'School']
print(new_df2)
print(new_df2.index)
print(new_df2.columns)


## df 변수명.renames(index = , columns = , inplace = True) 요소 바꾸기
new_df2.rename(columns={'나이':'age2','성별':'Gender2','학교':'School2'}, inplace= True)
print(new_df2)
print(new_df2.index)
print(new_df2.columns)


## df 변수명.drop(요소, inplace = True) 행 삭제
copy_df = new_df2
copy_df.drop('학생1', inplace= True)
print(copy_df)


## df 변수명.drop(요소, axis = 1, inplace = True) 행 삭제
copy_df1 = new_df2
copy_df1.drop('Age', axis = 1, inplace = True)
print(copy_df1)


## df 변수명.loc['index']
new_data= {'이름':['김','이','박'],'나이':[20,21,22]}
final_df = DataFrame(new_data, index = ['학생1','학생2','학생3'])
label1 = final_df.loc['학생1'] ## 키-값, 인덱스, 자료형 반환
print(label1)


## df 변수명.iloc[숫자]
label2 = final_df.iloc[1]
print(label2)



### 11주차) 22.11.16 데이터 시각화
### 1교시-1) matplotlib pyplot
import matplotlib
print(matplotlib.__version__)

from matplotlib import pyplot as plt

matplotlib.rcParams['font.family']='Malgun Gothic' ## 폰트 추가
matplotlib.rcParams['font.size']=12 ## 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False ## 마이너스 표시 오류


### 1교시-2) plt.plot() 그래프 그릴 값, 선 스타일, 범례 / plt.show()
x = [-1,2,3]
y = [-4,5,6]
plt.plot(x, y, 'bx-', label='11.28 practice')
## x, y에 변수명 아닌 직접 값 입력도 가능.
## 선 매개변수: linewidth, linestyle(ls), color(c)
## 점 매개변수: marker, markersize, markeredgecolor, markerfacecolor
## 색, 점, 선 함축 입력 가능. (ex. 'bx-', 'ro:')
## label = 해당 그래프 선의 범례. 다중 그래프는 그래프별 레전드 입력 가능.


### 1교시-3) plt.legend() 범례 위치 등 옵션
plt.legend(loc = 4)
plt.legend(loc = (0.5,0.5))


### 1교시-4) plt.title(), plt.xlabel(), plt.ylabel()
plt.title('종강은 12/16')
plt.xlabel('x축', color = 'red', loc = 'right')
plt.ylabel('y축', color = 'skyblue', loc = 'top')


### 1교시-5) plt.xticks(), plt.yticks() 축 범위 지정
x = [-1,2,10]
y = [-5,7,15]
plt.plot(x,y)
plt.xticks([-5,0,10,15])
plt.yticks([-6,1,6,16])


### 1교시-6) plt.fiqure(figsize = , dpi = ) 크기, 해상도 조절
plt.figure(figsize=(6,4), dpi = 50)
## 위 내용 설정 후 아래에 pyplot 입력, 출력(plt.show())


### 1교시-7) plt.savefig('파일명.jpg(png)', dpi = )
plt.figure(figsize=(6,4), dpi = 50)
x = [-1,2,10]
y = [-5,7,15]
plt.plot(x,y,c='skyblue')
plt.title('종강하고 싶다_1128')
plt.xlabel('x축 이름', loc='left', c='orange')
plt.ylabel('y축 이름', loc = 'bottom',c='green')
plt.xticks([-5,0,10,15])
plt.yticks([-6,1,6,16])
plt.savefig('20211648_1128plt.png', dpi = 100)


### 1교시-8) plt.text(), enumerate(x || y) 텍스트 삽입
for idx, txt in enumerate(y):
    plt.text(x[idx], y[idx] + 0.3, txt, ha = 'center', color= 'green')
    ## plt.tex(x좌표, y좌표 + 텍스트 상하 위치, y 값[i], ha=좌우 위치)

    

### 2교시-1) Pillow
from PIL import Image, ImageFilter, ImageEnhance, ImageOps


### 2교시-2) Image.open('파일명')
## 이미지 변수명.size, 이미지 변수명.format
## 이미지 변수명.show(), 이미지 변수명.save()
img = Image.open('dog1.jpg')
print(img.size) ## 크기
print(img.format) ## 파일 유형
img.save('dog1_1128.jpg')
# img.show()


### 2교시-3) 이미지 변수명.split() 삼원색 분리
print(img.mode) ## RGB 형식
r, g, b = img.split()
# r.show()
# g.show()
# b.show()


### 2교시-4) 이미지 변수명.transpose(Image.FLIP_LEFT_RIGHT || FLIP_TOP_BOTTOM)
## 이미지 좌우반전 또는 상하반전
imglr = img.transpose(Image.FLIP_LEFT_RIGHT)
imgtb = img.transpose(Image.FLIP_TOP_BOTTOM)
# imglr.show()
# imgtb.show()


### 2교시-5) 이미지 변수명.rotate(각도, expand=True) 회전
## expand = 회전 후 모서리 잘리지 않게 화면 확대
imgrt = img.rotate(30, expand = True)
# imgrt.show()


### 2교시-6) 이미지 변수명.crop((x1,y1,x2,y2)) 좌표 지정해서 크롭
imgcrop = img.crop((192,128,1000,1200))
# imgcrop.show()


### 2교시-7) 이미지 변수명.pates(병합할 이미지, (x1,y1,x2,y2)) 이미지 병합
img1 = Image.open('dog2.jpg') ## (630,420)
img2 = Image.open('dog3.jpg')
img2_r = img2.resize([63,42])

img1.paste(img2_r, (0,0,63,42)) ## 원 이미지 위에 병합.
# img1.show()


### 2교시-8) ImageEnhance.Brightness(이미지 변수명).enhance(1.0~5.0)
img3 = Image.open('dog4.jpg')
imgenhan = ImageEnhance.Brightness(img3).enhance(1.10)
# img3.show()
# imgenhan.show()


### 2교시-9) imgenhan = ImageEnhance.Brightness(img3).enhance(0.0~1.0) 어둡게


### 2교시-10)  ImageOps.grayscale(i이미지 변수명) 흑백으로
img4 = ImageOps.grayscale(img3)
# img4.show()


### 2교시-11) 이미지 변수명.filter(ImageFilter.EMBOSS) 엠보싱
img5 = img3.filter(ImageFilter.EMBOSS)
# img5.show()


### 2교시-12) 이미지 변수명.filter(ImageFilter.CONTOUR) 스케치 효과
img6 = img3.filter(ImageFilter.CONTOUR)
# img6.show()


### 2교시-13) 이미지 변수명.filter(ImageFilter.FIND_EDGES) 경계선 추출
img7 = img3.filter(ImageFilter.FIND_EDGES)
# img7.show()


### 2교시-14) 이미지 변수명.filter(ImageFilter.BLUR) 흐리게
img8 = img3.filter(ImageFilter.BLUR)
# img8.show()



# ### 3교시는 설명마다 실행 후 주석 처리
# ### 3교시-1) OpenCV
# import cv2
# print(cv2.__version__)


# ### 3교시-2) cv2.imread('파일명') 이미지 입력, cv2.resize(변수명, dsize = (,))
# image = cv2.imread('dog5.jpg', cv2.IMREAD_COLOR)
# src = cv2.resize(image, dsize=(640,480))

# ## cv2.imread('창 이름', 변수명) 이미지 출력
# cv2.imshow('image_dog5', image)
# cv2.imshow('image_src', src)
# cv2.waitKey(0)
# cv2.destroyAllWindows


# ### 3교시-3) cv2.VideoCapture(0) 카메라 출력
# capture = cv2.VideoCapture(0) ## 0 == 카메라
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) ## 너비
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) ## 높이

# while cv2.waitKey(33) < 0: ## 1초에 33장의 이미지. 동영상처럼.
#     ret, frame = capture.read()
#     cv2.imshow('VideoFrame', frame)

# capture.release() ## == f.close()
# cv2.destroyAllWindows()


# ### 3교시-4) cv2.flip(변수명, -1~1) 대칭
# src = cv2.imread('dog6.jpg', cv2.IMREAD_COLOR)
# src = cv2.resize(src, dsize=(640,480))
# dst = cv2.flip(src, 0)
# dst1 = cv2.flip(src, 1)
# dst_1 = cv2.flip(src, -1)

# cv2.imshow('src', src)
# cv2.imshow('dst', dst) ## 상하 반전
# cv2.imshow('dst1', dst1) ## 좌우 반전
# cv2.imshow('dst_1', dst_1) ## 상하좌우 반전
# cv2.waitKey()
# cv2.destroyAllWindows()


# ### 3교시-4-1) height, width, channel = src.shape / 대칭
# src = cv2.imread('dog6.jpg', cv2.IMREAD_COLOR)
# src = cv2.resize(src, dsize=(640,480))

# height, width, channel = src.shape

# ## 회전변환행렬 계산
# matrix = cv2.getRotationMatrix2D((width/2, height/2), 30, 1)
# ## matrix = cv2.getRotationMatrix2D(center=중심점, angle=각도, scale=비율)

# ## 아핀 변환 함수
# dst = cv2.warpAffine(src, matrix, (width, height))
# ## dst = cv2.warpAffine(변수명, M=회전변환행렬, dsize)

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()


# ### 3교시-5) 변수명[높이, 너비].copy() 자르기
# src = cv2.imread('dog7.jpg', cv2.IMREAD_COLOR)
# srccopy = src[100:600, 200:700].copy()

# cv2.imshow('src_copy', srccopy)
# cv2.waitKey()
# cv2.destroyAllWindows()


# ### 3교시-6) 색상 공간 변환 패스


# ### 3교시-7) cv2.blur(변수명, (5,5))
# ## || cv2.GaussianBlur(src, (5,5), 0) 흐림 효과
# src = cv2.imread('dog7.jpg', cv2.IMREAD_COLOR)
# srcblur1 = cv2.blur(src, (5,5))
# srcblur2 = cv2.GaussianBlur(src, (5,5), 0)

# cv2.imshow('src_blur1', srcblur1)
# cv2.imshow('src_blur2', srcblur2)
# cv2.waitKey()
# cv2.destroyAllWindows()


# ### 3교시-8) cv2.cvtColor(변수명, cv2.COLOR_BG2GRAY) 가장자리 검출
# src = cv2.imread('dog7.jpg', cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(src, cv2.COLOR_BG2GRAY)

# sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
# laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize = 3)
# canny = cv2.Canny(src, 100, 255)

# cv2.imshow('sobel', sobel)
# cv2.imshow('laplacian', laplacian)
# cv2.imshow('canny', canny)
# cv2.waitKey()
# cv2.destroyAllWindows()


# ### 3교시-9) 채널 분리 & 병합
# src = cv2.imread('dog7.jpg', cv2.IMREAD_COLOR)
# b, g, r = cv2.split(src) ## 분리
# inverse = cv2.merge((r,g,b)) ## 병합

# cv2.imshow('r', r)
# cv2.imshow('g', g)
# cv2.imshow('b', b)
# cv2.imshow('inverse', inverse)
# cv2.waitKey()
# cv2.destroyAllWindows()



### 13~14주차) 이론 (12주차 특강)