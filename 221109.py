# ## 다음 주까지 파이썬 실습, 그 다음 주는 특강, 남은 2주는 이론
# ## 기말은 대면으로. 수기로 볼 예정.

# ## 개발자, ai 쪽에서 [선형대수학, 자료구조] 학점을 본다. A+ 되도록...


# ### 1교시) 모듈
# ## 변수, 함수, 클래스를 모아둔 것이 모듈.
# ## 해당 모듈에서 불러오는 방법에 대해 배운다.

# ## 호출 방법 1) import 모듈이름
# import myfunction1109
# myfunction1109.say_hello()

# ## 호출 방법 2) from 모듈이름 import 함수, 변수명
# from myfunction1109 import say_bye
# say_bye()

# ## 호출 방법 3) import 모듈이름 as 바꿀이름(약자)
# import myfunction1109 as mf
# mf.say_bye()

# ## 호출 방법 3-1) from 모듈이름 import 함수, 변수명 as 바꿀이름
# from myfunction1109 import say_bye as sb
# sb()


# import numpy as np ## 암묵적으로 np로 많이 쓴다.

# ## 변수도 지정 가능함. 다시 해 보기.
# import myfunction1109
# b = myfunction1109.a + 3
# print(b)

# # from myfunction import say_bye
# # say_bye()
# # def say_bye(): 
# ## 모듈과 작성 중인 파일의 함수명이 동일하면 모듈 호출 함수가 사라짐.
# ## 함수 이름은 다르게 선언하도록 주의.


# ## 파이썬 제공 모듈 예시 1) math(cos, pi, pow 등)
# import math as m
# a = m.cos(m.pi/3)
# print(a)
# b = m.pow(2,3) ## 지수
# print(b)

# ## 파이썬 제공 모듈 예시 2) random(randrange, choice, randint 등)
# import random
# x = random.randrange(3,9) ## 3~9 중 랜덤 수
# print(x)


# from myfunction1109 import say_bye, say_hello ## 여러 함수 기재도 가능


# ### 1교시) 패키지 == 모듈 여러개를 합친 폴더
# import mine.myfunction as mf ## import 패키지.모듈

# ## 패키지 안의 각기 다른 모듈의 함수가 중복된다면?
# ## import 패키지
# ## 패키지.모듈.함수() 로 사용

# ## __init__.py
# import mine.myfunction
# mine.myfunction.say_hello()
# ## 출력 결과
# # 2022 datascience >> __init__.py >> 호출될 때마다 해당 파일 전체가 무조건 실행됨.
# # hello

# from mine.myfunction import say_hello ## 해당 함수가 많이 쓰일 때 호출
# say_hello()


# ### 1교시) 외부 라이브러리
# ## https://pypi.org/
# ## 해당 사이트에서 외부 라이브러리 서치 후 설치해 호출함.
# import pygame


# ### 1교시) numpy
# ## 2차원 데이터(매트릭스, 데이터프레임 등) 처리에 막강한 라이브러리.
# # 1차원 축 (행) : axis 0 → vector
# # 2차원 축 (열) : axis 1 → matrix (행렬)
# # 3차원 축 (채널) : axis 2 → tensor (3차원 이상)

# import numpy as np

# y = np.array([1,2,3]) ## 배열 선언
# print(y) ## 넘파이 배열 출력. 쉼표 없음. 단순 계산 가능.
# print(y.size) ## 넘파이 배열 요소 갯수 출력.
# print(y.dtype)
# print(y[2])

# x = [1,2,3] ## 넘파이와 단순 리스트의 차이.
# print(x) ## 리스트 출력.
 

# ## type()
# print(type(y)) ## <class 'numpy.ndarray'>
# print(type(x)) ## <class 'list'>


# ## 리스트를 넘파이 배열로 변경
# z = np.array(x) ## 해당 줄부터 리스트를 넘파이 배열로 변경.
# print(z)
# print(type(z)) ## <class 'numpy.ndarray'>


# ## dtype=
# a = np.array([[1, 2, 3.5], [4, 5, 6.5]], dtype=int) ## 층마다 대괄호. int는 소숫점 버림.
# b = np.array([[1, 2, 3.5], [4, 5, 6.5]], dtype=float) ## float은 실수라서 전부 .을 붙임.
# print(a)
# print(b)


