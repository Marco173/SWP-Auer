import numpy as np

Lottonumber = np.arange(1,46)

def Lotto_Ziehung(startValue,endValue):
    for x in range(6):
        drawing = np.random.randint(startValue,endValue,1)
        Lottonumber[drawing], Lottonumber[endValue] = Lottonumber[endValue], Lottonumber[drawing]

        endValue = endValue - 1

statistic_dic = {}
for x in range(45):
    statistic_dic[x+1] = 0

for e in range(1000):
    Lotto_Ziehung(0,44)
    numbers = Lottonumber[39:]
    print(numbers)
    for i in numbers:
        statistic_dic[i] += 1


print(statistic_dic) 