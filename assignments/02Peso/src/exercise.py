def main():
    #escribe tu código abajo de esta línea
     pesoi=float(input("Dame el peso inicial: "))
    pesof=float(input("Dame el peso final: "))
    cmeses=float(input("Dame la cantidad de meses: "))
    ppmeses=float((pesoi-pesof)/cmeses)
    print ("Lo que debes bajar por mes es: " + str(ppmeses))



if __name__ == '__main__':
    main()
