import numpy as np
import math
data = np.array([[15,3.78],
                           [29,2.0],
                           [10,2.5],
                           [25,2.85],
                           [30,3.96]])
logit_pi = []
for i in data:
    logit_pi.append(-3.98 + 0.2*i[0] + 0.5*i[1])
logit_pi=np.array(logit_pi)
p_xi = 1/(1+(math.e**(-logit_pi)))
n = int(input())
if 0>=n or n>len(data):
    print('Error')
elif p_xi[n-1] > 0.5:
    print('True')
else:
    print('False')
