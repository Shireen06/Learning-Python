year = int(input("Which year do you want to check? ")) 
# 🚨 Don't change the code above 👆
if year % 400 == 0:
  print("leap year")
elif year % 100 == 0:
  print("not leap year")
elif year % 4 == 0:
  print("leap year")
else:
  print("not leap year")