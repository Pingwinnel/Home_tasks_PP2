import random

germany=['g',]*4
italy=['i',]*6
russia=['r',]*7
china=['c',]*5
que=china.copy()
que.extend(russia)
que.extend(italy)
que.extend(germany)

favEvent = 0
totalVariants = 1000000
for N in range(totalVariants):
    random.shuffle(que)
    if que[:3].count('i') > 0:
        favEvent +=1
print(f'probability = {favEvent/totalVariants}')