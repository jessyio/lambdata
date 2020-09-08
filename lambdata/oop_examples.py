#class = contains methods, container of methods
#using class to make blueprint copies = instantiate an object
import pandas as pd

#pd.DataFrame is the dataframe class: can make children of classes you didn't write
class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]


class BareMinimumClass:
    pass



class Complex:
    def __init__(self): #constructors are methods executed when making a class
        '''constructor for complex numbers
        complex numbers are part real and part imaginary
        imaginary numbers are roots of negative numbers
        '''
        self.r = realpart #self is the object
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i) #return a string



class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvote(self): #upvote in increment of 1
        self.upvotes += 1

    def is_popular(self): #is popular with > 100 upvotes
        return self.upvotes > 100




class Animal:
    #general representation of animals
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return 'Vroom!'

    def eat(self, food):
        return food + ' is delicious, yum!'




class Tiger(Animal): #inherent parent class Animal to create a child class Tiger
    #more specific animal, tigers
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type) #inherit the Animal class
        self.num_stripes = int(num_stripes)

    def run(self):
        #overriding run to be different for tigers
        return 'Scamperwoosh!'

    def say_great(self):
        #method that only exists for tigers
        return "It's great!"




if __name__ == '__main__':
    #demo code when run 'python oop_examples.py'
    #example 0
    b = BareMinimumClass()

    #example 1
    num1 = Complex(3, -5)
    num2 = Complex(-1, 6)
    num1.add(num2) #what should num1 be after?
    print(num1.r, num1.i)

    #example 2
    user1 = SocialMediaUser('erle', 'Jax')
    user2 = SocialMediaUser('John', 'New York', upvotes=50)
    user3 = SocialMediaUser('John Doe', 'Anytown, USA')
    print(user2.is_popular()) #return false
    for _ in range(75):
        user2.receive_upvote()
    print(user2.is_popular()) #return true with 125 upvotes
