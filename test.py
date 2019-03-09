

class Animal(object):
    hobby = 'girl'

    def run(self):
        print(self.hobby)
        print('running...')

class Dog(Animal):
    hobby = '吃鸡'

    def __init__(self, name):
        self.name = name

liwenzhou = Dog('liwenzhou')
liwenzhou.run()

jinxin =Animal()
jinxin.run()