### 9/4 pandas 기본 활용법 7:03~7:50

import pandas as pd

array = pd.Series(['사과', '바나나', '당근'], index=['a', 'b', 'c'])

print(array) #인덱스와 값 모두 2차원 배열로 나옴
#a 사과
#b 바나나
#c 당근
#dtype: object

print(array['a']) #특정 인덱스 값이 무엇인지
#사과


### 딕셔너리를 바로 시리즈로 바꾸기
data = {
'a':'사과',
'b':'바나나',
'c':'당근'
}
array_ = pd.Series(data)
print(array_['a']) #사과


### 데이터 프레임이란?
### 다수의 시리즈를 모아 처리하기 위함
### 표 형태로 데이터 손쉽게 출력
word_dict = { #두 개의 딕셔너리 존재, 키는 동일함
'Apple':'사과',
'Banana':'바나나',
'Carrot':'당근'
}

frequency_dict = {
'Apple':3,
'Banana':5,
'Carrot':7
}

word = pd.Series(word_dict) #시리즈로 변경하기
frequency = pd.Series(frequency_dict)
summary = pd.DataFrame({ #이름(Name): 값(Values)
'word': word,
'frequency': frequency
})

print(summary)
# word frequency >>> index, name, values 시리즈로 나열됨
#Apple 사과 3 데이터를 인덱스 기준으로 나누는 것을 데이터프레임이라고 함
#Banana 바나나 5
#Carrot 당근 7


### 시리즈의 연산
word_dict1 = { #세 개의 딕셔너리 존재, 키는 동일함
'Apple':'사과',
'Banana':'바나나',
'Carrot':'당근'
}

frequency_dict1 = {
'Apple':3,
'Banana':5,
'Carrot':7
}

importance_dict1 = {
'Apple':3,
'Banana':2,
'Carrot':1
}

word1 = pd.Series(word_dict1) #시리즈로 변경하기
frequency1 = pd.Series(frequency_dict1)
importance1 = pd.Series(importance_dict1)

summary1 = pd.DataFrame({ #이름(Name): 값(Values)
'word1': word1,
'frequency1': frequency1,
'importance1': importance1
})

score = summary1['frequency1'] * summary1['importance1'] # 시리즈 곱해서 값을 만들어내고
summary1['score'] = score # 위 값을 스코어 구분으로 데이터 프레임에 추가한다

print(summary1)
# word1 frequency1 importance1 score
#Apple 사과 3 3 9
#Banana 바나나 5 2 10
#Carrot 당근 7 1 7


### 데이터 프레임의 슬라이싱
word_dict2 = { #세 개의 딕셔너리 존재, 키는 동일함
'Apple':'사과',
'Banana':'바나나',
'Carrot':'당근',
'Durian':'두리안'
}

frequency_dict2 = {
'Apple':3,
'Banana':5,
'Carrot':7,
'Durian':2
}

importance_dict2 = {
'Apple':3,
'Banana':2,
'Carrot':1,
'Durian':1
}

word2 = pd.Series(word_dict2) #시리즈로 변경하기
frequency2 = pd.Series(frequency_dict2)
importance2 = pd.Series(importance_dict2)

summary2 = pd.DataFrame({ #이름(Name): 값(Values)
'word2': word2,
'frequency2': frequency2,
'importance2': importance2
})

print(summary2)
# word2 frequency2 importance2
#Apple 사과 3 3
#Banana 바나나 5 2
#Carrot 당근 7 1
#Durian 두리안 2 1


### 이름을 기준으로 슬라이싱
print(summary2.loc['Banana':'Carrot', 'importance2':])
# importance2
#Banana 2
#Carrot 1


### 인덱스를 기준으로 슬라이싱 >> 위와 같은 결과

print(summary2.iloc[1:3, 2:]) #0번 빼고 1부터 3 미만까지, 0,1 빼고 2부터 끝까지(인데 이건 importance가 마지막이라서)
# importance2
#Banana 2
#Carrot 1


### 데이터 프레임의 연산

word_dict3 = { #세 개의 딕셔너리 존재, 키는 동일함
'Apple':'사과',
'Banana':'바나나',
'Carrot':'당근',
'Durian':'두리안'
}

frequency_dict3 = {
'Apple':3,
'Banana':5,
'Carrot':7,
'Durian':2
}

importance_dict3 = {
'Apple':3,
'Banana':2,
'Carrot':1,
'Durian':1
}

word3 = pd.Series(word_dict3) #시리즈로 변경하기
frequency3 = pd.Series(frequency_dict3)
importance3 = pd.Series(importance_dict3)

summary3 = pd.DataFrame({ #이름(Name): 값(Values)
'word3': word3,
'frequency3': frequency3,
'importance3': importance3
})

summary3.loc['Apple', 'importance3'] = 5 #데이터 변경
summary3.loc['Elderberry'] = ['엘더베리', 5, 3] # 새 데이터 삽입

print(summary3)
# word3 frequency3 importance3
#Apple 사과 3 5 >> 5로 값 바뀜
#Banana 바나나 5 2
#Carrot 당근 7 1
#Durian 두리안 2 1
#Elderberry 엘더베리 5 3 >> 새 데이터 추가


### 엑셀로 내보내기/불러오기
word_dict_ = {
'Apple':'사과',
'Banana':'바나나',
'Carrot':'당근'
}

frequency_dict_ = {
'Apple': 3,
'Banana': 5,
'Carrot': 7
}

word_ = pd.Series(word_dict_)
frequency_ = pd.Series(frequency_dict_)

summary_ = pd.DataFrame({
'word_': word_,
'frequency_': frequency_
})

summary_.to_csv("summary_.csv", encoding="utf-8-sig") # to_csv로 내보내기, 한글 데이터 잘 인식하기 위해 utf-8-sig

saved = pd.read_csv("summary_.csv", index_col=0) # pd.read_csv로 불러오기

print(saved)
# word_ frequency_ >> 내보낸 거 그대로 출력 잘 되는지 확인
#Apple 사과 3
#Banana 바나나 5
#Carrot 당근 7