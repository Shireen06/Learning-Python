#Write a program to read through the mbox-short.txt 
#and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then 
#splitting the string a second time using a colon.
#Once you have accumulated the counts for each hour, print out the counts, 
#sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
       
        time = words[5].split(':')
        counts[time[0]] = counts.get(time[0], 0) + 1
        #print(sorted( [ (h, f) for h, f in counts.items() ] ) )

list = sorted(counts.items())
for hour, fr in list :
    print(hour, fr)