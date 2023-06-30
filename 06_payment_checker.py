# functions go here

def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("please choose a valid payment method.")


# main routine
while True:
    payment_method = cash_credit("choose a payment method(cash or credit?): ")

    if payment_method == "yes":
        print("Instructions go here")

    print("should continue on.")
    print()

