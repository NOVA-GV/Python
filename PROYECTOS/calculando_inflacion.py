#Calcular la inflación de un producto teniendo en cuenta un precio de partida y el precio actual
def calcular_meses_trascurridos(fecha1,fecha2):
    B=0
    j=0
    cont=0
    while B!= 1:
        for j in range(12):
            if fecha1[0]==fecha2[0] and fecha1[1]==fecha2[1]:
                B=1
                break
            else:
                fecha1[0]+=1
                cont+=1
                j+=1
        fecha1[0] = 1
        fecha1[1]+=1
        j=0
    return(cont)

print("\t///CALCULAR INFLACIÓN///")
print('             ')
fecha_compra= [0,0]
fecha_actual= [0,0]

precio_compra= int(input("Ingrese el precio de partida: $"))
fecha_compra[0]= int(input("Ingrese el mes en que compró su producto: "))
fecha_compra[1]= int(input("Ingrese el año en que compró su producto: "))

precio_actual= int(input("Ingrese el precio actual: $"))
fecha_actual[0]= int(input("Ingrese el mes actual: "))
fecha_actual[1]= int(input("Ingrese el año actual: "))
meses_transcurridos= calcular_meses_trascurridos(fecha_compra,fecha_actual)

#print(f"cantidad de meses transcurridos: {meses_transcurridos} meses")
#inflacion= (precio_actual - precio_compra) * 1000 // precio_compra / 10

incremento_total= precio_actual - precio_compra

incremento_mensual= (incremento_total / meses_transcurridos)

porcentaje_incremento_mensual= (incremento_mensual / precio_compra) * 100

inflacion= (precio_actual - precio_compra) * 1000 // precio_compra / 10

incremento_mensual= round(incremento_mensual, 2)
porcentaje_incremento_mensual= round(porcentaje_incremento_mensual, 2)



print('             ')
print(f"- Precio de partida: ${precio_compra}\n-----------")
print(f"- Precio actual: ${precio_actual}\n-----------")
print(f"- Incremento total: ${incremento_total}")
print(f"- Incremento mensual: ${incremento_mensual}")
print(f"- Porcentaje del incremento mensual: %{porcentaje_incremento_mensual}")
print(f"- Inflación: %{inflacion}")
print('             ')