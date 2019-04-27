


#Ingreso de Renta


#Crear concepto de Gasto



listagastos = []
listconcepto = {}

seguir = input("Quieres crear un concepto de gasto [SI/NO]:")
seguir.lower()
while seguir != "no":
    concepto = input("Ingresa concepto de gasto:")
    listagastos.append(concepto)


    while seguir != "no":
        motivo = input("Ingresa el motivo del gasto:")
        costo =int(input("Ingresa costo del gasto:"))
        listconcepto[motivo] = costo
        seguir = input("Quieres continuar ingresando mas gastos para este comcepto?[SI/NO]:")


    seguir = input("Quieres crear un otro concepto de gasto [SI/NO]:")
    listconcepto2 = {}

print(listagastos)
print(listconcepto,listconcepto2)


print(".......................................................")