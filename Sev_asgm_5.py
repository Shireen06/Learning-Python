#counting averages in a loop
count = 0
total = 0
while True:
    snum = input("Enter a number: ")
    if snum == "done":
        break        
    try:
        fnum = float(snum)
    except:
        print("Invalid input")
        continue
    
    count = count + 1
    total = total + fnum
 
if count == 0:
    print("NO input")
else:
    print(total, count, total / count)

    