import requests
import inspect

def first_func():
    pass
class Human:
    def __init__(self, age, height, name = "John"):
        self.age = age
        self.name = name
        self.secondname = "Wick"
sig = inspect.signature(Human)
for parameter in sig.parameters.values():
    print(parameter.name, parameter.default)

rq = requests
fn = first_func
nick = Human

print(rq.__name__)
print(fn.__name__)
print(nick.__name__)

intro_list = []
for metod in dir(intro_list):
 print(metod)

class First_class:
    pass

class Second_class(First_class):
    pass

obj_from_class_2 = Second_class()

print(isinstance(obj_from_class_2, First_class))
print(isinstance(obj_from_class_2, Second_class))
print(issubclass(First_class, Second_class))
print(issubclass(Second_class, First_class))
print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))

