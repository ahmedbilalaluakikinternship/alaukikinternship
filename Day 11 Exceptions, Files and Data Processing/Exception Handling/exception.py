# try:
#     # Risky code

# except:
#     # Error handling

# else:
#     # Runs when no error occurs

# finally:
#     # Always executes




n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")



n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")

else:
    print("there is no exception")

finally:
    print("i will run ! no matter exception occurs")


try:
    res = "100" / 20 
    
except ArithmeticError:
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")