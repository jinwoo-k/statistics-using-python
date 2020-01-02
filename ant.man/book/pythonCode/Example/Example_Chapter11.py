#11_9
bacteria=np.array([175,190,215,198,184,207,210,193,196,180])
#11_10
xbar_b=np.mean(bacteria)
var_b=np.var(bacteria,ddof=1)
sd_b=np.std(bacteria,ddof=1)
median_b=np.median(bacteria)
min_b=np.min(bacteria)
max_b=np.max(bacteria)
sum_b=np.sum(bacteria)
n=bacteria.size

#11_11
se_b=stats.sem(bacteria);print(se_b)
t_alpha=stats.t.ppf(1-0.1/2,n-1);print(t_alpha)
interval=t_alpha*se_b;print(interval)
CI=[xbar_b-interval,xbar_b+interval];print(CI)


#11_12
tval=(xbar_b-200)/se_b;print(tval)
pval=stats.t.cdf(tval,n-1);print(pval)
#11_13
x=np.array([31,35,37,38,38,38,39,40,40,41,42,43,44,44,46,48])
#11_14



import statsmodels.api as sm
sm.qqplot(x,line="r")


#11_15
xbar_x=np.mean(x);print(xbar_x)
var_x=np.var(x,ddof=1);print(var_x)
sd_x=np.std(x,ddof=1);print(sd_x)
median_x=np.median(x);print(median_x)
min_x=np.min(x);print(min_x)
max_x=np.max(x);print(max_x)
sum_x=np.sum(x);print(sum_x)
n=x.size;print(n)
#11_16
se=stats.sem(x);print(se)
t_alpha=stats.t.ppf(1-0.05/2,n-1);print(t_alpha)
interval=t_alpha*se;print(interval)
CI=[xbar_x-interval,xbar_x+interval];print(CI)
#11_17
tval=(xbar_x-38)/se;print(tval)
pval=1-stats.t.cdf(tval,n-1);print(pval)
