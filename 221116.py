# ### 1교시
# ## 그래프는 간단하게, 포토샵 같은 시각화를 더 중점적으로 할 것.

# ## Matplotlib 설치 후 버전 확인
# import matplotlib
# print(matplotlib.__version__)


# ## 지난 시간 복습
# import numpy as np


# ## matplotlib의 pyplot
# # import matplotlib ## 이렇게만 호출하면
# # matplotlib.pyplot ## 복잡하게 사용
# from matplotlib import pyplot as plt ## 호출

# ## 그래프 창 오류 설정 방법
# import matplotlib
# ## 그래프 제목 한글 추가 방법. 폰트는 구글링하면 찾을 수 있음.
# matplotlib.rcParams['font.family']='Malgun Gothic' 
# ## 폰트 크기
# matplotlib.rcParams['font.size']=12 
# ## 음수 값 존재 시 마이너스 오류 수정 방법.
# matplotlib.rcParams['axes.unicode_minus']=False

# x = [-1, 2, 3]
# y = [-2, 4, 8]

# ## 1) plt.plot() == 그래프 그릴 값, 선 스타일, 범례 관련
# plt.plot(x,y, 'bx-', label='11월16일데이터')
# ## label = 그래프 내에 범례(레전드) 입력
# ## plt.plot([1,2,3], [2,4,8]) 해도 됨
# ## linewidth는 그래프 선 굵기 조절, linestyle(ls)는 선 모양. color(c)는 선 색상.
# ## marker, markersize, markeredgecolor, markerfacecolor는 그래프 점 모양, 크기 설정
# ## 'ro:', 'bx-' 등 색상, 점 모양, 선 모양 함축해서 입력도 가능함.


# ## 2) plt.legend() == 범례 위치 등 옵션
# plt.legend(loc=4) ## 범례 설정 방법 다양함. 아래 링크로 확인 가능.
# plt.legend(loc=(0.5,0.5)) ## 1을 기준으로 그려질 위치
# ## 범례 설정 (legend) : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html


# ## 3) plt.title, xlabel, ylabel == 제목
# plt.title('그래프', color = 'red') 
# ## 그래프 제목 추가. 뒤에 color 요소 추가해서 색 변경도 가능.
# plt.xlabel('good', color = 'blue', loc = 'left') 
# ## loc(제목 위치 변경) == left, center,  right
# plt.ylabel('bad', color = 'green', loc='bottom') 
# ## loc == top, center, bottom


# ## 4) plt.x(y)ticks == 축 범위 지정
# plt.xticks([-10,-8,-0,5]) 
# ## 그래프 x축 범위 직접 지정
# plt.yticks([-6,0,10]) 
# ## 그래프 y축 범위 직접 지정


# ## 5) plt.figure()
# ## plt.figure(figsize=(6,4), dpi = 200) 
# ## 크기, 해상도 조정.


# ## 6) plt.show() == 그래프 띄우기
# plt.show() ## vscode에서 그래프 보여주는 함수. Q 누르면 창 닫힘.


# ## 7) plt.savefig() == 그래프 저장
# plt.savefig('20211648plt.jpg') ## plt.show 실행 안 되어야 정상으로 저장됨.


# ## 8)  enumerate 함수는
# from matplotlib import pyplot as plt
# import matplotlib
# matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['axes.unicode_minus'] = False

# x = [-1, 2, 3]
# y = [-2, 4, 8]

# plt.plot(x, y)

# for idx, txt in enumerate(y):
#     plt.text(x[idx], y[idx] + 0.5, txt, ha = 'center')
#     ## for a, b in enumerate(큰 범위의 값): 
#     ##      a(앞의 변수) == 일반적 for문의 i와 같음. txt는 값 저장.
#     ## plt.text(x[a], y[a] + 0.3, txt, ha=, color=) 
#     ##      x[a], y[a] 인덱스 좌표일 때 값을 기재하는 함수.
#     ##      값 뒤에 +-는 txt 값을 위아래 어디에 기재할지.
#     ##      ha = 'center' == 해당 좌표 정중앙에 값 기재

# plt.plot(x, y, label='first') ## 그래프별로 레전드 입력 가능
# plt.plot(y, x, label='second')

# plt.show()



# ### 2교시
# ##  Pillow == 이미지 처리 프로그램
# from PIL import Image
# img = Image.open('1116pic.jpg')

# ## 기본적인 활용법
# print(img.size) ## 이미지 크기 확인
# print(img.format) ## 이미지 확장자 확인
# img.show() ## 이미지 띄우기
# img.save('1116pic.png')

# ##  Image data augmentation (증강시킴.)
# from PIL import Image
# img = Image.open('1116pic.jpg')

# ## RGB 분리(tenser로 되어있는 것)
# r, g, b = img.split() 
# print(r.size) ## 사이즈는 기존 이미지와 동일.
# ## 분리한 이미지로 띄우기
# # r.show()
# # g.show()
# # b.show()

# ## 이미지 좌우반전, 상하반전
# img.show()
# img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
# img2.show()
# img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
# img3.show()


# ## 이미지 회전
# img4 = img.rotate(45, expand=True) ## 각도, expand=True == 이미지 잘리지 않도록.
# img4.show()


# ## 이미지 잘라내기
# img5 = img.crop((100,200,300,500)) ## 좌측 상단 좌표, 우측 하단 좌표
# img5.show()


# ## 이미지 병합 (다시 하기)
# from PIL import Image
# img6 = Image.open('n1116pic.jpg')
# img7 = Image.open('n1117pic.jpg')
# img7_r = img7.resize([1920,900])


