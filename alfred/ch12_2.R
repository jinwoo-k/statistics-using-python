women_weight <- c(38.9, 61.2, 73.3, 21.8, 63.4, 64.6, 48.4, 48.8, 48.5)
men_weight <- c(67.8, 60, 63.4, 76, 89.4, 73.3, 67.3, 61.3, 62.4)
# 남자가 더 몸무게가 많이 나간다는 가정을 검정 
# 분산테스트(분산 동일성 검정)
var.test(men_weight,women_weight,conf.level = 0.95) # 분산이 다름

t_test = t.test(men_weight, women_weight,
                alternative = c("greater"), 
                paired = FALSE, 
                var.equal = FALSE,
                conf.level = 0.95)
print(t_test)
# 직접구할수 있을까?
mean_m = mean(men_weight)
mean_w = mean(women_weight)
var_m = var(men_weight)
var_w = var(women_weight)
n1 = length(men_weight)
n2 = length(women_weight)
df = (var_m/n1+var_w/n2)^2 / ( (var_m/n1)^2/(n1-1)+(var_w/n2)^2/(n2-1))
t = ((mean_m-mean_w) - 0)/sqrt(var_m/n1+var_w/n2)
print(t)
alpha = 0.05
t_alpha = qt(1-alpha,df,lower.tail = TRUE, log.p = FALSE)
print(t_alpha)
sd = sqrt(var_m/n1+var_w/n2)
print(sd)
t_interval = c((mean_m-mean_w)-t_alpha*sd,Inf)
print(t_interval)
p_val =  pt(t, df, lower.tail = FALSE, log.p = FALSE)
print(p_val)
