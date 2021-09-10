# Este programa ayuda a determina el IMC


def main():
    # Escribe el código adecuado para completar el programa
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    IMC = peso / altura**2  ##olvidaste verificar que no fueran 0
    if IMC < 20:
        print(' PESO BAJO ')
    if IMC <= 20 and IMC < 25:
        print(' PESO NORMAL ')
    if IMC <=25 and  IMC < 30:
        print(' SOBREPESO ')
    if IMC <= 30 and IMC < 40:
        print(' OBESIDAD ')
    if IMC >= 40:
        print(' OBESIDAD MORBIDA ')
    






if __name__ == '__main__':
    main()
