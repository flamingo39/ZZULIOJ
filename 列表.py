# 需求：3个办公室，8个老师，随机分配到办公室中
import random
# 把老师放到一个数组中
teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# 定义一个新的二维数组
offices = [[], [], []]
# 使用for循环进行数组teachers的遍历
for name in teachers:
    # 随机分配的办公室进行赋值
    offices[random.randint(0, 2)].append(name)
# 打印输出offices数组
print(offices)
