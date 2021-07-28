fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word not in lst:
         lst.append(word)
    #else:
     #continue
        
lst.sort()
print(lst)