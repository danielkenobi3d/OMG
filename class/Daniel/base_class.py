

class TemplateModel(object):
    def __init__(self, value):
        variable=5
        self.not_dying_variable = value

    def print_values(self):
        print(f'{self.not_dying_variable=}')



class NewClass(TemplateModel):
    def __init__(self):
        super(NewClass, self).__init__(6)
        self.age = 24


my_instance = NewClass()
print(my_instance.age)
print(my_instance.not_dying_variable)
my_instance.print_values()

"""
        


my_class_instance = TemplateModel(5)

my_class_instance.print_values()

print(f'the value is  : {my_class_instance.not_dying_variable}')
# print(f'the value of variable is  : {my_class_instance.variable}')

my_second_instance = TemplateModel()
my_second_instance.not_dying_variable = 20

print(f'the value in first is  : {my_class_instance.not_dying_variable}')
print(f'the value in second is  : {my_second_instance.not_dying_variable}')
print(type(my_class_instance))
print(type(my_second_instance))
my_integer = int()
print(my_integer)
"""

