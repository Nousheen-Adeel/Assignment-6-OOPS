# 13. Composition

# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        return "engine started"
    
class Car:
    def __init__(self,engine):
        self.engine =engine

    def engine_start(self):
        print(self.engine.engine_start())
car = Car(Engine)
car.engine_start()
