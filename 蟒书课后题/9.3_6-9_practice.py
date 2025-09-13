'''
    这个源文件, 解决蟒书9.3的课后练习题
'''

## 9-6: 冰淇淋小店
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

# 定义冰淇淋小店类, 它继承 Restaurant 类        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def demonstrate_flavors(self):
        """展示冰淇淋的风味"""
        print(f'本店有{len(self.flavors)}种风味冰淇淋, 如下：')
        for flavor in self.flavors:
            print(flavor)
        print() # 进行换行

# 创建冰淇淋小店实例
my_flavors = ['草莓', '香草', '荔枝']
my_ice_cream_stand = IceCreamStand('冰淇淋小店', '冰淇淋', my_flavors)
# 显示冰淇淋口味
my_ice_cream_stand.demonstrate_flavors()


## 9-7: 管理员
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

# 定义 Admin 类, 继承 User 类
# 下面这个 Privileges 类是为了实现 9-8 题目的, 9-7 题目没有使用, 当要尝试 9-8 题目时, 则需要取消注释
# class Privileges:
#     """权限类"""
#     def __init__(self, privileges):
#         """初始化权限"""
#         self.privileges = privileges

#     def show_privileges(self):
#         """显示权限"""
#         print(f'该管理员权限如下：{self.privileges}')

# 定义管理员类, 继承 User 类
class Admin(User):
    """管理员类"""
    def __init__(self, first_name, last_name, age, gender, privileges):
        """初始化管理员信息"""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        """显示管理员权限"""
        print(f'管理员 {self.first_name} {self.last_name} 的权限如下：{self.privileges}')

# 创建管理员实例1
my_admin1 = Admin('Zhang', 'san', 30, '男', "can add post")
# 显示管理员权限
my_admin1.show_privileges()


## 9-8: 权限
# 该题目与 9-7 题目有前后关联, 需要为 9-7 的 Admin 类添加权限属性, 并且该属性是一个类(Privileges)的实例
# 定义 Privileges 类, 当要尝试 9-8 题目时, 请在 9-7 题目中取消下面对应内容注释
# class Privileges:
#     """权限类"""
#     def __init__(self, privileges):
#         """初始化权限"""
#         self.privileges = privileges

#     def show_privileges(self):
#         """显示权限"""
#         print(f'管理员权限如下：{self.privileges}')

# 创建管理员实例2
my_admin2 = Admin('Cui', 'hua', 35, '女', "can delete post")
# 显示管理员权限
my_admin2.privileges.show_privileges()



