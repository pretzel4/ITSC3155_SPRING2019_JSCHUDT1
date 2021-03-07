ar = [12, 13, 14, 17, 11, 2, 3, 1]
ar2 = [-43,-12,-39,-18,-21,-15,11,-7]
re = 0
for i in range(len(ar)):
    re += ar2[i] * ar2[i]
print(re)