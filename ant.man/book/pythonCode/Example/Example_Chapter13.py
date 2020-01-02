# 13장 ===========================================================================================

# 자료 입력(13장_그림12)

import numpy as np
height = np.array([181, 161, 170, 160, 158, 168, 162, 179, 183, 178,
                   171, 177, 163, 158, 160, 160, 158, 173, 160, 163,
                   167, 165, 163, 173, 178, 170, 167, 177, 175, 169,
                   152, 158, 160, 160, 159, 180, 169, 162, 178, 173,
                   173, 171, 171, 170, 160, 167, 168, 166, 164, 173,
                   180])
weight = np.array([78, 49, 52, 53, 50, 57, 53, 54, 71, 73,
                   55, 73, 51, 53, 65, 48, 59, 64, 48, 53,
                   78, 45, 56, 70, 68, 59, 55, 64, 59, 55,
                   38, 45, 50, 46, 50, 63, 71, 52, 74, 52,
                   61, 65, 68, 57, 47, 48, 58, 59, 55, 74,
                   74])

# 회귀분석 및 결과(13장_그림13)
import pandas as pd
import statsmodels.formula.api as smf
d = {'height' : height, 'weight' : weight}
dat = pd.DataFrame(data = d)
fit = smf.ols('weight ~ height', data=dat).fit()
print(fit.summary())

# 회귀계수의 신뢰구간(13장_그림14)
fit.conf_int(0.05)

# 잔차도, 적합도, 잔차 정규확률도(13장_그림16)

import numpy as np
import matplotlib.pyplot as plt
from statsmodels import regression
from scipy import stats
import pylab
from matplotlib import font_manager, rc, rcParams
font_name = font_manager.FontProperties(fname = 'C:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family = font_name, size = 10)
rcParams['axes.unicode_minus'] = False
plt.subplot(2,2,1)
slope, intercept = np.polyfit(height, weight, 1)
abline_values = [slope * i + intercept for i in height]
plt.plot(height, weight, 'o')
plt.plot(height, abline_values, 'b')
plt.title('키(height) 선 적합도')
plt.xlabel('height')
plt.ylabel('weight')
plt.tight_layout()
plt.subplot(2,2,2)
r = statsmodels.regression.linear_model.RegressionResults.resid(fit)
plt.plot(height, r, 'o')
plt.title('키(height) 잔차도')
plt.xlabel('height')
plt.ylabel('weight')
plt.tight_layout()
plt.subplot(2,2,3)
stats.probplot(r, dist = 'norm', plot = pylab)
plt.title('잔차 정규 확률도')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.tight_layout()