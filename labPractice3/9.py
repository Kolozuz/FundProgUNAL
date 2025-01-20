worked_hours = int(input())
fee_per_hour = int(input())

if worked_hours <= 40:
    payment = fee_per_hour*worked_hours
elif worked_hours <= 48:
    base_payment = fee_per_hour*40
    extra_hours = worked_hours - 40

    payment_for_extra_hours = extra_hours*(fee_per_hour*2)
    payment = base_payment+payment_for_extra_hours

else:
    base_payment = fee_per_hour*40
    base_payment_for_extra_hours = 8*(fee_per_hour*2)

    plus8_hours = worked_hours-48
    payment_for_8plus_hours = plus8_hours*(fee_per_hour*3)

    payment = base_payment+base_payment_for_extra_hours+payment_for_8plus_hours

print(f"El empleado recibira un salario de ${payment}")