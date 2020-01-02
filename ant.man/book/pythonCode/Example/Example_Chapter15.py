

## chapter 15

##ex9

##figure 1

    import numpy as np

    O = np.array([18,55,27])
    Pr = np.array([0.25,0.50,0.25])
    n = O.sum()
    E = n * Pr
    df = len(O)-1

##figure 2

    from scipy import stats

    chi2, p = stats.chisquare(O,E)
    print (" Chi-squared test for given probabilities",
            "\n","\n",
            "Chi-Squared :", round(chi2,4),"\n",
            "df :",df,"\n",
            "P-Value :",round(p,4))

##figure 3

    sum( ( ( O - E )**2 ) / E )

##ex10

##figure 4

    import pandas as pd
    import numpy as np

    diet = np.array([[37,24,19],[17,33,20]])
    column_names = ['Good', 'Normal', 'Bad']
    row_names    = ['diet_A', 'diet_B']
    table = pd.DataFrame(diet, columns=column_names, index=row_names)
    table

##figure 5

    from scipy import stats

    chi22, p2, dof, expected = stats.chi2_contingency(diet)
    print (" Pearson's Chi-squared test","\n","\n",
            "Chi-Squared :",round(chi22,4),"\n",
            "df :",dof,"\n",
            "P-Value :", round(p2, 4))




