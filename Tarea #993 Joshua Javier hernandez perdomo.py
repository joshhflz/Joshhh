n1 = float(input("Introduce tu primer número: ") )
n2 = float(input("Introduce tu segundo número: ") )

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los numeros elegidos
    5) Convertir de decimal a binario
    6) Convertir de binario a decimal
    7) Cambiar los números elegidos
    8) Apagar calculadora
    
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
    elif opcion == 4:
        print(" ")
        print("RESULTADO: La division de",n1,"//",n2,"es igual a",n1//n2)
    elif opcion == 5:
        # decimal = 10, binario = "", cociente = 10, residuo = 0
        decimal = int(input("\nIngrese un numero decimal: "))
        binario = ""
        cociente = decimal
        residuo = 0
        while cociente > 0:
            residuo = cociente % 2
            binario += str(residuo)
            cociente //= 2
        binario = binario[::-1]
        print(f"\nDecimal: {decimal} -> Binario: {binario}\n")
    elif opcion == 6:
        # binario = 1010, decimal = 10, exponente = 3, cociente = 1, residuo = 1
        binario = int(input("\nIngrese un numero binario: "))
        decimal = 0
        exponente = 0
        cociente = binario
        residuo = 0
        while cociente > 0:
            residuo = cociente % 2
            if(residuo == 1):
                decimal += 2 ** exponente
            exponente += 1
            cociente //= 10
        print(f"\nBinario: {binario} -> Decimal: {decimal}\n")  
    elif opcion == 7:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
    
    elif opcion == 8:
        break
    else:
        print("Opción incorrecta")
