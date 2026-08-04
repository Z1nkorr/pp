# file = open("test.txt","w")

# a = 111

# file.write(f"{a}\n")
# file.write(str(111) + "\n")

# file.close()

file = open("test.txt","r")

file_lines = file.read()

file.close()

print(file_lines)

file = open("test.txt", "w")

file.writelines(file_lines)

file.close()

all_lines = []

with open("test.txt", "r", encoding="utf-8") as file:
    all_lines = file.readlines()

print(len(all_lines))
