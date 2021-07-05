'''
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.

'''
class restaurant:
    #constructor
    def __init__(self, amount):
        self.amount=amount
    #Instance Method
    def totalAmount(self):
        tax=(self.amount)*25/100
        tip=(self.amount)*18/100
        grandTotal=self.amount+tax+tip
        print("Your Grand total amount for your Meal is {} {:.2f}".format("$",grandTotal))

if __name__ == '__main__':
    amount= int(input("Enter your Order Amount: "))
    ob = restaurant(amount)
    ob.totalAmount()








