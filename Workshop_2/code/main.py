"""This module This file is responsible for correctly executing the logic of the arcade machine seller program.

Author: Maiker Alejandro Hernández <mahernandeza@udistrital.edu.co>
        Joan Sebastián Durán Pradilla <Jsduranp@udistrital.edu.co>
        
this file is part of Workshops.

Arcade Machine Seller is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either versio 3 of the License, or (at your opinion) any later version.

Arcade Machine Seller is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY... ; without even the implied warranty 
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>."""

from Workshop_classes import ArcadeMachine, GameCatalog, Customer, Utilities, DanceRevolutionMachine, ClassicalArcadeMachine, ShottingMachine, RacingMachine, VirtualRealityMachine

class main():
    
    """This class represents the main behavior of the application."""
    
    MENU_CHOOSE_MACHINE = "\n\n-----WELCOME! CHOOSE A PREDERTERMINATED ARCADE MACHINE!!-----\n\n\n-1. Dance Revolution Machine.\n-2. Classical Arcade Machine.\n-3. Shotting Machine.\n-4. Racing Machine.\n-5. Virtual Reality Machine.\n-6. Exit."
    MENU_DANCE_REVOLUTION_MACHINE = "\n\n-----DANCE REVOLUTION MACHINE MENU-----\n\n\n-1. Choose material.\n-2. Add/Quit game.\n-3. Add/Quit accessories.\n-4. Set memory.\n-5. Set number of processors.\n-6. Set number of difficulties.\n-7. Set number of arrow cardinalities.\n-8. Finish purchase.\n-9. Exit."
    MENU_CLASSICAL_ARCADE_MACHINE = "\n\n-----CLASSICAL ARCADE MACHINE MENU-----\n\n\n-1. Choose material.\n-2. Add/Quit game.\n-3. Add/Quit accessories.\n-4. Set memory.\n-5. Set number of processors.\n-6. Set vibration.\n-7. Set sound record alert.\n-8. Finish purchase.\n-9. Exit."
    MENU_SHOTTING_MACHINE = "\n\n-----SHOTTING MACHINE MENU-----\n\n\n-1. Choose material.\n-2. Add/Quit game.\n-3. Add/Quit accessories.\n-4. Set memory\n-5. Set number of processors\n-6. Set guns number.\n-7. Set guns type.\n-8. Finish purchase.\n-9. Exit."
    MENU_RACING_MACHINE = "\n\n-----RACING MACHINE MENU-----\n\n\n-1. Choose material.\n-2. Add/Quit game.\n-3. Add/Quit accessories.\n-4. Set memory\n-5. Set number of processors\n-6. Set steering wheel type.\n-7. Finish purchase.\n-8. Exit."
    MENU_VIRTUAL_REALITY_MACHINE = "\n\n-----VIRTUAL REALITY MACHINE MENU-----\n\n\n-1. Choose material.\n-2. Add/Quit game.\n-3. Add/Quit accessories.\n-4. Set memory\n-5. Set number of processors\n-6. Set glass type\n-7. Set glass resolution\n-8. Finish purchase.\n-9. Exit."
    
    def choose_predeterminated_machine_menu(self):
        """This method displays the menu to choose a predeterminated arcade machine."""
        print(MENU_CHOOSE_MACHINE)
        
    def show_menu(self):
        """This method displays the menu according to the predeterminated arcade machine chosen."""
        if isinstance(self.machine, DanceRevolutionMachine):
            print(MENU_DANCE_REVOLUTION_MACHINE)
        elif isinstance(self.machine, ClassicalArcadeMachine):
            print(MENU_CLASSICAL_ARCADE_MACHINE)
        elif isinstance(self.machine, ShottingMachine):
            print(MENU_SHOTTING_MACHINE)
        elif isinstance(self.machine, RacingMachine):
            print(MENU_RACING_MACHINE)
        elif isinstance(self.machine, VirtualRealityMachine):
            print(MENU_VIRTUAL_REALITY_MACHINE)
        
    def handle_menu(self, option:int):
        if option == 1:
            print("Choose the material:\n\n-Wood.\n-Aluminium.\n-Carbon fiber.")
            material = input("Enter the desired material: ")
            
            while material != "Wood" and material != "Aluminium" and material != "Carbon fiber":
                print("You have selected an invalid option, please try again.")
                input()
                utilities.ClearConsole()
                
                print("Choose the material:\n\n-Wood.\n-Aluminium.\n-Carbon fiber.")
                material = input("Enter the desired material: ")
            
            self.machine.SelectMaterial(material)
            print(f"\n\nThe chosen material was {material}...")
            input()
            utilities.ClearConsole()
            
        elif option == 2:
            print("Choose a game from the catalog:\n\n")
            catalog.SetGames(self.machine)
            catalog.DisplayGames()
            numberofgames = catalog.GetNumberOfGames()
            gamechosen = input(f"Choose the index of a game from the catalog: ")
            while not gameChosen.isdigit() or int(gameChosen) not in range (1, numberofgames + 1):
                print("\n\nError: Please enter a valid number.")
                input("\n\nPress enter to continue...")
                utilities.ClearConsole()
                catalog.DisplayGames()
                gameChosen = input("Select the index of a game from the catalog: ")
                
            gameChosen = int(gameChosen) #Parse the input to an integer
            machine.AddGame(catalog.FromIndextoGame(gameChosen)) # Add the selected game to the machine
            print(f"{catalog.FromIndextoGame(gameChosen)} has been added to the machine... Press enter to continue")
            input()
            utilities.ClearConsole()
            
        elif option == 3:
            print("Manage additional accessories:\n-1- Add accessory.\n-2- Remove accessory.\n-3- Show accessories.\n-4- Return to main menu.")
            accessoryOption = input("Choose an option: ") #COMPLETAR LOGICA...
            
        elif option == 4:
            print("Choose the memory for the arcade machine:\n\n-1. 250GB.\n-2. 500GB.\n-3. 1TB.")
            self.machine.SetMemory(input("Enter the desired memory: "))
            
        elif option == 5:
            print("Choose the number of processors for the arcade machine:\n\n-1. 1.\n-2. 2.\n-3. 4.")
            self.machine.SetNumberOfProcessors(input("Enter the desired number of processors: "))
        
        