# ### 2교시) numpy vs list
# ## numpy와 list 비교 == numpy는 연산이 되는구나 알면 됨.
# a = [1,2,3,4]
# b = [5,6,7,8]
# print(a + b) ## [1, 2, 3, 4, 5, 6, 7, 8]
# # print(a * b) ## 오류 발생

# a_n = np.array(a)
# b_n = np.array(b)
# print(a_n + b_n) ## [ 6  8 10 12]
# print(a_n - b_n)
# print(a_n * b_n)
# print(a_n / b_n)
# print(a_n == 2) ## [False  True False False]

# arr1 = np.array(a)
# print(a * 5)
# print(arr1 + 5)
# print(arr1 - 5)
# print(arr1 * 5)
# print(arr1 / 5)


# ## 1차원 배열 인덱스
# a = np.array([1,2,3,4,5,6])
# print(a[0])
# print(len(a))
# print(a[-2])



# ### 2교시) numpy 2차원 배열
# ## numpy 2차원 배열 == np.array([[], [], ...]) >> 소괄호 안의 대괄호 안의 대괄호
# x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(x)


# ## len(), len([]), .shape
# print(len(x)) ## nrow
# print(len(x[0])) ## ncol
# print(x.shape) ## (4, 3) >> 행, 열 순서로 적힘.


# ## 2차원 배열 인덱스 >> 이상:미만
# print(x[1,2])
# print(x[0,:]) ## : == 해당 라인 전부
# print(x[:,0])
# print(x[1:,0])
# print(x[:2,0])


# ## np.zeros(), np.ones() == 초기값 0 또는 1로 생성. 가장 많이 씀.
# a = np.ones(5)
# print(a)

# b = np.zeros((5,5)) ## 2차원 만들고 싶으면 소괄호 두 번
# print(b)

# a = np.zeros(43)
# print(a)


# ## np.random.randint() == 랜덤 초기값 설정
# a = np.random.randint(0,10,(3,4))
# print(a)

# b = np.random.rand() ## 소수 랜덤 출력.
# print(b)

# c = np.random.normal(0, 1, (3,3)) ## 평균이 0이고, 표준편차가 1인 표준 정규인 배열
# print(c)


# ## .reshape(,) 배열 구조 변경.
# a = np.array([1,2,3,4,5,6,7,8])
# b = a.reshape(2,4) ## 총 원소의 갯수는 맞춰서 변경해야 함.
# print(b)
# c = b.reshape(-1,) ## 무조건 한 줄로 바꿔 버린다.
# print(c) 


# ## .flatten()
# d = b.flatten()
# print(d) ## 위 reshape(-1,)과 결과 동일. 한 줄로 바뀜.


# ## np.concatenate([,]) == 한 줄로 붙임.
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# c = np.concatenate([a,b]) ## 소괄호 안에 대괄호 안에 열거
# print(c)


# ## np.vstack(), np.hstack()
# d = np.vstack((a,b)) ## 아래로 붙이기
# print(d)
# e = np.hstack((a,b)) ## 옆으로 붙이기
# print(e)


# ## 최대, 최소 및 기술 통계값. numpy 호출 안 했으면 그냥 함수로 사용됨.
# x = np.array([1, 2, 3, 4])
# print(np.sum(x))
# print(x.sum())
# print(x.min())
# print(x.max())
# print(x.argmin()) ## 최소값의 위치. y = x^2+1 == 1이지만 0으로 나옴.
# print(x.argmax())
# print(x.mean())
# print(np.var(x))
# print(np.std(x))



# ### numpy 예제
# ## 예제 1)
# a=[1,2,3,4,5]
# b=[]
# for i in a:
#     b.append(i+1)
# print(b)

# a=[1,2,3,4,5]
# b=np.array(a)
# print(b+1)


# ## 예제 2)
# a = np.array([1,3,5,7,8,11])
# b = a.reshape((2,3))
# print(b)


# ## 예제 3)
# a = np.array([1,3,5,7,8,11])
# res1 = np.add(10,30)
# res2 = np.subtract(40,93)
# res3 = np.multiply(55,71)
# res4 = np.divide(250,25)
# print(res1, res2, res3, res4)


