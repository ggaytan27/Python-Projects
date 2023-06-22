#Median
listNum = [40,6,23,24,18,20,15,26,30,35,50,55]
listNum.sort()

if len(listNum) % 2 == 0:
    m1 = listNum[len(listNum)//2]
    m2 = listNum[len(listNum)//2 - 1]
    median = (m1 + m2)/2
else:
    median = listNum[len(listNum)//2]

print("The median is: ", median)