# ## 밝게 하기
# from PIL import ImageEnhance
# img = Image.open('1116pic.jpg')

# img = ImageEnhance.Brightness(img).enhance(3.0)
# img.show()


# ## 어둡게 하기
# img = ImageEnhance.Brightness(img).enhance(0.4)
# img.show()


# ## 흑백으로 변환하기
# from PIL import ImageOps
# img = Image.open('1116pic.jpg')
# img = ImageOps.grayscale(img)
# img.show()


# ## 엠보싱 효과
# from PIL import ImageFilter
# img = img.filter(ImageFilter.EMBOSS)
# img.show()


# ## 스케치 효과 
# img = img.filter(ImageFilter.CONTOUR)
# img.show()



# ### 실습 1)
# from PIL import Image
# f = open('list.txt','r')
# lines = f.readlines()
# directory_name = 'images/' ## 경로 지정하는 것

# for line in lines:
#     filename = directory_name + line.strip()
#     img = Image.open(filename)

#     img2 = img.rotate(45, expand=True)
#     img2.save(filename.replace('dog','rot_dog'))
#     print(filename)

# f.close()


# ### 실습 2)
# from PIL import Image
# f = open('list.txt','r')
# lines = f.readlines()
# directory_name = 'images/'

# fw = open('summary.txt','w')
# for line in lines:
#     filename = directory_name + line.strip()
#     img = Image.open(filename)
#     # print(img.size)
#     result = line.strip() + ' 이미지의 가로는 ' + str(img.size[0]) + ', 세로는 ' + str(img.size[1]) + '입니다.'
#     # print(result)
#     fw.write(result + '\n')

# fw.close()
# f.close()



# ### 3교시
# ## OpenCV
# import cv2
# print(cv2.__version__)

# ## 이미지 출력
# img = cv2.imread('1116pic.jpg', cv2.IMREAD_COLOR)
# img2 = cv2.resize(img, dsize=(200,300))

# cv2.imshow("image", img) ## 창 이름, 불러올 이미지 변수명
# cv2.waitKey(0)
# cv2.destroyAllWindows


# ## 카메라 출력
# import cv2
# cap = cv2.VideoCapture(0) ## 0으로 하면 카메라. '동영상 파일명'을 하면 영상이 띄워짐.
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) ## .set은 가로세로 설정하는 것.
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# while cv2.waitKey(33) < 0: ## Q 누르면 종료됨.
# ## while문이라 무한 반복. 이미지 1초에 30개가 동영상. 1초에 이미지 33장 불러오도록 반복문 만든 것.
#     ret, frame = cap.read()
#     cv2.imshow("image", frame)

# cap.release() ## f.close()처럼 메모리 지워 주는 것.
# cv2.destroyAllWindows()


# ## 이미지 대칭
# import cv2
# img = cv2.imread("1116pic.jpg", cv2.IMREAD_COLOR)
# img2 = cv2.resize(img, dsize=(400,300))
# img2_r = cv2.flip(img2, 0)
# #dst = cv2.flip(src, 1)
# #dst = cv2.flip(src, -1)
# cv2.imshow("img2", img2)
# cv2.imshow("dst", img2_r)
# cv2.waitKey()


# ## 이미지 회전
# import cv2
# img = cv2.imread("1116pic.jpg")
# img = cv2.resize(img, dsize=(300,300))
# height, width, channel = img.shape
# matrix = cv2.getRotationMatrix2D((width/2, height/2), 30, 1)
# ## 매트릭스 공식(회전변환행렬 계산식)을 만들어서 그만큼 회전. 30도 각도 회전.
# dst = cv2.warpAffine(img, matrix, (width, height))

# cv2.imshow("src", img) ## 창 이름 설정 필요
# cv2.imshow("dst", dst)
# cv2.waitKey()


# ## 이미지 자르기
# import cv2
# img = cv2.imread("1116pic.jpg", cv2.IMREAD_COLOR)
# img2 = img[100:600, 200:700].copy() 
# ## copy를 해야 원본 손상 없음.
# ## 세로, 가로 길이 순서로 해야 함.

# cv2.imshow("IMG", img)
# cv2.imshow("IMG2", img2)
# cv2.waitKey()


# # 색상 공간 변환은 패스. 나머진 한 번씩 쳐 보기.



# ### 실습 3)
# import cv2

# f = open('list.txt','r')
# lines = f.readlines()
# directory_name = 'images/' ## 경로 지정하는 것

# for line in lines:
#     filename = directory_name + line.strip()
#     # print(filename)
#     img = cv2.imread(filename)

#     height, width, channel = img.shape
#     matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1) ## 이 줄, 아랫줄을 알아야 함.
#     dst = cv2.warpAffine(img, matrix, (width, height))

#     new_name = filename.replace('dog','rot_dog')
#     cv2.imwrite(new_name, dst) ## 저장하는 방법. cv2.imwrite(내용)

# f.close()

# # 파일 이름 불러와서 읽고, 수정해서 저장하는 매커니즘은 알아야 함.



# ### 실습 4)
# import cv2

# f = open('list.txt','r')
# lines = f.readlines()
# directory_name = 'images/' ## 경로 지정하는 것

# fw = open('summary1116.txt','w')
# for line in lines:
#     filename = directory_name + line.strip()
#     # print(filename)
#     img = cv2.imread(filename)
#     # print(img.size)
#     height, width, channel = img.shape
#     result = line.strip() + ' 이미지의 가로는 ' + str(width) + ', 세로는 ' + str(height) + '입니다.'
#     # print(result)
#     fw.write(result + '\n')

# fw.close()
# f.close()