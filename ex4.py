'''
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
'''
#Hint: There are 43,560 square feet in an acre.

class farmer:
    def fieldArea(self,l,w):
        self.l=l
        self.w=w
        return (l*w)
if __name__== "__main__":
    l=int(input("Enter length in feet: "))
    w=int(input("Enter width in feet :"))
    ob=farmer()
    print("There  are {} square feet in an acre".format(ob.fieldArea(l,w)))


