#Felipe S Y Cristopher O ..
def ingresar_dispositivos():
  
    
    dispositivos = {
        "Router 1801": 0,
        "Router 2901": 0,
        "Router 2911": 0,
        "Router 4321": 0,
        "Router 4331": 0,
        "Switch 2960": 0,
        "Switch 3550": 0,
        "Switch 3560": 0,
        "Switch 9200": 0,
        "Access Point Serie Catalyst 9100": 0,
        "Access Point Serie Catalyst 9800": 0,
        "Access Point Serie Catalyst 4800": 0,
        "Controladora Wireless Cisco 3504": 0
    }

    print("Bienvenido al sistema de registro de dispositivos de red.")
    print(S"Por favor, ingrese las cantidades de dispositivos para cada tipo.")

    while True:
        for dispositivo in dispositivos:
            while True:
                try:
                    cantidad = int(input(f"¿Cuántos {dispositivo} hay en la empresa? (Ingrese un número): "))
                    if cantidad < 0:
                        print("Por favor, ingrese un número positivo.")
                    else:
                        dispositivos[dispositivo] += cantidad
                        break
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.")

        print("\nResumen de Dispositivos registrados:")
        for dispositivo, cantidad in dispositivos.items():
            print(f"{dispositivo}: {cantidad}")

        salir = input("\n¿Desea continuar agregando dispositivos? (Ingrese 'S' para continuar o 'Salir' para finalizar): ").strip().lower()

        if salir == 'salir' or salir == 's':
            print("\nProceso finalizado. Aquí está el informe final:")
            for dispositivo, cantidad in dispositivos.items():
                print(f"{dispositivo}: {cantidad}")
            break
        else:
            print("\nContinuando con la entrada de más dispositivos...\n")


if __name__ == "__main__":
    ingresar_dispositivos()
