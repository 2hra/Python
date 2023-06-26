#### 2022-2학기 데이터마이닝이해와실습 (데사B0002 중간고사) #####

# ----------------------------------------------------------------------------------------------------------
# 다음과 같은 행위를 부정행위로 간주하며, 온라인 시험 부정행위에 대해서는 관련자 모두를 0점(F)처리하고 학칙에 따라 징계처분 될 수 있으니 유념하시기 바랍니다.
# (1) 대리시험을 치르는 행위
# (2) 시험 중 문제나 답안을 전화, SNS, 단톡방, 문제풀이 사이트 등을 통해 공유하는 행위
# (3) 시험도중 시험화면을 이탈하거나 특수키(Ctrl, Alt, Window key 등) 사용, 다른 프로그램을 사용하는 행위
# (4) 동일 장소 내에서 동일한 IP Address를 사용하는 행위
# (5) 중복 로그인(하나의 ID로 두 개 이상의 컴퓨터에서 동시접속)하는 행위
# (6) 마우스 커서가 시험 응시화면에서 이탈되는 경우
# (7) 오픈북 시험이 아닌데 교재나 시험관련 자료를 펴놓고 시험을 보는 행위
# ----------------------------------------------------------------------------------------------------------

# 본인은 온라인 시험 관련 모든 유의사항을 확인하였고 부정행위를 하지 않을 것이며, 부정행위를 하였을 경우에는 0점(F학점)을 감수하며 학칙에 따른 징계절차에 따르겠습니다.
# 위의 사항에 동의할 경우 아래 대답에 "동의합니다" 라고 작성해 주십시오.

#### 대답 : 동의합니다
#### 학번 : 20211648
#### 이름 : 이효라
#### 제출할 때 파일명을 학번.py로 변경해서 제출하시기 바랍니다.


#### 1번 문제 #####
for i in range(1,11):
    if i % 2 == 0:
        print("%d는 짝수입니다."%i)
    else:
        print("%d는 홀수입니다."%i)



#### 2번 문제 #####
i = 1
while i <= 30:
    if i%2 == 0 or i%3 == 0:
        i += 1
        pass
    else:
        print(i)
        i += 1



#### 3번 문제 #####
def rem(a,b):
    result = a % b
    print(result)

rem(9,3) #0
rem(7,5) #2


#### 4번 문제 #####
word = input("영단어를 입력해주세요:")
result = word[0] + str(len(word)) + word[-1]
print(result)


#### 5번 문제 ##### (txt파일은 제출할 필요 없음)
f = open('name.txt', 'w')
name = ['Alex','Emma','Smith','Jane','Ava','Charlotte','Evelyn']

for i in name:
    if len(i) == 4:
        f.write('%s\n' % i)
    else: pass

f.close()


#### 6번 문제 #####
score = {'국어': 90, '영어':95,'수학':77, '미술':68, '과학': 82}
sum = 0
average = 0.0
for i in score.keys():
    sum += score[i]
    print("%s 과목의 점수는 %d 입니다."%(i, score[i]))
average = sum/len(score)
print("전체 평균은 %d 입니다."%average)



#### 7번 문제 #####
def check_number(string):
    result = []
    for i in string:
        if i=='3' or i=='6' or i=='9':
            result.append('x')
        else:
            result.append(i)
    print(result)

check_number("010-9012-3569")


#### 8번 문제 #####
answer = input("학번을 입력해 주세요:")

# coding here ##
n1 = int(int(answer)/100000%10)
n2 = int(int(answer)/10000%10)
num = '%d%d'%(n1,n2)
id = str(num)

print("당신은 %s학번 입니다."%id)


#### 9번 문제 #####
visit = ['영국','일본','미국','프랑스','폴란드','칠레','캐나다','이탈리아']
wish = ['브라질', '독일', '캐나다', '호주', '영국']
result = []

# coding here ##
for i in wish:
    if i in visit:
        result.append(i)

print(result)


#### 10번 문제 #####

# coding here ##
for i in range(1,7):
    print('%d '%(7-i)*(7-i))

f = open('20211648.txt','w')
for i in range(1,7):
    word = '%d '%(7-i)*(7-i)
    f.write('%s\n'%word)
f.close()










