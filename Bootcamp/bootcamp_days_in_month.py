def is_leap(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False
    
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  #is_leap(year)  
  if is_leap(year) == True:
    return month_days_leap[month-1]
  else:
    return month_days[month-1]

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












