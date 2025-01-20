account_balance = int(input())
expenses = int(input())

print(f"Te quedan {account_balance+expenses} de tus {account_balance}")

if account_balance+expenses >= 0:
    print(f"Si llegas a fin de mes")
else:
    print(f"No llegas a fin de mes")
    