def run():
    # Create instances of necessary classes
    machine = ArcadeMachine()
    catalog = GameCatalog()
    utilities = Utilities()
    customer = Customer()
    
    while True:
        # Display the main menu options
        print("\n\n-----MENU DE COMPRA DE MAQUINA ARCADE-----\n\n")
        print("-1. Escoger material para la máquina.")
        print("-2. Agregar juego a la máquina.")
        print("-3. Gestionar accesorios adicionales.")
        print("-4. Finalizar Compra.")
        print("-5. Salir.")
        
        # Get user input for menu option and validate that the option is a number between 1 and 5
        option = input("Elige una opción: ")
        if not option.isdigit() or int(option) not in range (1, 6):
            print("\n\nError: Por favor ingresa un número entre 1 y 5.")
            input("\n\nPresione enter para continuar...")
            utilities.ClearConsole()
            continue
        
        option = int(option)
        utilities.ClearConsole()
        
        if option == 1:
            # Material selection process
            print("Elige el material")
            print("-Wood")
            print("-Aluminium")
            print("-Carbon fiber")
            
            material = input("Escribe el material deseado: ")
            while material != "Wood" and material != "Aluminium" and material != "Carbon fiber":
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
            # Display game catalog and allow user to select a game
            catalog.DisplayGames()
            gameChosen = input("Seleccione el índice de un juego del catálogo (1-17): ")
            
            # Validate game selection
            while not gameChosen.isdigit() or int(gameChosen) not in range (1, 18):
                print("\n\nError: Por favor ingresa un número entre 1 y 17.")
                input("\n\nPresione enter para continuar...")
                utilities.ClearConsole()
                catalog.DisplayGames()
                gameChosen = input("Seleccione el índice de un juego del catálogo (1-17): ")
                
            gameChosen = int(gameChosen)
            machine.AddGame(catalog.FromIndextoGame(gameChosen)) # Add the selected game to the machine
            print(f"Ha sido añadido {catalog.FromIndextoGame(gameChosen)} a la maquina... Presione enter para continuar")
            input()
            utilities.ClearConsole()
        
        elif option == 3:
            # Accessory management
            print("Gestionar accesorios adicionales:")
            print("-1. Agregar accesorio.")
            print("-2. Eliminar accesorio.")
            print("-3. Mostrar accesorios.")
            print("-4. Volver al menú principal.")
            
            accessoryOption = input("Elige una opción: ")
            while not accessoryOption.isdigit() or int(accessoryOption) not in range (1, 5):
                print("\n\nError: Por favor ingresa una opción valida.")
                input("\n\nPresione enter para continuar...")
                utilities.ClearConsole()
                print("Gestionar accesorios adicionales:")
                print("-1. Agregar accesorio.")
                print("-2. Eliminar accesorio.")
                print("-3. Mostrar accesorios.")
                print("-4. Volver al menú principal.")
                accessoryOption = input("Elige una opción: ")
            
            accessoryOption = int(accessoryOption)
            utilities.ClearConsole()
            
            if accessoryOption == 1:
                # Add accessory
                print("Elige el accesorio para agregar:")
                print("-1. Protector de pantalla")
                print("-2. Soporte para bebidas")
                print("-3. Luces LED")
                print("-4. Sistema de enfriamiento")
                print("-5. Kit de limpieza")
                print("-6. Cable de extensión")
                
                accessory = input("Escribe el índice del accesorio deseado: ")
                while not accessory.isdigit() or int(accessory) not in range (1, 7):
                    print("\n\nError: Por favor ingresa una opción valida.")
                    input("\n\nPresione enter para continuar...")
                    utilities.ClearConsole()
                    print("Elige el accesorio para agregar:")
                    print("-1. Protector de pantalla")
                    print("-2. Soporte para bebidas")
                    print("-3. Luces LED")
                    print("-4. Sistema de enfriamiento")
                    print("-5. Kit de limpieza")
                    print("-6. Cable de extensión")
                    accessory = input("Escribe el índice del accesorio deseado: ")
                
                accessory = int(accessory)
                machine.AddAccessory(accessory)
                if accessory == 1:
                    print("Accesorio 'Protector de pantalla' añadido.")
                elif accessory == 2:
                    print("Accesorio 'Soporte para bebidas' añadido.")
                elif accessory == 3:
                    print("Accesorio 'Luces LED' añadido.")
                elif accessory == 4:
                    print("Accesorio 'Sistema de enfriamiento' añadido.")
                elif accessory == 5:
                    print("Accesorio 'Kit de limpieza' añadido.")
                elif accessory == 6:
                    print("Accesorio 'Cable de extensión' añadido.")
                
                
                
                input("\n\nPresione enter para continuar...")
                utilities.ClearConsole()
            
            elif accessoryOption == 2:
                # Remove accessory
                print("Elige el accesorio para eliminar:")
                print("-1. Protector de pantalla")
                print("-2. Soporte para bebidas")
                print("-3. Luces LED")
                print("-4. Sistema de enfriamiento")
                print("-5. Kit de limpieza")
                print("-6. Cable de extensión")
                
                accessory = input("Escribe el índice del accesorio a eliminar: ")
                while not accessory.isdigit() or int(accessory) not in range (1, 7):
                    print("\n\nError: Por favor ingresa una opción valida.")
                    input("\n\nPresione enter para continuar...")
                    utilities.ClearConsole()
                    print("Elige el accesorio para agregar:")
                    print("-1. Protector de pantalla")
                    print("-2. Soporte para bebidas")
                    print("-3. Luces LED")
                    print("-4. Sistema de enfriamiento")
                    print("-5. Kit de limpieza")
                    print("-6. Cable de extensión")
                    accessory = input("Elige una opción: ")
                
                accessory = int(accessory)
                machine.RemoveAccessory(accessory)
                if accessory == 1:
                    print("Accesorio 'Protector de pantalla' eliminado.")
                elif accessory == 2:
                    print("Accesorio 'Soporte para bebidas' eliminado.")
                elif accessory == 3:
                    print("Accesorio 'Luces LED' eliminado.")
                elif accessory == 4:
                    print("Accesorio 'Sistema de enfriamiento' eliminado.")
                elif accessory == 5:
                    print("Accesorio 'Kit de limpieza' eliminado.")
                elif accessory == 6:
                    print("Accesorio 'Cable de extensión' eliminado.")
            
            elif accessoryOption == 3:
                # Show accessories
                print("Accesorios adicionales actuales:")
                machine.ShowAccessories()
                input("\n\nPresione enter para continuar...")
                utilities.ClearConsole()
            
            elif accessoryOption == 4:
                utilities.ClearConsole()
                continue
        
        elif option == 4:
            # Customer information input and purchase finalization
            print("Para finalizar la compra por favor ingrese su información de contacto: \n\n")
            name = input("Por favor ingrese su nombre completo: ")
            address = input("Por favor ingrese una dirección valida: ")
            customer.UpdateInformation(name, address) # Update customer information
            print(f"Los datos de usuario ingresados son los siguientes:\n\n-Nombre: {customer.name}\n-Dirección: {customer.address}")
            
            finalization = input("¿Desea finalizar la compra? (1.SI / 2.NO): ")
            while not finalization.isdigit() or int(finalization) not in range (1, 3):
                print("\n\nError: Por favor ingresa una opción valida.")
                input("\n\nPresione enter para continuar...")
                utilities.ClearConsole()
                finalization = input("¿Desea finalizar la compra? (1.SI / 2.NO): ")
                
            finalization = int(finalization)
            
            if finalization == 1:
                # Check if material is selected before finalizing
                if machine.material is None:
                    print("¡Por favor ingrese un material de fabricación para su maquina arcade!")
                    input("Presione enter para continuar...")
                    utilities.ClearConsole()
                    continue
                else:
                    utilities.ClearConsole()
                    print("--¡TU MAQUINA ARCADE HA SIDO ENVIADA A TU DIRECCIÓN CON EXITO!--")
                    print(f"\nEl material de tu máquina arcade es: {machine.material}.\n")
                    print(f"\nLos juegos añadidos a tu máquina arcade son: \n")
                    machine.ShowChosenGames()
                    print("\n\nAccesorios añadidos a tu máquina arcade:\n")
                    machine.ShowAccessories()
                    input("\n\nPresiona enter para continuar...")
                    
                    repeat = input("¿Desea realizar otra compra? (1.SI / 2.NO): ")
                    while not repeat.isdigit() or int(repeat) not in range (1, 3):
                        print("\n\nError: Por favor ingresa una opción valida.")
                        input("\n\nPresione enter para continuar...")
                        utilities.ClearConsole()
                        repeat = input("¿Desea realizar otra compra? (1.SI / 2.NO): ")
                
                    repeat = int(repeat)
                    
                    if repeat == 1:
                        # Reset instances for another purchase
                        machine = ArcadeMachine()
                        catalog = GameCatalog()
                        customer = Customer()
                        continue
                    else:
                        break
            else:
                utilities.ClearConsole()
                continue
        
        elif option == 5:
            break
                        
if __name__ == "__main__": # Run the main function when the script is executed
    run()
