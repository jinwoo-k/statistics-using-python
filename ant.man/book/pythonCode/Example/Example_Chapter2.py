# module import

import os
# os.chdir("D:\\Dropbox\\plot")
# os.getcwd()

#------------ data input --------------------
import numpy as np
death = np.array([2, 1, 2, 4, 2, 5, 3, 3, 5, 6, 3, 8, 3,
                  3, 6, 3, 6, 5, 3, 5, 2, 6, 2, 3, 4, 3,
                  2, 9, 2, 2, 3, 2, 7, 3, 2, 10, 6, 2, 3,
                  1, 2, 3, 3, 4, 3, 2, 6, 2, 2, 3, 2, 3,
                  4, 3, 2, 3, 5, 2, 5, 5, 3, 4, 3, 6, 2,
                  1, 2, 3, 2, 6, 3, 3, 6, 3, 2, 3, 6, 4,
                  6, 5, 3, 5, 6, 2, 6, 3, 2, 3, 2, 6, 2,
                  6, 3, 3, 2, 6, 9, 6, 3, 6, 6, 2, 3, 2,
                  3, 5, 3, 5, 2, 3, 2, 3, 3, 1, 3, 3, 2,
                  3, 3, 4, 3, 6, 6, 3, 3, 3, 2, 3, 3, 6])


#------------ frequency table --------------------
import pandas as pd

table = pd.crosstab(index = death , colnames = ["질병"], columns = '도수')
table.index = ["감염","각종암","순환기","호흡기","소화기",
               "사고사","비뇨기","정신병","노환","신경계"]
print(table)
#------------ bar plot --------------------

# 한글 입력
from matplotlib import font_manager, rc

# font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family =font_name)

# 막대 그래프
import matplotlib.pyplot as plt

plt.figure()
table.plot(kind='bar',legend=False)
plt.xlabel('사망원인')
plt.ylabel("빈도수")
plt.title("사망원인에 따른 막대그래프")
plt.xticks(rotation=360)
plt.show()


plt.savefig('./plot/그림18.png') # 그림 저장

#------------ bar plot --------------------

#import matplotlib.patches as mpatches
#import matplotlib.cm
#cause1 = mpatches.Patch(color='b', label=table.index[0])
#cause2 = mpatches.Patch(color='g', label=table.index[1])
#cause3 = mpatches.Patch(color='r', label=table.index[2])
#cause4 = mpatches.Patch(color='c', label=table.index[3])
#cause5 = mpatches.Patch(color='m', label=table.index[4])
#cause6 = mpatches.Patch(color='y', label=table.index[5])
#cause7 = mpatches.Patch(color='k', label=table.index[6])
#cause8 = mpatches.Patch(color='b', label=table.index[7])
#cause9 = mpatches.Patch(color='g', label=table.index[8])
#cause10 = mpatches.Patch(color='r', label=table.index[9])

import matplotlib.pyplot as plt

plt.figure()
colors = 'bgrcmyk'
table.plot(kind='bar',color=colors)
plt.xlabel('사망원인')
plt.ylabel("빈도수")
plt.title("사망원인에 따른 막대그래프")
plt.xticks(rotation=360)
plt.show()


plt.savefig('./plot/그림20.png') # 그림 저장
#------------ pie plot --------------------
import matplotlib.pyplot as plt

plt.figure()
index = ["감염","각종암","순환기","호흡기","소화기",
         "사고사","비뇨기","정신병","노환","신경계"]
plt.pie(table['도수'],labels=index)
plt.rc('font', size=8) # 그래프 글자 크기
plt.title("사망원인에 대한 원형 그래프")
plt.show()

plt.savefig('./plot/그림21.png')

#------------ preto plot --------------------
# 한글 입력
from matplotlib import font_manager, rc

# font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family =font_name)

from paretochart import pareto
import matplotlib.patches as mpatches # 범례 만들기 위한 모듈

plt.figure()
fig, ax = plt.subplots() # subplot 생성
ax.paretoplot = pareto(table['도수'], line_args=('black',),labels=index )
p_legend = mpatches.Patch(color='black', label='누적상대도수') #범례1
p_legend1 = mpatches.Patch(color='blue', label='빈도수') #법례2
plt.legend(handles=[p_legend,p_legend1],loc='center right') #범례 표시

plt.title("사망원인") #제목
plt.xlabel("질병종류") #x축
ax.set_ylabel("Frequency") #왼쪽 y축
plt.ylabel('cumulative percentage') #오른쪽 y축
plt.rc('font', size=6) #그래프 글자크기 조절
plt.show()

plt.savefig('./plot/그림22.png')
#------------ data input --------------------
import numpy as np
drink = np.array([101.8, 101.5, 101.8, 102.6, 101, 96.8, 102.4, 100, 98.8, 98.1,
                  98.8, 98, 99.4,95.5, 100.1, 100.5, 97.4, 100.2, 101.4, 98.7,
                  101.4, 99.4, 101.7, 99, 99.7, 98.9, 99.5, 100, 99.7, 100.9,
                  99.7, 99, 98.8, 99.7, 100.9, 99.9, 97.5, 101.5, 98.2, 99.2,
                  98.6, 101.4, 102.1, 102.9, 100.8, 99.4, 103.7, 100.3, 100.2, 101.1,
                  101.8, 100, 101.2, 100.5, 101.2, 101.6, 99.9, 100.5, 100.4, 98.1,
                  100.1, 101.6, 99.3, 96.1, 100, 99.7, 99.7, 99.4, 101.5, 100.9,
                  101.3, 99.9, 99.1, 100.7, 100.8, 100.8, 101.4, 100.3, 98.4, 97.2])

#------------ histgram --------------------
# 한글 입력
from matplotlib import font_manager, rc
# font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family =font_name)


# 히스토그램

import matplotlib.pyplot as plt

plt.figure()
n, bins, patches = plt.hist(drink, bins = 10, facecolor="blue", alpha = 0.3)
x = [(bins[i]+bins[i+1])/2 for i in range(len(bins)-1)]
w_bin = bins[1]-bins[0]
x.insert(0,x[0]-w_bin)
x.append(x[-1]+w_bin)
n = np.insert(n,0,0.0)
n = np.append(n,0.0)
plt.xlabel('drink')
plt.ylabel('Frequency')
plt.title("Histogram of drink")
plt.plot(x,n,'blue',marker='o')
plt.show()




plt.savefig('./plot/그림26.png')



plt.subplot(2,1,1)