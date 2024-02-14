def identificar_cuadrilatero(lados):
    lados_ordenados = sorted(lados)
    if lados_ordenados[0] == lados_ordenados[3]:
        return "Cuadrado"
    elif lados_ordenados[0] == lados_ordenados[1] and lados_ordenados[2] == lados_ordenados[3]:
        return "Rectángulo"
    else:
        return "Otro cuadrilátero"

def main():
    lados = []
    for i in range(4):
        lado = float(input(f"Ingrese la medida del lado {i+1}: "))
        lados.append(lado)

    tipo = identificar_cuadrilatero(lados)
    print("El cuadrilátero ingresado es:", tipo)

if __name__ == "__main__":
    main()
