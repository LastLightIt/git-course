# from tkinter import *

# root = Tk()





# def Hello(event):
#     print('Hello world!')

# btn = Button(root, text='Click me', width=30, height=5, bg='white', fg='black')

# btn.bind('<Button-1>', Hello)
# btn.pack()
# root.mainloop()


# Классы


class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):

        """Инициализируем атрибуты имя и возраст"""
        self.name = name
        self.age = age
        print('Собака создана')


    def sit(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + 'собака села')


    def jump(self):
        """Собака будет перекатываться по команде"""
        print(self.name.title() + ' собака перекатилась')

    
my_dog = Dog('Tolpik', 5)
my_dog_2 = Dog('Reks', 12)

print(my_dog.age)
print(my_dog_2.age)
print(my_dog_2.name)

my_dog.jump()
my_dog_2.jump()