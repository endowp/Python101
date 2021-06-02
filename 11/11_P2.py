import numpy as np
score=[]
n=int(input())
for i in range(n):
    inp = input()
    if i>=3:
        score.append([int(e) for e in inp.split(",")[1:]])
score=np.array(score,float)
for s in score:
    print(sum(s))
        

    
