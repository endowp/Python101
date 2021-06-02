import numpy as np
def read_height_weight():
    list_hw = []
    for k in range(int(input())) :
        h,w = input().split()
        list_hw.append((int(h),int(w)))
    return np.array(list_hw)
def cm_to_m(x):
    return x/100
def cal_bmi(hw):
    calculated=[]
    for h,w in hw:
        calculated.append( w/ (cm_to_m(h)**2) )
    return np.array(calculated)
def main():
    hw = read_height_weight()
    bmi = cal_bmi(hw)
    avg_bmi = sum(cal_bmi(hw))/len(hw)
    count_underweight = sum(cal_bmi(hw)<18.5)
    print('average bmi =', avg_bmi)
    print('#bmi < 18.5 =', count_underweight)
exec(input().strip())
