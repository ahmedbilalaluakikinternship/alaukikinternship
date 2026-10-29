# #while loop

i = 1
while i <= 10:
    print(i)
    i += 1


i = 1
while i <= 30:
    if i % 2 == 0:
        print(i)
    i += 1

i=1

while i >= 1:
    print(i)
    i -= 1


# break , continue and pass
#break
i = 0

while i <=5:
    if( i ==3):
        break
    print(i)

#contnue
i = 0

while i<=7:
    if(i==3):
        i +=1
        continue
    print(i)
    i +=1


#pass

i = 1

while i <= 10:
    pass
