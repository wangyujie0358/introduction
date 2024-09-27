n = 6
fish = [-4, -3, -1, -5, -1, -2]
# max
maxx = fish[0]
for i in range(n):
    if fish[i] > maxx:
        maxx = fish[i]
print(maxx)

# 判断target在不在list里面，在的话打印yes，不在打印no
# yes或者no只可以打印一次
# target = -10
# exist = False
# for i in range(n):
#     if fish[i] == target:
#         exist = True
# if exist:
#     print("yes")
# else:
#     print("no")

# 有没有两个数字加在一起等于target，不允许自己加自己，有yes，没有no
target = -10
exist = False
for i in range(n):
    for j in range(i + 1, n):
        print(fish[i], fish[j])
        if fish[i] + fish[j] == target:
            exist = True
if exist:
    print("yes")
else:
    print("no")
