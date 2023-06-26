### 9/4 넘파이 기본 다지기 6:20~6:47

import numpy as np #넘파이를 줄여서 np라고 함

list_data = [1, 2, 3] #리스트 형태를
array = np.array(list_data) #넘파이로 바꿔 줌

print(array)
print(array.size) #몇 개의 데이터
print(array.dtype) #어떠한 자료형
print(array[2]) #리스트처럼 인덱스 사용 가능


### 0부터 3까지의 배열 만들기
array1 = np.arange(4) # 0부터 해당 숫자 전까지의 배열
print(array1)


### 넘파이 초기화 하기
array2 = np.zeros((4,4),dtype=float)
# zeros는 0으로 초기화해서 만들라는 것
# 4*4 크기의 2차원 배열을 자료형 실수형으로 만들어라

print(array2)
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]


### 1로 초기화하기
array3 = np.ones((3,3), dtype=str)
print(array3)
#[['1' '1' '1'] 문자형, 1로 초기화 3*3
# ['1' '1' '1'] zeros와 작성방법은 같다
# ['1' '1' '1']]


### 0부터 9까지 랜덤으로 초기화
array4 = np.random.randint(0, 10, (3,3)) #np.랜덤.랜덤int(0 이상, 10 미만,(3*3))
print(array4)
#[[8 5 2] 매번 랜덤
# [0 4 5]
# [0 9 0]]


### 평균 0이고, 표준편차가 1인 표준 정규를 띄는 배열 >> 표준 정규 분포
array5 = np.random.normal(0, 1, (3, 3))
print(array5)
#[[-2.12880655 0.73590101 -0.08429047]
# [-0.90579623 0.86225018 -0.0808253 ]
# [ 1.53530935 -0.27039287 -1.18471556]]


### 배열 가로 축으로 합치기
array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])
array_3 = np.concatenate([array_1,array_2])

print(array_3.shape) #(6,) 6개의 데이터가 있다
print(array_3) #[1 2 3 4 5 6] array 적은 순서대로 기재됨


### 배열 형태 바꾸기
#ㅁㅁㅁㅁ 1*4를
#ㅁㅁ
#ㅁㅁ 2*2로 형태 바꾸기
array__1 = np.array([1,2,3,4])
array_4 = array__1.reshape((2,2)) #리쉐잎

print(array_4)
#[[1 2]
# [3 4]]


### 배열 세로 축으로 합치기
array__2 = np.arange(4).reshape(1,4) #4까지의 범위, 1*4의 쉐잎으로
array__3 = np.arange(8).reshape(2,4) #8까지의 범위, 2*4의 쉐잎으로

print(array__2)
print(array__3)
#[[0 1 2 3]] #__2
#[[0 1 2 3] #__3
# [4 5 6 7]]

array__4 = np.concatenate([array__2,array__3],axis=0)
#axis에 0을 넣으면 행이니까 아래에 다음 배열이 바로 합쳐지게 하는 것

print(array__4)
#[[0 1 2 3]
# [0 1 2 3]
# [4 5 6 7]]


### 배열 나누기
array_ = np.arange(8).reshape(2, 4) #8까지의 수를 2*4 2차원 배열로
left, right = np.split(array_, [2], axis=1)

#인덱스 2열(axis 1이 열)을 기준으로 왼쪽, 오른쪽 나눔
print(left.shape)
print(right.shape)
print(array_)
#(2, 2) 2*2
#(2, 2) 2*2
#[[0 1 2 3] #원 형태
# [4 5 6 7]]

print(left)
#[[0 1] #왼쪽 2*2 분리된 형태
# [4 5]]