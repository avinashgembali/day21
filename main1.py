class Animal:
    def __init__(self):
        self.eyes = 2
    def breathe(self):
        print("inhale and exhale.")

class Eagle(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("on the top of sky but in the air")
    def fly(self):
        print("to move in the air")

eagle =Eagle()
eagle.fly()
print(eagle.eyes)
eagle.breathe()