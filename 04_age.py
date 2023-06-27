# checks the age of the user -- will not proceed if the integer is too high or too low
# functions go here
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter a valid age sick ass##le")

# main routine is here


tickets_sold = 0


while True:

    name = input("enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
# if you're too young, the program won't allow you to carry on
    elif age < 12:
        print("you are TOO young to be watching this movie, kid.")
        continue
# if youre too old/ or have an integer as age, program will flame the s##t out of you and won't allow you to carry on
    else:
        print("bruuhhhh thinks they can pass the movie!!!1@ go back to your retirement house")
        continue

    tickets_sold += 1
    print("you have sold {} ticket/s. There is {} tickets/s remaining".format(tickets_sold, tickets_sold))

