import numpy as np
def read_square_matrix():
    d = [int(e) for e in input().split()]
    m = [d]
    for k in range(len(d)-1):
        m.append([int(e) for e in input().split()])
    return np.array(m)
def min_in_each_row(m): # หาวิธีเขียนแค่ค าสั่งเดียว
    return np.array([min(r) for r in m])
def max_in_each_column(m): # หาวิธีเขียนแค่ค าสั่งเดียว
    return np.array([max(r) for r in m.T])
def diff_of_sums_of_two_diags(m):# หาวิธีเขียนอย่างมากสองค าสั่ง
    diag1=sum([m[i][i] for i in range(len(m))])
    diag2=sum([m[len(m)-1-i][i] for i in range(len(m))])
    return abs(diag1 - diag2)
def halve(m): # หาวิธีเขียนอย่างมากสองค าสั่ง
    new=[]
    for i in range(m.shape[0]//2):
        subnew=[]
        for j in range(m.shape[1]//2):
            subnew.append(m[2*i][2*j] + m[2*i+1][2*j] + m[2*i][2*j+1] + m[2*i+1][2*j+1])
        new.append(subnew)
    return np.array(new)
exec(input().strip()) # do not remove this line
