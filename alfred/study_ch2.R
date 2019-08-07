par(family="NanumGothic")

library(qcc) # for pareto.chart

data  = read.csv("aboard2.csv",header=T,sep=",")

#도수분포표
tbl = table(data$fld_sttus)
print(tbl)
xtbl = xtabs(~fld_sttus,data)
print(xtbl)
#상대도수
proptbl = prop.table(tbl)
print(proptbl)

#파이차트
pie(tbl)

#막대그래프
barplot(tbl)
barplot(proptbl)

#파레토 차트
pareto.chart(tbl)

#점도표
stripchart(data$diff2)
stripchart(data$diff2,method="stack")
stripchart(data$diff2,method="jitter")

#예제7 (p20)
student = c(181,161,170,160,158,169,162,179,183,178,171,177,163,
            158,160,160,158,174,160,163,167,165,163,173,178,170,
            167,177,176,170,152,158,160,160,159,180,169,162,178,
            173,173,171,171,170,160,167,168,166,164,174,180)
table(student)

#계급구간수 정하기
nclass.Sturges(student)
nclass.scott(student)
nclass.FD(student)

#히스토그램 /도수다각형
hist(student)
hist(student,freq=F)
h1 = hist(student,breaks=seq(149.5,184.5,by=5),freq=T,labels = TRUE)
lines(h1$mids,h1$counts,type="b",pch=23,bg="orange")
h1 = hist(student,breaks=seq(149.5,184.5,by=2),freq=F,labels = TRUE)
lines(h1$mids,h1$density,type="b",pch=23,bg="orange")
lines(density(student))
print(h1)


## 히스토그램의 막대높이
rfreq = h1$counts/length(student)
print(rfreq)
print(rfreq/5)

#줄기-잎그림
stem(data$diff2)

