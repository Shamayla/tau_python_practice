# For Loop
# While Loop
# Loop Controls:
    # - break, continue, pass

# For Loop
fruits = ["oranges", "apples", "banana", "pomegrant", "grapes", "mangoes"]
for fruit in fruits:
    print(f"Do you like {fruit}?")

# While Loop
set_temp = 40
while set_temp > 32:
    print(f"The water is {set_temp} degrees")
    set_temp -= 1

# Loop Control
# break
set_temp = 40
while set_temp > 32:
    print(f"The water is {set_temp} degrees")
    set_temp -= 1
    if set_temp == 33:
        break

# continue
for number in range(1, 11):
    if number == 7:
        print(f"We are skipping {number}")
        continue
    print(f"The number is: {number}")

# pass - means do nothing or skips over unimplemented part of code
for number in range(1, 11):
    if number == 3:
        pass
    else:
        print(f"The number is {number}")