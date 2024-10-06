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
import sys

MENU_CHOOSE_MACHINE = "\n\n-----WELCOME! CHOOSE A PREDERTERMINATED ARCADE MACHINE!!-----\n\n\n-1. Dance Revolution Machine.\n-2. Classical Arcade Machine.\n-3. Shotting Machine.\n-4. Racing Machine.\n-5. Virtual Reality Machine.\n-6. Exit."
MENU_DANCE_REVOLUTION_MACHINE = "\n\n-----DANCE REVOLUTION MACHINE MENU-----\n\n\n-1. Choose material.\n-2. Add/Quit game.\n-3. Set memory.\n-4. Set number of processors.\n-5. Set number of difficulties.\n-6. Set number of arrow cardinalities.\n-7. Finish purchase.\n-8. Exit."
MENU_CLASSICAL_ARCADE_MACHINE = "\n\n-----CLASSICAL ARCADE MACHINE MENU-----\n\n\n-1. Choose material.\n-2. Add/Quit game.\n-3. Set memory.\n-4. Set number of processors.\n-5. Set vibration.\n-6. Set sound record alert.\n-7. Finish purchase.\n-8. Exit."
MENU_SHOTTING_MACHINE = "\n\n-----SHOTTING MACHINE MENU-----\n\n\n-1. Choose material.\n-2. Add/Quit game.\n-3. Set memory\n-4. Set number of processors\n-5. Set guns number.\n-6. Set guns type.\n-7. Finish purchase.\n-8. Exit."
MENU_RACING_MACHINE = "\n\n-----RACING MACHINE MENU-----\n\n\n-1. Choose material.\n-2. Add/Quit game.\n-3. Set memory\n-4. Set number of processors\n-5. Set steering wheel type.\n-6. Finish purchase.\n-7. Exit."
MENU_VIRTUAL_REALITY_MACHINE = "\n\n-----VIRTUAL REALITY MACHINE MENU-----\n\n\n-1. Choose material.\n-2. Add/Quit game.\n-3. Set memory\n-4. Set number of processors\n-5. Set glass type\n-6. Set glass resolution\n-7. Finish purchase.\n-8. Exit."
MENU_ADD_QUIT_GAMES = "Select an option:\n\n-1- Add game.\n-2- Remove game.\n-3- Show games.\n-4- Return to main menu."


