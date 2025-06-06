print("Welcome to the tip calculator!")
bill =  float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? "))
number_people = int(input("How many people to split the bill? "))

total_bill = bill * (1+tip/100)
each_one_bill = round(total_bill / number_people , 2)

print(f"Each person should pay: ${each_one_bill}")
