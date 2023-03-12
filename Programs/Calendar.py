import calendar

# Taking year & month input from the user

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

print("Calendar of the month for particular year you had asked for is given below"
      +"\n"

      +calendar.month(yy, mm))