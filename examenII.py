def print_square(n):
    for i in range(1, n*n + 1):
        print(i, end=' ')
        if i % n == 0:
            print()

n = int(input("Ingrese el numero para generar el cuadrado: "))
print_square(n)