# ## 예제 4)
# a = np.random.random((10, 10))
# min_a = a.min()
# max_a = a.max()
# print(a)
# print(min_a, max_a)


# 여기부터 위로 주석 해제
### 2교시) pandas Series
import numpy as np
import pandas as pd

a = pd.Series([1,2,3,4, np.nan]) ## np.nan은 값이 정해지지 않은 것. NaN으로 출력.
print(a)


## Series 생성 방법 1) 딕셔너리로
from pandas import Series ## 윗부분에서 배운 것처럼.
dict_data = {'이지상': 95, '하진영':82, '박주희':79, '김소연':91}
series_data = Series(dict_data) ## 위에 as pd 했으면 pd.Series로 해도 같은 내용.
print(type(series_data))
print(series_data)


## Series 생성 방법 2) 리스트로
from pandas import Series
list_name = ['이지상','하진영','박주희','김소연']
list_data = [95, 82, 79, 91]
series_data = Series(data = list_data, index=list_name) ## 행 이름에 저 리스트 대입해 달라 == index=list명
print(type(series_data))
print(series_data)


## Series 데이터 접근
list_name = ['이지상','하진영','박주희','김소연']
list_data = [95, 82, 79, 91]
series_data = Series(data = list_data, index=list_name)
print(series_data['하진영']) ## 82(값만 호출)
print(series_data[1]) ## 82(값만 호출)
print(series_data['이지상':'박주희']) ## 키로 호출하면 포함
print(series_data[0:4]) ## 인덱스로 호출하면 미만
print(series_data[['이지상']]) ## 키와 값 같이 호출
print(series_data[['이지상','박주희']]) ## : 말고 , 쓸 경우 각각의 값 연달아 호출


## Series : 산술 연산 시 데이터가 한쪽에 데이터가 존재하지 않으면 그 결과는 NaN
list_name1 = ['이지상','하진영','박주희','김소연']
list_data1 = [15, 32, 29, 41]
series_data1 = Series(data = list_data1, index=list_name1)
list_name2 = ['이지상','정소민','박주희','김승주']
list_data2 = [69, 22, 13, 61]
series_data2 = Series(data = list_data2, index=list_name2)
new_series = series_data1 + series_data2 ## 겹치는 것만 연산, 한 쪽에만 존재하면 NaN 출력.
print(new_series)


## .unique()
data = ['라일락','코스모스','코스모스','장미','코스모스','장미']
series_data = Series(data)
print(series_data.unique()) ## 중복값 제외하고 종류만 호출.


## .value_counts()
print(series_data.value_counts()) ## 중복값 제외하고 요약해서 호출.


## .isin([])
print(series_data.isin(['라일락']))
# 결과 >> 일치하는 부분에 불 자료형으로 호출
# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# dtype: bool


### 2교시) pandas DataFrame
## DataFrame() == 시리즈가 여러개 합쳐진 자료형
## index는 행 이름, colums는 열 이름


## 생성 방법 1) 딕셔너리로
from pandas import DataFrame
dict_data ={'나이':[20,21,24], '성별':['여','남','여'], '학교':['A','B','C']}
df = DataFrame(dict_data, index=['김지연','이태형','전지희'])
print(type(df))
print(df)


## 생성 방법 2) 리스트로
df = DataFrame([[20,'여','A'], [21,'남','B'], [24,'여','C']],index=['김지연','이태형','전지희'], columns=['나이','성별','학교'])
print(type(df))
print(df)


## 이름 바꾸기
df.index = ['학생1','학생2','학생3']
df.columns = ['Age','Gender','School']
print(df.index)
print(df.columns)

df.rename(columns={'나이':'age','성별':'gender','학교':'school'}, inplace=True)
## inplace=True 필수
print(df)
print(df.index)
print(df.columns)


## .drop() == 행 삭제
df2=df.copy()
df2.drop('전지희',inplace=True)
print(df2)

df3 = df.copy()
df3.drop('성별', axis=1, inplace=True)
print(df3)


## .loc[] 이름으로 인덱싱
label1 = df.loc['김지연']
print(label1)


## .iloc[] 숫자로 인덱싱
label2 = df.iloc[0]
print(label2)

