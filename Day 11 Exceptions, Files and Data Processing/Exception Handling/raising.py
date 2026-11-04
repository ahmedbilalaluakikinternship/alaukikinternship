def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(5)
except ValueError as e:
    print(e)

else:
    print("Age are valid")

finally:
    print("i dont care i will run eveytime")

