
# Este programa determina si a una persona se  le otorga una licencia de conducir o no


def main():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print(' Primera verifivación pasada con éxito ')
    elif edad <0:
        print(' Respuesta incorrecta ')

    else:
        print(' Licencia denegada ')
    identificacion = str(input( ' Tienes identificaciónoficial? (s/n) ')
    if identificacion == "si":
                   print('Licencia autorizada')
    elif identificacion == "no":
                        print('Licencia rechazada')
        
        


                         

    

    
    


       
if __name__ == '__main__':
    main()
                         
    
 

