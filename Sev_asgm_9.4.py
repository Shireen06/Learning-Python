name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1
#print(counts)
frequency = -1
email = None
for name,count in counts.items():
    if count > frequency:
        frequency = count
        email = name
print(email, frequency)


    
