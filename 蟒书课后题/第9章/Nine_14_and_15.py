'''
    这个源文件, 解决蟒书 9.5 的 9-14 题目
'''

## 9-14：彩票
# 导入库
import random

# 定义彩票数据, 10个数字和5个字母
tickets = [1, 51, 13, 54, 12, 63, 15, 62, 14, 65, 'A', 'C', 'I', 'T', 'K']

# 随机选择一个彩票, 经查询, 可以使用sample方法, 会返回一个列表存储各个随机选出的元素
reward = random.sample(tickets, 4)

# 打印彩票
print("本期彩票为: ", reward)

# 9-15：彩票分析
# 定义一个 my_ticket 列表, 模拟记录自己买彩票的结果
my_ticket = [1, 51, 13, 54, 12, 63, 15, 62, 14, 65, 'A', 'C', 'I', 'T', 'K']

times = 0
while True:
    # 输入自己的购买结果
    times += 1
    my_result = random.choice(my_ticket)
    if my_result in reward:
        print(f'你购买的彩票号码为{my_result}')
        print(f'恭喜你在第{times}次时中奖了！')
        break
    else:
        continue
        
