import system
from java.util import Calendar

# Calculate yesterday's date
calendar = Calendar.getInstance()
calendar.add(Calendar.DATE, -1)
yesterday = calendar.getTime()

# Set the start date to August 14, 2023
startCalendar = Calendar.getInstance()
startCalendar.set(2023, Calendar.AUGUST, 14)  # Calendar.AUGUST is equivalent to 7

while startCalendar.getTimeInMillis() <= yesterday.getTime():
    print(startCalendar.getTime())
    startCalendar.add(Calendar.DATE, 1)
