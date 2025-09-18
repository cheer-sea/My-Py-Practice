'''
    这个源文件,解决蟒蛇书9.1的课后练习题
'''

## 9-1: 餐馆
# 定义餐厅类
class Restaurant:
    """餐厅类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐厅名称和种类"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type    

    def describe_restaurant(self):
        """打印餐厅信息"""
        print(f'餐厅名称：{self.restaurant_name}, 种类：{self.cuisine_type}')

    def open_restaurant(self):
        """打印餐厅营业状态"""
        print(f'欢迎来到{self.restaurant_name}, 正在营业')


## 9-2: 三家餐馆
# 实例化餐厅类
res_1 = Restaurant('餐厅1', '日式料理')
res_2 = Restaurant('餐厅2', '西式料理')
res_3 = Restaurant('餐厅3', '韩式料理')

# 调用类方法
res_1.describe_restaurant()
res_2.describe_restaurant()
res_3.describe_restaurant()


## 9-3: 用户
# 定义一个用户类
class User:
    """用户类"""
    def __init__(self, first_name, last_name, age, gender):
        """初始化用户信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        """打印用户信息"""
        message = f'当前用户姓名:{self.first_name}{self.last_name}, 年龄:{self.age}, 性别:{self.gender}'
        print(message)

    def greet_uesr(self):
        """欢迎用户"""
        greeting = f'你好呀！{self.first_name}用户, 祝你开心每一天！\n'
        print(greeting)

u_1 = User('张', '三', 25, '男')
u_2 = User('李', '四', 30, '女')
u_1.describe_user()
u_1.greet_uesr()
u_2.describe_user()
u_2.greet_uesr()

