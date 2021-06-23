'''
Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
'''
class RoomArea:
    def area(self,w,l):
        self.w=w
        self.l=l
        return (w*l)
if __name__ == "__main__":
    l=int(raw_input("Enter the length in meters :"))
    w =int(raw_input("Enter the width in meters :"))
    ob=RoomArea()
    print("Area of Room in meters is :{}".format(ob.area(l,w)))