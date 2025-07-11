class Animal:
    def legs(self):
        print("I have four legs")

    def fur(self):
        print("My body is covered with fur")

class Dog(Animal):
    def bark(self):
        print("The dog barks")

class Cat(Animal):
    def meow(self):
        print("Thr cat meaws")

class cow(Animal):
    def moo(self):
        print("The cow moos")
d = Dog()
d.bark()
d.legs()
d.fur()
c= Cat()
c.meow()
c.legs()
c.fur()
co = cow()
co.moo()
co.legs()
co.fur()    


    
    