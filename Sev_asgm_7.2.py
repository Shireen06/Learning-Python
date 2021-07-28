fname = input("Enter file name: ")
fh = open(fname)

total = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    position = line.find(":")
    number = str(line[position + 1:])
    fnum = float(number)
        
    total = total + fnum
    count = count + 1

average = total/count
print('Average spam confidence:', average)
    
    
  