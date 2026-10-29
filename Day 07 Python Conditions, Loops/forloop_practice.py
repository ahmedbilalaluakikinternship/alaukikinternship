# for loop practice 

# find the sum of a number n

n = int(input("Enter Your number: "))
sum = 0

for sum in range(n,n+1):
    sum +=1
    print(sum)



# factorial of a number

n = 5
fact=1

for i in range(n,n+1):
    fact *=i
    print(fact)


# search a number in a tuple

tup= (3,4,5,6,7,8,9,11,12,13,14,15)

x=12

for num in tup:
    if num == x:
        print("X is finded")
        break
else:
        print("Finding")
