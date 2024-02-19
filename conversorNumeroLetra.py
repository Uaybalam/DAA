def num_a_letras(numero):
    def unidad(num):
        unidades = ("cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve")
        return unidades[num]

    def decenas(num):
        decena = (num // 10) * 10
        unidad_num = num % 10
        if num < 10:
            return unidad(num)
        elif 10 <= num <= 15 or num == 20:
            return {10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince", 20: "veinte"}[num]
        elif 16 <= num <= 19:
            return "dieci" + unidad(unidad_num)
        elif 21 <= num <= 29:
            return "veinti" + unidad(unidad_num)
        else:
            decenas = {30: "treinta", 40: "cuarenta", 50: "cincuenta", 60: "sesenta", 70: "setenta", 80: "ochenta", 90: "noventa"}
            texto_decena = decenas[decena]
            return texto_decena if unidad_num == 0 else texto_decena + " y " + unidad(unidad_num)

    def centenas(num):
        if num < 100:
            return decenas(num)
        elif 100 <= num <= 199:
            return "ciento " + decenas(num % 100) if num != 100 else "cien"
        else:
            centena = (num // 100) * 100
            centenas = {200: "doscientos", 300: "trescientos", 400: "cuatrocientos", 500: "quinientos",
                        600: "seiscientos", 700: "setecientos", 800: "ochocientos", 900: "novecientos"}
            return centenas[centena] + (" " + decenas(num % 100) if num % 100 != 0 else "")

    def miles(num):
        if num < 1000:
            return centenas(num)
        elif 1000 <= num <= 1999:
            return "mil " + centenas(num % 1000) if num != 1000 else "mil"
        else:
            mil = num // 1000
            return num_a_letras(mil) + " mil" + (" " + centenas(num % 1000) if num % 1000 != 0 else "")

    def millones(num):
        if num < 1000000:
            return miles(num)
        elif 1000000 <= num <= 1999999:
            return "un millón " + miles(num % 1000000) if num != 1000000 else "un millón"
        else:
            millon = num // 1000000
            return num_a_letras(millon) + " millones" + (" " + miles(num % 1000000) if num % 1000000 != 0 else "")

    def billones(num):
        if num < 1000000000000:
            return millones(num)
        elif 1000000000000 <= num <= 1999999999999:
            return "un billón " + millones(num % 1000000000000) if num != 1000000000000 else "un billón"
        else:
            billon = num // 1000000000000
            return num_a_letras(billon) + " billones" + (" " + millones(num % 1000000000000) if num % 1000000000000 != 0 else "")

    def trillones(num):
        if num < 1000000000000000:
            return billones(num)
        else:
            return "un trillón"  # Máximo soportado

    return trillones(numero)

# Prueba
print(num_a_letras(1234567890120000000000000))