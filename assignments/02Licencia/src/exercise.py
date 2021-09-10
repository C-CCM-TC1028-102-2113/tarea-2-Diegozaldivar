
# Este programa determina si a una persona se  le otorga una licencia de conducir o no


def main():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print(' Primera verifivación pasada con éxito ')
    elif edad <0:
        print(' Respuesta incorrecta ')

    else:
        print(' Licencia denegada ')
    identificacion = str(input( ' Tienes identificaciónoficial? (s/n) ')) ##1. Indicas que conteste con s o n
    if identificacion == "si": ##2. Tienes que usar las mismas letras que definiste en 1
                print('Licencia autorizada')
    elif identificacion == "no": ##2. Tienes que usar las mismas letras que definiste en 1
                        print('Licencia rechazada')
        
        


                         

    

    
    


       
if __name__ == '__main__':
    main()
                         
    
 

