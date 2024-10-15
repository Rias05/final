import re
def parser_matriz(path):
    try:
        lista = []
        with open(path,"r",encoding="utf-8") as archivo :
            for  linea in archivo:
                registro = re.split(";|\n",linea.strip())
                lista.append(registro)
                

        return lista
    except:
        print("erorr al leer archivo")
sd = parser_matriz("data_final_20241015.csv")



for i in range(len(sd)):
    for j in range(len(sd[0])):
     sd[i][j]= int(sd[i][j])
       
    #  print(sd[i][j],end= " ")
# print(" ")    
# print(sd)   

def suma_diagonales(matriz):
    suma_principal = 0
    suma_secundaria = 0
    # Tu código aquí
    for i in range(len(matriz[0])):
        for j in range(len(matriz[0])):
            if i == j:
                suma_principal+= matriz [i][j]
    return suma_principal, suma_secundaria
def determinar_diagonal2(matriz:list):
    diagonal2 = " "# str
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i+j == len( matriz[0])-1:
                diagonal2 += matriz[i][j]
    return diagonal2
# remove
def contar_secuendcias( matriz) :
    contador=0
    secuencias = []
    n= len( matriz[0])
    acumulador = 0
    # for i in range(len(matriz)):
    #     for j in range(len(matriz[0])):
    #         acumulador += matriz[i][j]
    
    for i in range(2,n+1):
        for j in range(n-i+1):
            secuencia = sd[j:j+i ]
    suma =(sum(secuencia))
    print(suma)
  
            

    #     if acumulador == 8:
    #         lista.append(i)
    

contar_secuendcias(sd)

      