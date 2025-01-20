pos1 = float(input())
pos2 = float(input())
pos3 = float(input())

if (pos2 <= pos1 and pos1 <= pos3) or (pos3 <= pos1 and pos1 <= pos2):
    print("Gana Andrea")
elif (pos1 <= pos2 and pos2 <= pos3) or (pos3 <= pos2 and pos2 <= pos1):
    print("Gana Sandra")
elif (pos1 <= pos3 and pos3 <= pos2) or (pos2 <= pos3 and pos3 <= pos1):
    print("Gana Milena")