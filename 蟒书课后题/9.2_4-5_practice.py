'''
    这个源文件,解决蟒蛇书9.2的课后练习题
'''

# 9-4: 就餐人数
# 定义餐厅类
class Restaurant:
    """餐厅类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐厅名称和种类"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐厅信息"""
        print(f'餐厅名称：{self.restaurant_name}, 种类：{self.cuisine_type}')

    def open_restaurant(self):
        """打印餐厅营业状态"""
        print(f'欢迎来到{self.restaurant_name}, 正在营业')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increse_number):
        self.number_served += increse_number

# 定义餐馆实例
my_restaurant = Restaurant('千岛湖', '中式')
# 打印初次记录的就餐人数
print(f'初次次记录的就餐人数：{my_restaurant.number_served}')
# 修改就餐人数为 10 人,并打印
my_restaurant.number_served = 10
print(f'第一次修改的就餐人数：{my_restaurant.number_served}')
# 使用类定义的方法修改就餐人数为 15 人,并打印
my_restaurant.set_number_served(15)
print(f'使用类定义的方法修改的就餐人数：{my_restaurant.number_served}')
# 使用类定义的方法增加每天可能的就餐人数 5 人,并打印
my_restaurant.increment_number_served(5)
print(f'使用类定义的方法增加的就餐人数：{my_restaurant.number_served}')


## 9-5: 尝试登录次数
# 定义一个用户类
class User:
    """用户类"""
    def __init__(self, first_name, last_name, age, gender):
        """初始化用户信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    
    def describe_user(self):
        """打印用户信息"""
        message = f'当前用户姓名:{self.first_name}{self.last_name}, 年龄:{self.age}, 性别:{self.gender}'
        print(message)

    def greet_uesr(self):
        """打印用户欢迎信息"""
        greeting = f'你好呀！{self.first_name}用户, 祝你开心每一天！\n'
        print(greeting)

    def increment_login_attempts(self):
        """增加登录次数"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置登录次数"""
        self.login_attempts = 0

# 定义实例
my_user = User('张三', '李四', 25, '男')
# 打印属性
print(f'初始登录次数：{my_user.login_attempts}')
# 多次调用 increment_login_attempts 方法, 这里调用 3 次, 输出结果应为 3
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(f'调用 3 次方法后次数：{my_user.login_attempts}')
# 重置登录次数, 输出结果应为 0
my_user.reset_login_attempts()
print(f'重置后次数：{my_user.login_attempts}')


