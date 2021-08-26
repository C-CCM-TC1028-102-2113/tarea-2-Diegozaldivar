#Este programa ordena de manera ascendente tres números enteros



def main():
# Escribe el código adecuado para completar el programa
x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))
z = int(input("Ingresa el tercer número: "))

if((x <= y) and (x <= z)):
       num_menor = x;
       if(y <= z):
              num_medio=y;
              num_mayor=z;
       else:
              medio=numeroz;
              mayor=numeroy;
              
elif((y <= x) and (y < z)):
       num_menor = y;
       if(x <= z):
              num_medio = x;
              num_mayor = z;
       else:
              num_medio = z;
              num_mayor = x
else:
       num_menor = z;

       if(x <= y):
              num_medio = x;
              num_mayor = y;
       else:
              num_medio = y;
              num_mayor = x;
print(str(num_menor),str(num_medio),str(num_mayor));




        


    
            
if __name__ == '__main__':
    main()

