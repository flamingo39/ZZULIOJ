factorial = 1
j = 1
y_1 = 0
y_2 = 0
x = int(input())
# 计算算式中的正值
for i in range(1, 20, 4):  # 1,5,9,13,17
    while j <= i:
        factorial = factorial * j  # 一到i的阶乘
        j += 1
    sum_1 = x**i / factorial
    factorial = 1  # 使阶乘归一,不使其累乘
    j = 1  # 使j归一,使阶乘从一开始
    y_1 += sum_1
# 计算算式中的负值
for i in range(3, 20, 4):  # 3,7,11,15,19
    while j <= i:
        factorial = factorial * j  # 一到i的阶乘
        j += 1
    sum_2 = x**i / factorial
    factorial = 1  # 使阶乘归一,不使其累乘
    j = 1  # 使j归一,使阶乘从一开始
    y_2 += sum_2
y = y_1 - y_2
print('%.3f' % y, end='')
