class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def disp(self):
        print("Hello my name is {} and roll is {}.".format(self.name, self.roll))
ob=student("Ravi", 120)
ob.disp()
