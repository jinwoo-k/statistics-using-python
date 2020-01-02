
import numpy as np

height = np.array([181,161,170,160,158,168,162,179,183,178,171,177,163,158,160,160,158,
                   173,160,163,167,165,163,173,178,170,167,177,175,169,152,158,160,160,
                   159,180,169,162,178,173,173,171,171,170,160,167,168,166,164,173,180])

weight = np.array([78,49,52,53,50,57,53,54,71,73,55,73,51,53,65,48,59,
                   64,48,53,78,45,56,70,68,59,55,64,59,55,38,45,50,46,
                   50,63,71,52,74,52,61,65,68,57,47,48,58,59,55,74,74])

#calculate the correlation

import numpy as np
np.corrcoef(height,weight)[0][1]


#draw the scatter plot


import matplotlib.pyplot as plt

plt.figure()
plt.scatter(height, weight, color ='black')
plt.xlabel('height(cm)')
plt.ylabel('weight(kg)')
plt.title('height(cm) and weight(kg)')
plt.show()

