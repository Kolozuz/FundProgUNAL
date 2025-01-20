a = float(input())
b = float(input())
c = float(input())

triangle = True if a+b>c and a+c>b and b+c>a else False

if triangle:
    triangle_type = 'equilatero' if a==b and b==c else ''
    triangle_type = 'isosceles' if (a==b and b!=c) or (b==c and c!=a) else triangle_type
    triangle_type = 'escaleno' if (a!=b and b!=c and c!=a) else triangle_type

    print(f"Los lados ingresados conforman un triangulo {triangle_type}")
else:
    print("Los lados ingresados no conforman un triangulo")
