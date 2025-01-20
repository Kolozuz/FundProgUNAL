amount = int(input()) 

denominations = [50000, 20000, 10000, 5000, 2000, 1000]
result = {}

for bill in denominations:
    if amount >= bill:
        num_bills = amount // bill
        amount %= bill
        result[bill] = num_bills
    
for bill, count in result.items():
    print(f"{count} de ${bill}")
