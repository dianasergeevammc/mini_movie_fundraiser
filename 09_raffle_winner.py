
import pandas
import random

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

# choose a winner for the name on the list

winner_name = random.choice(all_names)

# choose position of winner name on the list
win_index = all_names.index(winner_name)

# total count up
total_won = mini_movie_frame.at[win_index, 'total']

# set index in the end
mini_movie_frame = mini_movie_frame.set_index('name')
print(mini_movie_frame)


print()
print('---raffle winner---')
print("Congrats, {}. You have won ${} ie: your ticket is free!".format(winner_name, total_won))

