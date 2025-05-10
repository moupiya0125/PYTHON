print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_tip = tip/100 * bill
total_bill = (bill + total_tip)/people
print(total_bill)
total = round(total_bill,2)
print(f"Each person has to pay $: {total}")


