var1 = str(input())
val1 = float(input())

var2 = str(input())
val2 = float(input())

var_names = ['V','D','T'] 

var_names.remove(var1)
var_names.remove(var2)

var_to_calculate = var_names[0]
result = str()

if var_to_calculate == 'V':
    result = val1/val2
elif var_to_calculate == 'T':
    result = val2/val1
elif var_to_calculate == 'D' :
    result = val1*val2

print(f"{var_to_calculate} = {round(result, 1)}")