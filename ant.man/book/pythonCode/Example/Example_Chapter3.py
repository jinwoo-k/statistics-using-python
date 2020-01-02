#------------ descriptive summary --------------------
import numpy as np

# length
count = len(drink)
print(count)
# mean
mean = np.mean(drink)
print(mean)
# median
median = np.median(drink)
print(median)
# quantile
per = np.percentile(drink,[0,25,50,75,100])
print(per)
# var
var = np.var(drink)
print(var)
# std
std = np.std(drink)
print(std)
# min, max, range
min, max = np.min(drink), np.max(drink)
print(min,max)
range = max - min
print(range)
# IQR
q75, q25 = np.percentile(drink, [75, 25])
print(q75,q25)
IQR = q75 - q25
print(IQR)

# 10백분위수,90백분위수
per01_09 = np.percentile(drink,q=[10,90])
print(per01_09)

# summary
drink_df = pd.DataFrame(drink)
summary = drink_df.describe()
print(summary)

print('길이     :' , count,'\n',
      '평균     :' , mean,'\n',
      '분산     :' , var , '\n',
      '표준편차 :' , std, '\n',
      '중앙값   :' , median ,'\n',
      '최댓값   :' , max  , '\n',
      '최솟값   :' , min  , '\n',
      '제1사분위수 :', per25, '\n',
      '제2사분위수 :', per50, '\n',
      '제3사분위수 :', per75, '\n',
      '사분위수범위 :' ,IQR,'\n'
      )

