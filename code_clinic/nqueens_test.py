# getting all fields where Queen can beat
n = 8
c = list(range(n))
print(c)
fin = []
for i in c:
    var = []
    for m in c:
        var.append((i,m))
    fin.append(var)

print(len(fin))
x, y = 4, 0
su = x+y
mi = x-y

for i in range(n):
    for f in range(n):
        xpos = fin[i][f][0]
        ypos = fin[i][f][1]
        if (xpos+ypos == su or 
           xpos-ypos == mi or 
           xpos == x or 
           ypos == y):
            fin[i][f] = (9,9)

for i in range(n):
    print(fin[i])

