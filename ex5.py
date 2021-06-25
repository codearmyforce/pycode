'''
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.

'''
class drink:
    #Instance mathod
    def refund(self, containers,size):
        self.containers=containers
        self.size=size

        #calculating refurnd amount
        if size <= 1:
            total=float(self.containers*0.10)
            print("You will be receive {} {:.2f} of amount for the containers. ".format("$",total))
        elif size >= 1:
            total=float(self.containers*0.25)
            print("You will be receive {} {:.2f} of amount for the containers. ".format("$",total))

if __name__ == "__main__":
    containers=int(input("How Many containers you have? "))
    size=float(input("What is capacity of containers in leters? "))
    ob=drink()
    ob.refund(containers,size)


