MONTHS = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

month = MONTHS.index(str(input()))+1
day = int(input())

if (month == 3 and day >= 20) or month == 4 or month == 5 or (month == 6 and day < 21):
    print("Primavera")
elif (month == 6 and day >= 21) or month == 7 or month == 8 or (month == 9 and day < 22):
    print("Verano")
elif (month == 9 and day >= 22) or month == 9 or month == 10 or (month == 12 and day < 21):
    print("Otono")
elif (month == 12 and day >= 21 ) or month == 1 or month == 2 or (month == 3 and day < 20):
    print("Invierno")
