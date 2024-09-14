"""//////////////PONER ENCABEZADO"""

from workshop_classes import ArcadeMachine, GameCatalog, Customer, Utilities

def main():
    machine = ArcadeMachine()
    catalog = GameCatalog()
    utilities = Utilities()
    customer = Customer()
    
    while True:
        print("\n\n-----MENU DE COMPRA DE MAQUINA ARCADE-----\n\n")
        print("-1. Escoger material para la máquina.")
        print("-2. Agregar juego a la máquina.")
        print("-3. Finalizar Compra.")
        print("-4. Salir.")
        
        option = input("Elige una opción: ")
        if not option.isdigit() or int(option) not in range (1, 5):
            print("\n\nError: Por favor ingresa un número entre 1 y 5.")
            input("\n\nPresione enter para continuar...")
            utilities.ClearConsole()
            continue
        
        option = int(option)
        utilities.ClearConsole()
        
        if option == 1:
            
            print("Elige el material")
            print("-Madera")
            print("-Aluminio")
            print("-Fibra de carbono")
            
            material = input("Escribe el material deseado: ")
            while material != "Madera" and material != "Aluminio" and material != "Fibra de carbono":
                print("Has seleccionado una opción invalida, intenta de nuevo.")
                input()
                utilities.ClearConsole()
                print("Elige el material")
                print("-Madera")
                print("-Aluminio")
                print("-Fibra de carbono")
                material = input("Escribe el material deseado: ")
            
            print(f"\n\nEl material escogido fue {material}...")
            machine.SelectMaterial(material)
            input()
            utilities.ClearConsole()
            
        elif option == 2:
            catalog.DisplayGames()
            gameChosen = input("Seleccione el índice de un juego del catálogo (1-17): ")
            while not gameChosen.isdigit() or int(gameChosen) not in range (1, 18):
                print("\n\nError: Por favor ingresa un número entre 1 y 17.")
                input("\n\nPresione enter para continuar...")
                utilities.ClearConsole()
                catalog.DisplayGames()
                gameChosen = input("Seleccione el índice de un juego del catálogo (1-17): ")
                
            gameChosen = int(gameChosen)
                
            machine.AddGame(catalog.FromIndextoGame(gameChosen))
            print(f"Ha sido añadido {catalog.FromIndextoGame(gameChosen)} a la maquina... Presione enter para continuar")
            input()
            utilities.ClearConsole()
            
        elif option == 3:
            print("Para finalizar la compra por favor ingrese su información de contacto: \n\n")
            name = input("Por favor ingrese su nombre completo: ")
            address = input("Por favor ingrese una dirección valida: ")
            customer.UpdateInformation(name, address)
            print(f"Los datos de usuario ingresados son los siguientes:\n\n-Nombre: {customer.name}\n-Dirección: {customer.address}")
            
            finalization = input("¿Desea finalizar la compra? (1.SI / 2.NO): ")
            while not finalization.isdigit() or int(finalization) not in range (1, 3):
                print("\n\nError: Por favor ingresa una opción valida.")
                input("\n\nPresione enter para continuar...")
                utilities.ClearConsole()
                finalization = input("¿Desea finalizar la compra? (1.SI / 2.NO): ")
                
            finalization = int(finalization)
            
            if finalization == 1:
                if machine.material is None:
                    print("¡Por favor ingrese un material de fabricación para su maquina arcade!")
                    input("Presione enter para continuar...")
                    utilities.ClearConsole()
                    continue
                else:
                    print("--¡TU MAQUINA ARCADE HA SIDO ENVIADA A TU DIRECCIÓN CON EXITO!--")
                    print(f"\nEl material de tu máquina arcade es: {machine.material}.\n")
                    print(f"Los juegos añadidos a tu máquina arcade son: ")
                    machine.ShowChosenGames()
                    input("\n\nPresiona enter para continuar...")
                    
                    repeat = input("¿Desea realizar otra compra? (1.SI / 2.NO): ")
                    while not repeat.isdigit() or int(repeat) not in range (1, 3):
                        print("\n\nError: Por favor ingresa una opción valida.")
                        input("\n\nPresione enter para continuar...")
                        utilities.ClearConsole()
                        repeat = input("¿Desea realizar otra compra? (1.SI / 2.NO): ")
                
                    repeat = int(finalization)
                    
                    if repeat == 1:
                        machine = ArcadeMachine()
                        catalog = GameCatalog()
                        customer = Customer()
                        continue
                    else:
                        break
            else:
                utilities.ClearConsole()
                continue
            
        elif option == 4:
            break
                        
if __name__ == "__main__":
    main()