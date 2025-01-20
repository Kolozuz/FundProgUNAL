# vu_apple = int(input())
# bought_apples = int(input())
# total = 0

# if bought_apples <= 2:
#     total = vu_apple*bought_apples
# elif bought_apples >= 3 and bought_apples <= 5:
#     total_normal = vu_apple*bought_apples
#     total = total_normal*0.9
# elif bought_apples >= 6 and bought_apples <= 10:
#     total_normal = vu_apple*bought_apples
#     total = total_normal*0.85
# elif bought_apples >= 6 and bought_apples <= 10:
#     total_normal = vu_apple*bought_apples
#     total = total_normal*0.85
# elif bought_apples >= 11:
#     total_normal = vu_apple*bought_apples
#     total = total_normal*0.8

# print(f"El total a pagar por el cliente es ${round(total)}")

# extracted_num = int(input())

# if extracted_num < 0:
#     print("Ancheta")
# elif extracted_num == 0:
#     print("Licuadora")
# elif extracted_num >= 0:
#     print("Bicicleta")


# bought_desks = int(input())
# price = 1200000
# total = 0

# if bought_desks < 5:
#     total_normal = price*bought_desks
#     total = total_normal*0.9
# elif bought_desks >= 5 and bought_desks < 10:
#     total_normal = price*bought_desks
#     total = total_normal*0.8
# elif bought_desks >= 10:
#     total_normal = price*bought_desks
#     total = total_normal*0.6

# print(f"El valor a pagar por el cliente es ${round(total, 1)}")

n1 = int(input())
n2 = int(input())
n3 = int(input())

nums = []
fibbon_seq = []

for i in range(-1,n3+1):
    i = i+(i-1)
    fibbon_seq.append(i)

print(fibbon_seq)
if len(nums) == 3:   
    print(f"Los numeros {nums} podrian ser parte de la secuencia de Fibonnacci y el cuarto termino seria 21")
else:
    print("Los numeros no podrian ser parte de la secuencia de Fibonacci")