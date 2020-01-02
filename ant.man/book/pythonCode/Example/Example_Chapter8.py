##예제 11

from scipy.stats import norm
print(norm.cdf(x=50,loc=63,scale=10))

from scipy.stats import norm
print(norm.ppf(q=0.9,loc=63,scale=10))

##예제12

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = np.array([4001,3927,3048,4298,4000,3445,
                4949,3530,3075,4012,3797,3550,
                4027,3571,3738,5157,3598,4749,
                4263,3894,4262,4232,3852,4256,
                3271,4315,3078,3607,3889,3147,
                3421,3531,3987,4120,4349,4071,
                3683,3332,3285,3739,3544,
                4103,3401,3601,3717,4846,
                5005,3991,2866,3561,4003,
                4387,3510,2884,3819,3173,
                3470,3340,3214,3370,3694])
sm.qqplot(data)
plt.title("Normal Q-Q plot")


sm.qqplot(data,line='s')
plt.title("Normal Q-Q plot")
##예제13

import numpy as np
import matplotlib.pyplot as plt

data = np.array([39.3,14.8,6.3,0.9,6.5,
                3.5,8.3,10.0,1.3,7.1,
                6.0,17.1,16.8,0.7,7.9,
                 2.7,26.2,24.3,17.7,3.2,
                 7.4,6.6,5.2,8.3,5.9,
                 3.5,8.3,44.8,8.3,13.4,
                 19.4,19.0,14.1,1.9,12.0,
                 19.7,10.3,3.4,16.7,4.3,
                 1.0,7.6,28.3,26.2,31.7,
                 8.7,18.9,3.4,10.0])

plt.hist(data, bins=5, range=(0,50))
plt.xlabel('data')
plt.ylabel('Density')
plt.title('Historam of data')
plt.show()

sm.qqplot(data,line='s')
plt.title("Normal Q-Q plot")


##제곱근 변환

data2 = np.sqrt(data)
sm.qqplot(data2, line = 's')
plt.title("Normal Q-Q plot")


##네제곱근 변환

data4 = np.power(data,0.25)
sm.qqplot(data4, line = 's')
plt.title("Normal Q-Q plot")



##예제

#6.23 (1)
import numpy as np
import statsmodels.api as sm

data = np.array([9.51,0.28,1.63,1.39,
                 1.58,3.04,1.49,1.79,
                 3.89,0.98])

sm.qqplot(data,line='s')

data_log =  np.log(data)
sm.qqplot(data_log,line='s')


#6.23 (2)
import numpy as np
import statsmodels.api as sm

data = np.array([314.46,361.81,36.23,
                 2253.48,21.57,7.94,
                 46.38,2.60,3.71,37.26])

sm.qqplot(data,line='s')

data_log =  np.log(data)
sm.qqplot(data_log,line='s')

#6.24(1)
import numpy as np
import statsmodels.api as sm

data = np.array([2.97,4.35,2.67,3.27,
                 1.75,4.27,4.19,2.67,
                 1.04,1.93])

sm.qqplot(data,line='s')















