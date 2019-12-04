# H0
#  두 신발 원재료 A, B는 닳는 정도가 같다 
#  (mu1 = mu2, ie. difference = 0)
# H1 
#  두 신발 원재료 A, B는 닳는 정도가 다르다
#  (mu1 != mu2, ie. difference != 0) => 양측검정

# 예제 데이터
library(MASS)
str(shoes)
# t.test 사용해보자ㅣ
t_test = t.test(shoes$A, shoes$B,
       alternative = c("two.sided"), 
       paired = TRUE, 
       conf.level = 0.95)
print(t_test)
## 직접구해보자!
D = shoes$A - shoes$B
n = length(D)
mean_D = mean(D) #표본평균
sd_D = sd(D)     #표본표준편차
t = (mean_D - 0) /(sd_D/sqrt(n)) 
print(t)
alpha = 0.05
t_half_alpha  = qt(alpha/2, n-1, lower.tail = FALSE, log.p = FALSE)
print(t_half_alpha)
t_interval = c(mean_D-t_half_alpha*sd_D/sqrt(n),mean_D+t_half_alpha*sd_D/sqrt(n))
print(t_interval)
pval = 2*pt(t, n-1, lower.tail = TRUE, log.p = FALSE)
print(pval)
