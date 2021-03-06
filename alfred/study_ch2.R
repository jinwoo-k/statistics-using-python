par(family="NanumGothic")

library(qcc) # for pareto.chart

data  = read.csv("aboard2.csv",header=T,sep=",")

#$)C55<v:PFwG%
tbl = table(data$fld_sttus)
print(tbl)
xtbl = xtabs(~fld_sttus,data)
print(xtbl)
#$)C;s4k55<v
proptbl = prop.table(tbl)
print(proptbl)

#$)CFD@LBwF.
pie(tbl)

#$)C874k1W7!GA
barplot(tbl)
barplot(proptbl)

#$)CFD79Ed BwF.
pareto.chart(tbl)

#$)CA!55G%
stripchart(data$diff2)
stripchart(data$diff2,method="stack")
stripchart(data$diff2,method="jitter")

#$)C?9A&7 (p20)
student = c(181,161,170,160,158,169,162,179,183,178,171,177,163,
            158,160,160,158,174,160,163,167,165,163,173,178,170,
            167,177,176,170,152,158,160,160,159,180,169,162,178,
            173,173,171,171,170,160,167,168,166,164,174,180)
table(student)

#$)C0h1^180#<v A$GO1b
nclass.Sturges(student)
nclass.scott(student)
nclass.FD(student)

#$)CHw=:Ed1W7% /55<v4Y0"G|
hist(student)
hist(student,freq=F)
h1 = hist(student,breaks=seq(149.5,184.5,by=5),freq=T,labels = TRUE)
lines(h1$mids,h1$counts,type="b",pch=23,bg="orange")
h1 = hist(student,breaks=seq(149.5,184.5,by=2),freq=F,labels = TRUE)
lines(h1$mids,h1$density,type="b",pch=23,bg="orange")
lines(density(student))
print(h1)


## $)CHw=:Ed1W7%@G 874k3t@L
rfreq = h1$counts/length(student)
print(rfreq)
print(rfreq/5)

#$)CAY1b-@Y1W82
stem(data$diff2)

