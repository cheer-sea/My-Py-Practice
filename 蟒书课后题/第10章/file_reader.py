with open('pi_digits.txt') as file:
    contents = file.read()

for line in file:
    print(line.strip())
print(contents)