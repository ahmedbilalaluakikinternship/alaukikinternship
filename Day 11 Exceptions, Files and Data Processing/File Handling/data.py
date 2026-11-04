# f=open("data.txt","r")

# data=f.read()
# print(data)
# print(type(data))
# f.close()


from pathlib import Path

file_path = Path(__file__).parent / "data.txt"

with open(file_path, "r") as file:
    data = file.read()
    print(data)