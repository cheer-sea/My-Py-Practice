'''
    这个源文件, 解决蟒书 9.5 中的 9-13 题
'''

## 9-13: 骰子
# 导入 random 模块
import random
# 定义骰子类
class Die:
    """骰子类"""
    def __init__(self, sides = 6):
        """初始化骰子类属性"""
        self.sides = sides # sides 默认值为 6

    def roll_die(self):
        """随机返回一个 1 到骰子面数之间的随机数"""
        print(f'本次随机数为: {random.randint(1, self.sides)}, 骰子面数为: {self.sides}')

# 定义一个 6 面骰子实例
d6 = Die()
print(f'当前骰子面数为: {d6.sides}\n')
# 调用 roll_die 方法 10 次
for i in range(10):
    d6.roll_die()

# 定义一个 10 面骰子实例
d10 = Die(10)
print(f'当前骰子面数为: {d10.sides}\n')
# 调用 roll_die 方法 10 次
for i in range(10):
    d10.roll_die()

# 定义一个 20 面骰子实例
d20 = Die(20)
print(f'当前骰子面数为: {d20.sides}\n')
# 调用 roll_die 方法 10 次
for i in range(10):
    d20.roll_die()
