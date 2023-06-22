
#main routine starts here
#set max numbers of tickets below
MAX_TICKETS = 3

if want_instructions == "yes":
    print("Instructions go here")


#loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("please enter your name or 'xxx' to quit: ")





    if name == 'xxx':
        break

    tickets_sold += 1

#output the numbers of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Congrats, you have sold all of the tickets.").format(tickets_sold, MAX_TICKETS - tickets_sold)

else:
    print("you have sold {} ticket/s. There is {} tickets/s"" remaining")
