##예제4
import numpy as np
 a= np.array(range(0,10,1))

 b = np.array(range(9,0,-1))

 c = np.array(0.5,10.5,1)
 print(c)


import numpy as np
a = np.random.randint(0, 100, size=5)

b = np.random.randint(0, 100, size=5)

np.random.seed(1)
c = np.random.randint(0, 100, size=5)

np.random.seed(1)
d = np.random.randint(0, 100, size=5)

print("a :", a)
print("b :", b)
print("c :", c)
print("d :", d)

##표본 평균 저장

import numpy as np
m = []
np.random.seed(1234)
for i in range(100):
    sample=np.random.randint(0, 10, size = 5)
    m.append(np.mean(sample))
m = np.array(m)

print(m)


##히스토그램

import matplotlib.pyplot as plt
plt.hist(m, bins=9)
plt.xlabel('m')
plt.ylabel('Frequency')
plt.title('Historam of m')
plt.show()

#정규 확률 그림
import matplotlib.pyplot as plt
sm.qqplot(m,line='s')
plt.title("Normal Q-Q plot")


##예제4.17
import numpy as np
m = []
for i in range(100):
    np.random.seed(i)
    sample=np.random.poisson(lam = 3, size = 9)
    m.append(np.mean(sample))

m = np.array(m)
print (np.round(m,4))

np.mean(m)
np.std(m)
np.sqrt(3)/3
##히스토그램

import matplotlib.pyplot as plt
plt.hist(m, bins=9)
plt.show()

#정규 확률 그림
import matplotlib.pyplot as plt
sm.qqplot(m,line='s')





