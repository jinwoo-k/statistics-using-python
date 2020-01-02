# 12장 ===========================================================================================

# 본문 시작
import scipy.stats as stats
stats.norm.ppf(0.6) # qnorm in R
stats.norm.cdf(0.6) # pnorm in R
stats.t.ppf(1-0.05/2, n1+n2-2) # qt in R
stats.t.cdf(0.5, 0.7) # pt in R

# 자료 입력(12장_그림1)
import numpy as np
x = np.array([77, 77, 78, 78, 81, 81, 82, 82, 82, 82,
              82, 83, 83, 84, 84, 84, 84, 85, 86, 86,
              86, 86, 86, 87, 87, 87, 87, 87, 87, 87,
              89, 89, 89, 89, 89, 89, 89, 90, 90, 90,
              91, 91, 91, 91, 91, 91, 91, 91, 91, 91,
              93, 93, 93, 93, 93, 93, 94, 94, 94, 94,
              94, 94, 94, 94, 94, 94, 94, 94, 95, 95,
              95, 95, 95, 96, 96, 96, 96, 96, 96, 97,
              97, 97, 97, 97, 97, 97, 97, 97, 98, 99,
              100, 100, 100, 100, 100, 100, 100, 100,
              100, 101, 101, 101, 101, 101, 101, 102,
              102, 102, 102, 102, 102, 103, 103, 104,
              104, 104, 105, 107])
y = np.array([71, 72, 73, 74, 75, 77, 78, 79, 79, 79,
              79, 80, 80, 80, 81, 81, 81, 82, 82, 82,
              82, 84, 84, 84, 84, 84, 84, 85, 85, 85,
              85, 85, 85, 86, 86, 87, 88, 90, 91, 94])

# 표준오차 계산(12장_그림2)
import numpy as np
import math
var1 = np.var(x, ddof=1); print(var1)
var2 = np.var(y, ddof=1); print(var2)
n1 = len(x); print(n1)
n2 = len(y); print(n2)
se = math.sqrt(var1/n1 + var2/n2); print(se)

# 신뢰구간 계산(12장_그림3)
from scipy import stats
import numpy as np
z_alpha = stats.norm.ppf(1 - 0.05/2); print(z_alpha)
interval_z = z_alpha * se; print(interval_z)
xbar1 = np.mean(x); print(xbar1)
xbar2 = np.mean(y); print(xbar2)
diff = xbar1 - xbar2; print(diff)
CI_1 = [diff - interval_z, diff + interval_z]; print(CI_1)

# 합동추정량 및 표준오차 계산(12장_그림4)
import math
spooled = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2); print(spooled)
se_spooled = math.sqrt(spooled) * math.sqrt(1/n1 + 1/n2); print(se_spooled)

# 신뢰구간 계산(12장_그림5)
from scipy import stats
t_alpha = stats.t.ppf(1 - 0.05/2, n1 + n2 - 2); print(t_alpha)
interval_t = t_alpha * se_spooled; print(interval_t)
CI_2 = [diff - interval_t, diff + interval_t]; print(CI_2)