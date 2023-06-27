# main routine starts here

# checks if the user has entered yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please enter yes or no")


# checks if response isn't blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this cant be blank. Try again.. ")

        else:
            return response

# main routine

# set max numbers of tickets below


MAX_TICKETS = 3
tickets_sold = 0

# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want the instructions? ")

if want_instructions == "yes":
    print("instructions")

print("program continues...")
print("")

# loop to sell tickets


while tickets_sold < MAX_TICKETS:
    name = not_blank("please enter your name (or 'xxx' to quit): ")

    if name == 'xxx':
        break

    tickets_sold += 1

# output the numbers of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Congrats, you have sold all of the tickets.")
else:
    print("you have sold {} ticket/s. There is {} tickets/s "
          "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
