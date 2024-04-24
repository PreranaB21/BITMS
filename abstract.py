from abc import ABC, abstractmethod
class Car(ABC):
    def milage(self):
        pass
    def bitm(self):
        print('Non abstract method')
class Tesla(Car):
    def milage(self):
        print("Milage is 60kmp")
t=Tesla()
t.milage()