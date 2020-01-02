#10_8
import numpy as np
height=np.array([163,161,168,161,157,162,153,159,164,170,
                 152,160,157,168,150,165,156,151,162,150,
                 156,152,161,165,168,167,165,168,159,156])
#10_9
xbar_h=np.mean(height);print(xbar_h)
var_h=np.var(height,ddof=1);print(var_h)
sd_h=np.std(height,ddof=1);print(sd_h)
median_h=np.median(height);print(median_h)
min_h=np.min(height);print(min_h)
max_h=np.max(height);print(max_h)
sum_h=np.sum(height);print(sum_h)
n=height.size;print(n)


#10_10
from scipy import stats
se_h=stats.sem(height);print(se_h)
z_alpha=stats.norm.ppf(1-0.05/2);print(z_alpha)
interval=z_alpha*se_h;print(interval)
CI=[xbar_h-interval,xbar_h+interval];print(CI)

#10_11
zval=(xbar_h-159)/se_h;print(zval)


#10_12
pval=2*(1-stats.norm.cdf(zval));print(pval)
#10_13
noise=np.array([55.9,63.8,57.2,59.8,65.7,62.7,60.8,51.3,61.8,56.0,
                66.9,56.8,66.2,64.6,59.5,63.1,60.6,62.0,59.4,67.2,
                63.6,60.5,66.8,61.8,64.8,55.8,55.7,77.1,62.1,61.0,
                58.9,60.0,66.9,61.7,60.3,51.5,67.0,60.2,56.2,59.4,
                67.9,64.9,55.7,61.4,62.6,56.4,56.4,69.4,57.6,63.8
                ])
#10_14
xbar_n=np.mean(noise);print(xbar_n)
sd_n=np.std(noise,ddof=1);print(sd_n)
n=noise.size;print(n)
#10_15
se_n=stats.sem(noise);print(se_n)
z_alpha=stats.norm.ppf(1-0.02/2);print(z_alpha)
interval=z_alpha*se_n;print(interval)
CI=[xbar_n-interval,xbar_n+interval];print(CI)
#10_16
zval=(xbar_n-60)/se_n;print(zval)

#10_17
pval=stats.norm.sf(np.abs(zval));print(pval)
