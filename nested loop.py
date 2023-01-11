"""number1 = 3
number2 = 3
for x in range(number1):
    for y in range(number2):
        print(f"{x} {y}")"""

numbers = [5, 2, 5, 2, 2]
output = ''
for x_count in numbers:
    #print(output)
    #print(x_count)

    for count in range(x_count):
        output = output + 'X'
    print(output)
"""
n = [5, 2, 5, 5, 2]

for i in n:
    # i += 1
    print(i * "*")"""