class Main():
    """This class represents the main behavior of the application."""
    
    def __init__(self, machine:ArcadeMachine, catalog:GameCatalog, customer:Customer):
        self.utilities = Utilities()
        self.machine = machine
        self.catalog = catalog
        self.customer = customer
    
        
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
        
    def handle_menu(self):
        option = input("Choose an option: ")
        while not option.isdigit() or int(option) not in range(1, 10):
            print("\n\nError: Please enter a valid option.")
            input("\n\nPress enter to continue...")
            self.utilities.ClearConsole()
            main_instance.show_menu()
            option = input("Choose an option: ")
                
        option = int(option)
        self.utilities.ClearConsole()
        if option == 1:
            print("Choose the material:\n\n-Wood.\n-Aluminium.\n-Carbon fiber.")
            material = input("Enter the desired material: ")
            
            while material != "Wood" and material != "Aluminium" and material != "Carbon fiber":
                print("You have selected an invalid option, please try again.")
                self.utilities.ClearConsole()
                self.utilities.ClearConsole()
                
                print("Choose the material:\n\n-Wood.\n-Aluminium.\n-Carbon fiber.")
                material = input("Enter the desired material: ")
            
            self.machine.SelectMaterial(material)
            print(f"\n\nThe chosen material was {material}...")
            input()
            self.utilities.ClearConsole()
            
            
        elif option == 2:
            print(MENU_ADD_QUIT_GAMES)
            option = input("\n\nChoose an option: ")
            while option not in range(1, 5) and not option.isdigit():
                print("\n\nError: Please enter a valid option.")
                input("\n\nPress enter to continue...")
                self.self.utilities.ClearConsole()
                print(MENU_ADD_QUIT_GAMES)
                option = input("Choose an option: ")
                
            option = int(option)
                
            if option == 1: #Add game
                self.utilities.ClearConsole()
                print("Choose a game from the catalog:\n\n")
                self.catalog.SetGames(self.machine) 
                self.catalog.DisplayGames()
                numberofgames = self.catalog.GetNumberOfGames()
                gamechosen = input(f"\n\nChoose the index of a game from the catalog: ")
                while not gamechosen.isdigit() or int(gamechosen) not in range (1, numberofgames + 1):
                    print("\n\nError: Please enter a valid number.")
                    input("\n\nPress enter to continue...")
                    self.utilities.ClearConsole()
                    self.catalog.DisplayGames()
                    gamechosen = input("Select the index of a game from the catalog: ")
                
                self.utilities.ClearConsole()
                gamechosen = int(gamechosen) #Parse the input to an integer
                self.machine.AddGame(self.catalog.FromIndextoGame(gamechosen)) # Add the selected game to the machine
                print(f"{self.catalog.FromIndextoGame(gamechosen)} has been added to the machine... \n\nPress enter to continue")
                self.base_price += 10
                input()
                self.utilities.ClearConsole()
                    
            elif option == 2: #Remove game
                self.utilities.ClearConsole()
                print("Choose a game to remove from the machine:\n\n")
                self.machine.ShowChosenGames()
                if self.machine.GetNumberOfGames() != 0:
                    gamechosen = input("\n\nSelect the index of a game to remove from the machine: ")
                    while not gamechosen.isdigit() or int(gamechosen) not in range (1, self.machine.GetNumberOfGames() + 1):
                        print("\n\nError: Please enter a valid number.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        self.machine.ShowChosenGames()
                        gamechosen = input("Select the index of a game to remove from the machine: ")
                    
                    gamechosen = int(gamechosen)
                    temporal = self.catalog.FromIndextoGameAdded(gamechosen, self.machine)
                    self.machine.RemoveGame(temporal)
                    print(f"{temporal} has been removed from the machine... \n\nPress enter to continue")
                    self.base_price -= 10
                    input()
                    self.utilities.ClearConsole()
                else:
                    print("\n\nPress enter to continue")
                    input()
                    self.utilities.ClearConsole()
                
            elif option == 3: #Show games
                self.utilities.ClearConsole()
                print("Current games in the machine:\n")
                self.machine.ShowChosenGames()
                input("\n\nPress enter to continue...")
                self.utilities.ClearConsole()
                
            elif option == 4:
                self.utilities.ClearConsole()
 
        elif option == 3:
            print("Choose the memory for the arcade machine:\n\n-1. 250GB.\n-2. 500GB.\n-3. 1TB.")
            temporal = input("Enter the desired memory: ")
            while not temporal.isdigit() or int(temporal) not in range(1, 4):
                print("\n\nError: Please enter a valid option.")
                input("\n\nPress enter to continue...")
                self.utilities.ClearConsole()
                print("Choose the memory for the arcade machine:\n\n-1. 250GB.\n-2. 500GB.\n-3. 1TB.")
                temporal = input("Enter the desired memory: ")
                
            temporal = int(temporal)
            self.machine.SetMemory(temporal)
            
            if temporal == 1:
                temporal = "250GB"
            elif temporal == 2:
                temporal = "500GB"
            elif temporal == 3:
                temporal = "1TB"
            
            print(f"\n\nThe memory has been set to {temporal}... \n\nPress enter to continue.")
            input()
            
            
        elif option == 4:
            print("Choose the number of processors for the arcade machine:\n\n-1. 1.\n-2. 2.\n-3. 4.")
            temporal = input("Enter the desired number of processors: ")
            while not temporal.isdigit() or int(temporal) not in range(1, 4):
                print("\n\nError: Please enter a valid option.")
                input("\n\nPress enter to continue...")
                self.utilities.ClearConsole()
                print("Choose the number of processors for the arcade machine:\n\n-1. 1.\n-2. 2.\n-3. 4.")
                temporal = input("Enter the desired number of processors: ")
            
            temporal = int(temporal)
            self.machine.SetProcessors(temporal)
            
            if temporal == 3:
                temporal = "4"
                
            print(f"\n\nThe number of processors has been set to {temporal}... \n\nPress enter to continue.")
            input()
            
        elif option == 7:
            self.utilities.ClearConsole()
            
            finalization = input("Do you want to finalize the purchase? (1.YES / 2.NO): ")
            while not finalization.isdigit() or int(finalization) not in range (1, 3):
                print("\n\nError: Please enter a valid option.")
                input("\n\nPress enter to continue...")
                self.utilities.ClearConsole()
                finalization = input("Do you want to finalize the purchase? (1.YES / 2.NO): ")
                
            finalization = int(finalization)
            if finalization == 1:
                if self.machine.material is None:
                    print("Please enter a manufacturing material for your arcade machine!")
                    print("\nPress enter to continue...")
                    input()
                    self.utilities.ClearConsole()
                    
                else:
                    self.utilities.ClearConsole()
                    
                    #change color
                    print("Please enter the color of the arcade machine: ")
                    print("\n\n-1. Red.\n-2. Blue.\n-3. Green.\n-4. Yellow.\n-5. Black.\n-6. White.")
                    color = input("\n\nEnter the desired color: ")
                    while not color.isdigit() or int(color) not in range(1, 7):
                        print("\n\nError: Please enter a valid option.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        print("Please enter the color of the arcade machine: ")
                        print("\n\n-1. Red.\n-2. Blue.\n-3. Green.\n-4. Yellow.\n-5. Black.\n-6. White.")
                        color = input("\n\nEnter the desired color: ")
                        
                    color = int(color)
                    colors = {
                        1: "Red",
                        2: "Blue",
                        3: "Green",
                        4: "Yellow",
                        5: "Black",
                        6: "White"
                    }
                    
                    print(f"\n\nThe color of the arcade machine has been set to {colors.get(color, 'Unknown')}... \n\nPress enter to continue.")
                    self.machine.color = colors.get(color, "Unknown")
                    input()
                    
                    self.utilities.ClearConsole()
                    #get contact information
                    print("To finalize the purchase please enter your contact information: \n\n")
                    name = input("Please enter your full name: ")
                    address = input("Please enter a valid address: ")
                    
                    self.utilities.ClearConsole()
                    print("--YOUR ARCADE MACHINE HAS BEEN SUCCESSFULLY SENT TO YOUR ADDRESS!--")
                    
                    print("\n\nType of arcade machine: ", "---------", type(self.machine).__name__, "---------")
                    
                    
                    print(f"\nYour arcade machine material is: {self.machine.material}.\n")
                    
                    print(f"\nGames added to your arcade machine are: \n")
                    
                    self.machine.ShowChosenGames()
                    
                    print(f"\n\nenergy consumption: {self.machine.energyconsumption} watts.")
                    
                    print(f"\n\nThe color of the arcade machine is: {colors.get(color, 'Unknown')}.")
                    
                    print(f"\n\nThe price of the arcade machine is: {self.machine.base_price} USD.")
                    
                    print(f"the dimensions of the arcade machine are: {self.machine.dimensions} cm.")
                    
                    print(f"\n\nThe weight of the arcade machine is: {self.machine.weight} kg.")
                    
                    if isinstance(self.machine, DanceRevolutionMachine):
                        print(f"\n\nThe number of difficulties is: {self.machine.difficulties}.")
                        print(f"\n\nThe number of arrow cardinalities is: {self.machine.arrowCardinalities}.")
                        
                    elif isinstance(self.machine, ClassicalArcadeMachine):
                        print(f"\n\nThe vibration is: {'YES' if self.machine.vibration == 1 else 'NO'}.")
                        print(f"\n\nThe sound record alert is: {'YES' if self.machine.sound_record_alert == 1 else 'NO'}.")
                        
                    elif isinstance(self.machine, ShottingMachine):
                        print(f"\n\nThe number of guns is: {self.machine.guns_number}.")
                        print(f"\n\nThe type of guns is: {self.machine.guns_type}.")
                        
                    elif isinstance(self.machine, RacingMachine):
                        print(f"\n\nThe type of steering wheel is: {self.machine.steering_wheel_type}.")
                        
                    elif isinstance(self.machine, VirtualRealityMachine):
                        print(f"\n\nThe type of glass is: {self.machine.glass_type}.")
                        print(f"\n\nThe resolution of the glass is: {self.machine.glass_resolution}.")
                        
                    print(f"\n\nThe memory is: {self.machine.memory}.")
                    
                    print(f"\n\nThe number of processors is: {self.machine.processors}.")
                    
                    print(f"\n\nThe contact information is: \n\n-Name: {name}\n-Address: {address}")
                    
                    print("\n\nThe purchase has been successfully completed... \n\nPress enter to continue.")
                    
                    input()
                    
                    
                    repeat = input("\n\nDo you want to make another purchase? (1.YES / 2.NO): ")
                    while not repeat.isdigit() or int(repeat) not in range (1, 3):
                        print("\n\nError: Please enter a valid option.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        repeat = input("Do you want to make another purchase? (1.YES / 2.NO): ")
                    
                    repeat = int(repeat)
                    if repeat == 1:
                        machine = ArcadeMachine()
                        catalog = GameCatalog()
                        customer = Customer()
                        
                    else:
                        print("Exiting the program...")
                        input("Press enter to continue...")
            
            
        
        elif option == 8:
            print("Exiting the program...")
            input("Press enter to continue...")
            sys.exit()
            
        else:
            if isinstance(self.machine, DanceRevolutionMachine):
                if option == 5:
                    print("Choose the number of difficulties for the game:\n\n-1. 1.\n-2. 2.\n-3. 3.")
                    numberofdifficulties = input("Enter the desired number of difficulties: ")
                    while not numberofdifficulties.isdigit() or int(numberofdifficulties) not in range(1, 4):
                        print("\n\nError: Please enter a valid number.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        print("Choose the number of difficulties for the game:\n\n-1. 1.\n-2. 2.\n-3. 3.")
                        numberofdifficulties = input("Enter the desired number of difficulties: ")
                        
                    self.machine.setDifficulties(numberofdifficulties)
                    print(f"\n\nThe number of difficulties has been set to {numberofdifficulties}... \n\nPress enter to continue.")
                    input()
                    self.utilities.ClearConsole()
                
                elif option == 6:
                    print("Choose the number of arrow cardinalities for the game:\n\n-1. 4.\n-2. 8.\n")
                    numberofarrowcardinalities = input("Enter the desired number of arrow cardinalities: ")
                    while not numberofarrowcardinalities.isdigit() or int(numberofarrowcardinalities) == 4 or int(numberofarrowcardinalities) == 8:
                        print("\n\nError: Please enter a valid number.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        print("Choose the number of arrow cardinalities for the game:\n\n-1. 4.\n-2. 8.\n")
                        numberofarrowcardinalities = input("Enter the desired number of arrow cardinalities: ")
                        
                    self.machine.setArrowCardinalities(numberofarrowcardinalities)
                    print(f"\n\nThe number of arrow cardinalities has been set to {numberofarrowcardinalities}... \n\nPress enter to continue.")
                    input()
                    self.utilities.ClearConsole()
                    
            elif isinstance(self.machine, ClassicalArcadeMachine):
                if option == 5:
                    print("Choose the vibration for the machine:\n\n-1. Yes.\n-2. No.")
                    vibration = input("Enter the desired vibration: ")
                    while not vibration.isdigit() or int(vibration) not in range(1, 3):
                        print("\n\nError: Please enter a valid number.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        print("Choose the vibration for the machine:\n\n-1. Yes.\n-2. No.")
                        vibration = input("Enter the desired vibration: ")
                        
                    vibration = int(vibration)
                    self.machine.setMakeVibration(vibration)
                    print(f"\n\nThe vibration has been set to {'YES' if vibration == 1 else 'NO'}... Press enter to continue.")
                    input()
                    self.utilities.ClearConsole()
                
                elif option == 6:
                    print("Choose the sound record alert for the machine:\n\n-1. Yes.\n-2. No.")
                    soundrecordalert = input("Enter the desired sound record alert: ")
                    while not soundrecordalert.isdigit() or int(soundrecordalert) not in range(1, 3):
                        print("\n\nError: Please enter a valid number.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        print("Choose the sound record alert for the machine:\n\n-1. Yes.\n-2. No.")
                        soundrecordalert = input("Enter the desired sound record alert: ")
                        
                    soundrecordalert = int(soundrecordalert)
                    self.machine.setSoundRecordAlert(soundrecordalert)
                    print(f"\n\nThe sound record alert has been set to {'YES' if soundrecordalert == 1 else 'NO'}... Press enter to continue.")
                    input()
                    self.utilities.ClearConsole()
                    
            elif isinstance(self.machine, ShottingMachine):
                if option == 5:
                    print("Choose the number of guns for the machine:\n\n-1. 1.\n-2. 2.\n-3. 4.")
                    numberofguns = input("Enter the desired number of guns: ")
                    while not numberofguns.isdigit() or int(numberofguns) not in range(1, 4):
                        print("\n\nError: Please enter a valid number.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        print("Choose the number of guns for the machine:\n\n-1. 1.\n-2. 2.\n-3. 4.")
                        numberofguns = input("Enter the desired number of guns: ")
                        
                    numberofguns = int(numberofguns)
                    self.machine.setGunsNumber(numberofguns)
                    print(f"\n\nThe number of guns has been set to {numberofguns}... Press enter to continue.")
                    input()
                    self.utilities.ClearConsole()
                    
                elif option == 6:
                    print("Choose the type of guns for the machine:\n\n-1. Pistol.\n-2. Rifle.\n-3. Shotgun.\n-4. Machine gun.")
                    gunstype = input("Enter the desired type of guns: ")
                    while not gunstype.isdigit() or int(gunstype) not in range(1, 5):
                        print("\n\nError: Please enter a valid number.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        print("Choose the type of guns for the machine:\n\n-1. Pistol.\n-2. Rifle.\n-3. Shotgun.\n-4. Machine gun.")
                        gunstype = input("Enter the desired type of guns: ")
                        
                    gun_types = {
                        1: "Pistol",
                        2: "Rifle",
                        3: "Shotgun",
                        4: "Machine gun"
                    }
                    
                    gunstype = int(gunstype)
                    self.machine.setGunType(gunstype)
                    
                    gun_name = gun_types.get(gunstype, "Unknown")
                    
                    print(f"\n\nThe type of guns has been set to {gun_name}... Press enter to continue.")
                    input()
                    self.utilities.ClearConsole()
                
            elif isinstance(self.machine, RacingMachine):
                if option == 5:
                    print("Choose the type of steering wheel for the machine:\n\n-1. Basic.\n-2. Advanced.\n-3. Professional.\n-4. Ultimate.")
                    steeringwheeltype = input("Enter the desired type of steering wheel: ")
                    while not steeringwheeltype.isdigit() or int(steeringwheeltype) not in range(1, 5):
                        print("\n\nError: Please enter a valid number.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        print("Choose the type of steering wheel for the machine:\n\n-1. Basic.\n-2. Advanced.\n-3. Professional.\n-4. Ultimate.")
                        steeringwheeltype = input("Enter the desired type of steering wheel: ")
                        
                    steeringwheeltype = int(steeringwheeltype)
                    self.machine.setSteeringWheelType(steeringwheeltype)
                    steering_wheel_types = {
                        1: "Basic",
                        2: "Advanced",
                        3: "Professional",
                        4: "Ultimate"
                    }
                    
                    steering_wheel_name = steering_wheel_types.get(int(steeringwheeltype), "Unknown")
                    
                    print(f"\n\nThe type of steering wheel has been set to {steering_wheel_name}... Press enter to continue.")
                    input()
                    self.utilities.ClearConsole()
                
            elif isinstance(self.machine, VirtualRealityMachine):
                if option == 5:
                    print("Choose the type of glass for the machine:\n\n-1. Basic.\n-2. Advanced.\n-3. Professional.\n-4. Ultimate.")
                    glasstype = input("Enter the desired type of glass: ")
                    while not glasstype.isdigit() or int(glasstype) not in range(1, 5):
                        print("\n\nError: Please enter a valid number.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        print("Choose the type of glass for the machine:\n\n-1. Basic.\n-2. Advanced.\n-3. Professional.\n-4. Ultimate.")
                        glasstype = input("Enter the desired type of glass: ")
                        
                    glasstype = int(glasstype)
                    self.machine.setGlassType(glasstype)
                    glass_types = {
                        1: "Basic",
                        2: "Advanced",
                        3: "Professional",
                        4: "Ultimate"
                    }
                    
                    glass_name = glass_types.get(int(glasstype), "Unknown")
                    
                    print(f"\n\nThe type of glass has been set to {glass_name}... \n\nPress enter to continue.")
                    input()
                    self.utilities.ClearConsole()
                    
                elif option == 6:
                    print("Choose the resolution of the glass for the machine:\n\n-1. 720p.\n-2. 1080p.\n-3. 1440p.\n4. 2160p.")
                    glassresolution = input("Enter the desired resolution of the glass: ")
                    while not glassresolution.isdigit() or int(glassresolution) not in range(1, 4):
                        print("\n\nError: Please enter a valid number.")
                        input("\n\nPress enter to continue...")
                        self.utilities.ClearConsole()
                        print("Choose the resolution of the glass for the machine:\n\n-1. 720p.\n-2. 1080p.\n-3. 1440p.\n4. 2160p.")
                        glassresolution = input("Enter the desired resolution of the glass: ")
                        
                    self.machine.setGlassResolution(glassresolution)
                    glass_resolutions = {
                        1: "720p",
                        2: "1080p",
                        3: "1440p",
                        4: "2160p"
                    }
                    
                    glass_resolution_name = glass_resolutions.get(int(glassresolution), "Unknown")
                    
                    print(f"\n\nThe resolution of the glass has been set to {glass_resolution_name}... \n\nPress enter to continue.")
                    input()
        self.show_menu()
        self.handle_menu()
        
                    
                
        
        
def run():
    # Create instances of necessary classes
    machine = ArcadeMachine()
    utilities = Utilities()
    catalog = GameCatalog()
    customer = Customer()
    main_instance = Main(machine, catalog, customer)    
    
    
    while True:
        main_instance.choose_predeterminated_machine_menu()
        machine_option = input("Choose an option: ")
        while not machine_option.isdigit() or int(machine_option) not in range(1, 7):
            print("\n\nError: Please enter a valid option.")
            input("\n\nPress enter to continue...")
            self.utilities.ClearConsole()
            main.choose_predeterminated_machine_menu()
            machine_option = input("Choose an option: ")
            
        machine_option = int(machine_option)
        utilities.ClearConsole()
        if machine_option == 1:
            machine = DanceRevolutionMachine()
        elif machine_option == 2:
            machine = ClassicalArcadeMachine()
        elif machine_option == 3:
            machine = ShottingMachine()
        elif machine_option == 4:
            machine = RacingMachine()
        elif machine_option == 5:
            machine = VirtualRealityMachine()
        elif machine_option == 6:
            print("Exiting the program...")
            input("Press enter to continue...")
            sys.exit()
        
        main_instance.machine = machine
        main_instance.show_menu() # Show the menu according to the selected arcade machine
        main_instance.handle_menu() # Handle the selected option
        break
                        
if __name__ == "__main__": # Run the main function when the script is executed
    run()
