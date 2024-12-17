

class TemplateModel(object):
    def __init__(self):
        variable = 5  # 局部变量，仅在 __init__ 方法内部有效
        self.not_dying_variable = 10  # 实例变量，每个实例独有
        print(variable)  # 打印 5
        print(self.not_dying_variable)  # 打印 10

    def print_values(self):
        print(f'{self.not_dying_variable}')



# 创建 TemplateModel 的第一个实例
my_class_instance = TemplateModel(5)

my_class_instance.print_values()

print(f'the value is : {my_class_instance.not_dying_variable}')
# print(f'the value of variable is : {my_class_instance.variable}')  # 如果取消注释，这行代码会报错，因为 variable 不是实例的属性

# 创建 TemplateModel 的第二个实例
my_second_instance = TemplateModel()
my_second_instance.not_dying_variable = 20  # 修改 my_second_instance 的实例变量

# 分别打印两个实例的 `not_dying_variable` 的值
print(f'the value in first is : {my_class_instance.not_dying_variable}')  # 应该打印 10
print(f'the value in second is : {my_second_instance.not_dying_variable}')  # 应该打印 20

# 打印两个实例的类型
print(type(my_class_instance))  # 应该打印 <class '__main__.TemplateModel'>
print(type(my_second_instance))  # 应该打印 <class '__main__.TemplateModel'>

my_integer = int()
print(my_integer)
