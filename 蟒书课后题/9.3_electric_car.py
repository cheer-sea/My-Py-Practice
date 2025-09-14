'''
    这个源文件, 创建电动汽车类。我们将会先定义汽车 Car 类, 然后创建电动汽车 ElectricCar 类, 继承 Car 类, 并添加 Battery 类作为电动汽车的电池属性。
'''

# 定义汽车类
class Car:
    """汽车类"""
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.model = model
        self.year = year
        self.make = make

# 定义电池类
class Battery:
    """电池类"""
    def __init__(self, battery_size = 75):
        """初始化电池属性"""
        self.battery_size = battery_size
    
    def upgrade_battery(self):
        """升级电池容量"""
        if self.battery_size < 100:
            self.battery_size = 100 # 升级电池容量, 为 100 kwh

    def get_range(self):
        """获取电池续航里程"""
        if self.battery_size == 75:
            range = 240 # 75 kwh 电池的续航里程为 240 公里
        elif self.battery_size == 100:
            range = 300 # 100 kwh 电池的续航里程为 300 公里

        print(f'这辆车续航里程为 {range} 公里')

# 定义电动汽车类
class ElectricCar(Car):
    """电动汽车类"""
    def __init__(self, make, model, year):
        """初始化电动汽车属性"""
        super().__init__(make, model, year)
        self.battery = Battery() # 默认电池容量为 75 kwh

    def describe_battery(self):
        """打印电池信息"""
        print(f'这辆车电池容量为 {self.battery_size}-kwh')

# 创建电动汽车实例
my_car = ElectricCar('Tesla', 'Model S', 2021)
my_car.battery.get_range() # 第一次里程
my_car.battery.upgrade_battery() # 升级电池容量
my_car.battery.get_range() # 第二次里程
