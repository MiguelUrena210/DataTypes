# add
print(123+234)

# subs
print(3-1)

# mult
print(3 * 2)

# division
print(6 / 3) # float type
print(6//3) # int type (returns only the int part)

# power
print(2**3)

# PEMDAS hierarchy
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

# floor and round
bmi = 84 / 1.65 ** 2
print(bmi)

# floor
print(int(bmi))

# round nearest int
print(round(bmi))

# round to 2 decimal
print(round(bmi, 2))

# add and minus value to a previous value
score = 0

# add
score += 1

# minus
score -= 1

# printf
print(f"Your score is = {score}, your bmi is = {bmi}")