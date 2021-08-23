def main():
    #escribe tu código abajo de esta línea
    sma= float(input("Dame el saldo del mes anterior: "))
    ingresos=float(input("Dame los ingresos: "))
    egresos=float(input("Dame los egresos: "))
    cheques=float(input("Dame el numero de cheques: "))
    interes=float((sma+ingresos-egresos-(cheques*13))*0.075)
    saldof= float(sma+ingresos-egresos-(cheques*13)-interes)
    print ("El saldo final de la cuenta es: "+ str(saldof))


if __name__ == '__main__':
    main()
