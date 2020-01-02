## chapter 14

##ex1
##figure 1

    import numpy as np
    import pandas as pd

    y = np.array([10,15,8,12,15,
            14,18,21,15,
            17,16,14,15,17,15,18,
            12,15,17,15,16,15])
    treat = np.repeat(['A','B','C','D'],[5,4,7,6])
    data = pd.DataFrame({'y':y,'treat':treat})

    data


    from statsmodels.formula.api import ols
    import statsmodels.api as sm

##figure 2

    lmFit = ols('y ~ treat', data = data).fit()
    sm.stats.anova_lm(lmFit)





