# https://hyperskill.org/learn/step/6469
# Given a three-digit integer (i.e., an integer from 100 to 999), find the sum of its digits and print the result.

# no loops yet, no functions yet

n = int(input("Enter a three-digit number: "))
s = 0
s += n % 10
n //= 10
s += n % 10
n //= 10
s += n
print(s)