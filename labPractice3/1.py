fee = int(input())
hrs = int(input())
bill = 0

if hrs <= 5:
    base_bill = hrs*fee
    bill = base_bill*0.4
else:
    extra_hrs_bill = (hrs-5)*fee
    base_bill = (5*fee)*0.4
    bill = base_bill+(extra_hrs_bill*1.5)
    
print(f"${round(bill)}")