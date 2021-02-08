"""A vaccination calculator."""

#Sherin Stanley = "730404205"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta



total_pop: int = int(input("Population: "))
doses_ad: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_vac: int = int(input("Target percent vaccinated: "))


total_doses_needed: int = round(total_pop * (target_vac / 100) * 2)
doses_left: int = total_doses_needed - doses_ad
days_left: int = round(doses_left / doses_per_day)
time_until_target: timedelta = timedelta(days_left)

today: datetime = datetime.today()
target_date: datetime = today + time_until_target


print("We will reach " + str(target_vac) + "% " + "in " + str(days_left) + " days, which falls on " + target_date.strftime("%B %dth, %Y") + ".")
