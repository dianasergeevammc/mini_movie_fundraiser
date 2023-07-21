import pandas
import random
from datetime import date


# lists to hold ticket details
# dictionary to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}


mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate the total ticket cost
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                          + mini_movie_frame['Ticket Price']
# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate the ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()


# choose a winner for the name on the list
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# set index in the end(before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')


# ************ get current date and time for heading and filename
# get todays date
today = date.today()

# get day, month, and year as individual settings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")


heading = "Mini Movie Fundraise Ticket Data {}/{}/{} ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# change frame to a string so that we can export it to a file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create strings for printing
ticket_cost_heading = "\n-------ticket cost/profit"
total_ticket_sales = "total ticket sales: ${}".format(total)
total_profit =  "total profit : ${}".format(profit)

# edit text
sales_status = "\n*****all tickets have been sold*****"

winner_heading = "\n---raffle winner---"
winner_text = "the winner of the raffle is {}." \
              "they have won ${}. ie: their ticket is" \
              "free!".format(winner_name, total_won)

# list holding content to print

to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# print output

for item in to_write:
    print(item)

# write output to file
# create file to hold data
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()

