class Animal(object):
    def run(self):
        print('Animal is running....')

    def run_twice(animal):
        animal.run()
        animal.run()


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat ...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')