import string
with open('/home/drake/Downloads/1000.txt', 'r') as file:
    for line in file:
        for n in line.split():
            print(n)

