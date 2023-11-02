text = input().split("\\")

name = ""
extension = ""

for item in text:
    data = text[-1].split(".")

    name, extension = data[0], data[1]

print(f"File name: {name}")
print(f"File extension: {extension}")
