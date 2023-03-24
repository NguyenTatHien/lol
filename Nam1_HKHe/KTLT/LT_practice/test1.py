class ClassName:
    """This is a docstring. I have created a new class"""
    attr = 0
    def func(self):
        print("Hallo!")

        
print(ClassName.__doc__)
print(ClassName.attr)
print(ClassName.func)