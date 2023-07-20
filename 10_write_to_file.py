

from datetime import date


# get todays date
today = date.today()

# get day, month, and year as individual settings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "the current date is {}/{}/{}".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# heading
print(heading)
print("the filename will be {}.txt".format(filename))