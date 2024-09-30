"""This module contains both abstract and concrete class definitions for an arcade machine seller program.

Author: Maiker Alejandro Hernández <mahernandeza@udistrital.edu.co>
        Joan Sebastián Durán Pradilla <Jsduranp@udistrital.edu.co>
        
this file is part of Workshops.

Arcade Machine Seller is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your opinion) any later version.

Arcade Machine Seller is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY... ; without even the implied warranty 
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>."""

import os
class ArcadeMachine ():
        """
        It represents an arcade video game machine. It allows selecting materials, adding games, 
        and completing the purchase.
        """
        
        def __init__(self): 
                self.material = None
                self.gamesadded = []
                self.extraaccesories = ExtraAccesories()
                self.dimensions = []
                self.weight = 0
                self.energyconsumption = 0
                self.memory = None
                self.processors = None
                self.base_price = 0
                self.color = None
        
        def  SelectMaterial (self, material: str):
                """
                This method selects a material for the arcade machine.
                
                This method takes one argument, expected as a string, and sets the material for the arcade machine.
                
                Args:
                  material (str): The material to be selected for the arcade machine.
                  
                Returns:
                  None.
                """
                
                self.material = material
                
                if material == "Wood":
                    self.weight *= 1.1
                    self.base_price *= 0.95
                    self.energyconsumption *= 1.15
                    
                elif material == "Aluminium":
                    self.weight *= 0.95
                    self.base_price *= 1.1
                
                elif material == "Carbon fiber":
                    self.weight *= 0.85
                    self.base_price *= 1.2
                    self.energyconsumption *= 0.9
                      

        def AddGame (self, game: str):
                """
                This method adds a game to the list of added games.
                
                This method takes one argument, expected as a string, and appends it to the list of games 
                if it is not already present. If the game is already in the list, it prints a message indicating 
                that the game is already in the list.
                
                Args:
                  game (str): The game to be added to the list.
                  
                Returns:
                  None.
                """
                
                if game in self.gamesadded:
                        print("El juego ya se encuentra en la lista")
                        input()
                else:
                        self.gamesadded.append(game)
                        self.base_price += 2
                        
        def ShowChosenGames (self):
                """
                This method displays the list of chosen games for the actual machine.
                
                This method iterates over the list of added games and prints each game with a corresponding number.
                If the list of games is empty, it prints a message indicating that the list is empty.
                  
                Returns:
                  None.
                """
                
                counter = 0
                if len(self.gamesadded) > 0:
                        for game in self.gamesadded:
                                counter += 1
                                print(f"{counter}. {game}.")
                else:
                        print("La lista de juegos está vacia.")
                        
        def AddAccessory(self, accessory: str):
                """
                This method adds an accessory to the arcade machine.
                
                Args:
                accessory (str): The name of the accessory to be added.
                
                Returns:
                None.
                """
                self.extraaccesories.AddAccessory(accessory)
                
        def RemoveAccessory(self, accessory: str):
                """
                This method removes an accessory from the arcade machine.
                
                Args:
                accessory (str): The name of the accessory to be removed.
                
                Returns:
                None.
                """
                self.extraAccesories.RemoveAccessory(accessory)
                
        def ShowAccessories(self):
                """
                This method displays the current status of all accessories.
                
                Returns:
                None.
                """
                self.extraaccesories.ShowAccessories()
            
            
        def SetEnergyConsumption(self, energyconsumption: float):
            """
            This method sets the energy consumption of the arcade machine.
            
            Args:
            energyconsumption (float): The energy consumption of the arcade machine.
            
            Returns:
            None.
            """
            while energyconsumption < 0:
                print("set the correct energy consumption.")
                energyconsumption = float(input("set the energy consumption of the machine: "))
            self.energyconsumption = energyconsumption
            
        
        def SetMemory(self, memory: int):
            """
            This method sets the memory of the arcade machine.
            The memory must be greater than 0, and it could be 250, 500 or 1000
            
            Args:
            memory (int): The memory of the arcade machine.
            
            Returns:
            None.
            """
            while memory < 0 and memory != 250 and memory != 500 and memory != 1000:
                print("Set a correct number for the memory.")
                memory = int(input("set the memory of the machine: "))
            self.memory = memory
                
                
        def SetProcessors(self, processors: int):
            """
            This method sets the number of processors of the arcade machine.
            The number of processors must be greater than 0, and it could be 1, 2 or 4.
            
            Args:
            processors (int): The number of processors of the arcade machine.
            
            Returns:
            None.
            """
            while processors < 0 and processors != 1 and processors != 2 and processors != 4:
                print("Set a correct number for the processors.")
                processors = int(input("set the number of processors of the machine: "))
            self.processors = processors
            
        
        def SetColor(self, color: str):
            """
            This method sets the color of the arcade machine.
            
            Args:
            color (str): The color of the arcade machine.
            
            Returns:
            None.
            """
            self.color = color       
                
                
class DanceRevolutionMachine (ArcadeMachine):
    
    def __init__(self):
        super().__init__()
        self.difficulties = None
        self.arrowCardinalities = None
        self.controls_price = None
        
    def setDifficulties(self, difficulties: int):
        """
        This method sets the number of difficulties for the game.
        
        Args:
        difficulties (int): The number of difficulties for the game.
        
        Returns:
        None.
        """
        self.difficulties = difficulties
        
    def setArrowCardinalities(self, arrowCardinalities: int):
        """
        This method sets the number of cardinalities for the arrows. It could be 4 or 8.
        
        Args:
        arrowCardinalities (int): The number of cardinalities for the arrows.
        
        Returns:
        None.
        """
        while arrowCardinalities != 4 and arrowCardinalities != 8:
            print("El número de cardinalidades debe ser 4 o 8.")
            arrowCardinalities = int(input("Ingrese el número de cardinalidades: "))
        
        self.arrowCardinalities = arrowCardinalities
        
    def setControls(self, controls_price: float):
        """
        This method sets the price for the controls.
        
        Args:
        controls_price (float): The price for the controls.
        
        Returns:
        None.
        """
        self.controls_price = controls_price
        
        
    
class ClassicalArcadeMachine (ArcadeMachine):
    
    def __init__(self):
        super().__init__()
        self.makeVibration = None
        self.soundRecordAlert = None
        
    def setMakeVibration(self, makeVibration: bool):
        """
        This method sets the vibration for the machine.
        
        Args:
        makeVibration (bool): The vibration for the machine.
        
        Returns:
        None.
        """
        self.makeVibration = makeVibration
        
    def setSoundRecordAlert(self, soundRecordAlert: bool):
        """
        This method sets the sound record alert for the machine.
        
        Args:
        soundRecordAlert (bool): The sound record alert for the machine.
        
        Returns:
        None.
        """
        self.soundRecordAlert = soundRecordAlert
        
        
class ShottingMachine (ArcadeMachine):
    
    def __init__(self):
        super().__init__()
        self.gunsNumber = None
        self.gunPrice = None
        self.gunType = None
        
    def setGunsNumber (self, guns: int):
        """
        This method sets the number of guns for the machine.
        
        Args:
        guns (int): The number of guns for the machine.
        
        Returns:
        None.
        """
        while guns < 1:
            print("Ingrese un número valido.")
            guns = int(input("Ingrese el número de armas: "))
            
        self.gunsNumber = guns
        
    def setGunType (self, gunType: str):
        """
        This method sets the type of gun for the machine and calculates the price.
        
        Args:
        gunType (str): The type of gun for the machine.
        
        Returns:
        None.
        """
        self.gunType = gunType
        if gunType == "Pistol":
            self.gunPrice = 50
        elif gunType == "Rifle":
            self.gunPrice = 100
        elif gunType == "Shotgun":
            self.gunPrice = 150
        elif gunType == "Machine gun":
            self.gunPrice = 200
        
        
class RacingMachine (ArcadeMachine):
    
    def __init__(self):
        super().__init__()
        self.steeringWheelPrice = None
        self.steeringWheelType = None
        
    def setSteeringWheelType (self, steeringWheelType: str):
        """
        This method sets the type of steering wheel for the machine.
        
        Args:
        steeringWheelType (str): The type of steering wheel for the machine.
        
        Returns:
        None.
        """
        self.steeringWheelType = steeringWheelType
        
        if steeringWheelType == "Basic":
            self.steeringWheelPrice = 50
        elif steeringWheelType == "Advanced":
            self.steeringWheelPrice = 100
        elif steeringWheelType == "Professional":
            self.steeringWheelPrice = 150
        elif steeringWheelType == "Ultimate":
            self.steeringWheelPrice = 200
        
class VirtualRealityMachine (ArcadeMachine):
    
    def __init__(self):
        super().__init__()
        self.glassesType = None
        self.glassesPrice = None
        self.glassesResolution = None
        
    def setGlassesType (self, glassesType: str):
        """
        This method sets the type of glasses for the machine.
        
        Args:
        glassesType (str): The type of glasses for the machine.
        
        Returns:
        None.
        """
        self.glassesType = glassesType
        
        if glassesType == "Basic":
            self.glassesPrice = 50
        elif glassesType == "Advanced":
            self.glassesPrice = 100
        elif glassesType == "Professional":
            self.glassesPrice = 150
        elif glassesType == "Ultimate":
            self.glassesPrice = 200
        
    def setGlassesResolution (self, glassesResolution: str):
        """
        This method sets the resolution for the glasses between 720p, 1080p, 1440p, and 2160p.
        
        Args:
        glassesResolution (str): The resolution for the glasses.
        
        Returns:
        None.
        """
        while glassesResolution != "720p" and glassesResolution != "1080p" and glassesResolution != "1440p" and glassesResolution != "2160p":
            print("Ingrese una resolución válida.")
            glassesResolution = input("Ingrese la resolución de las gafas: ")
        self.glassesResolution = glassesResolution
    
    

class GameCatalog ():
        """
        It maintains and displays the list of available games.
        """
        
        def __init__(self):
                self.games = ["Space invaders", "Tetris", "Donkey Kong", "Street Fighter II", "Metal Slug",
                              "Ghosts 'n Goblins", "OutRun", "Double Dragon", "Asteroids", "Galaxian", "Frogger",
                              "Scramble", "Galaga", "Tempest", "Dragon's lair", "1942", "Kung-fu master"]
                
        def DisplayGames(self):
                """
                This method displays the list of available games.
                
                This method iterates over the list of available games and prints each game with a corresponding number.
                
                Returns:
                  None.
                """
                
                counter = 0
                for game in self.games:
                        counter += 1
                        print(f"{counter}. {game}")
                        
        def FromIndextoGame(self, index: int) -> str:
                """
                This method retrieves a game from the list based on its index.
                
                This method takes one argument, expected as an integer, and returns the game corresponding to that index 
                in the list of games.
                
                Args:
                  index (int): The index of the game to retrieve (1-based).

                Returns:
                  str: The game at the specified index.
                """
                
                return self.games[index - 1]
        
class Customer ():
        """
        It represents the customer making the purchase. It stores the customer's basic personal information.
        """
        
        def __init__(self):
                self.name = None
                self.address = None
                
        def UpdateInformation (self, name: str, address: str):
                """
                This method updates the name and address information.
                """
                self.name = name
                self.address = address
                
class ExtraAccesories:
        """
        It represents the extra accessories available for the arcade machine.
        """
    
        def __init__(self):
                self.screenProtector = False
                self.drinksHolder = False
                self.ledLights = False
                self.coolingSystem = False
                self.cleaningKit = False
                self.extensionCable = False

        def AddAccessory(self, accessory: int):
                """
                This method adds an accessory to the arcade machine.
                
                Args:
                accessory (str): The name of the accessory to be added.
                
                Returns:
                None.
                """
        
                if accessory == 1:
                        self.screenProtector = True
                elif accessory == 2:
                        self.drinksHolder = True
                elif accessory == 3:
                        self.ledLights = True
                elif accessory == 4:
                        self.coolingSystem = True
                elif accessory == 5:
                        self.cleaningKit = True
                elif accessory == 6:
                        self.extensionCable = True

        def RemoveAccessory(self, accessory: int):
                """
                This method removes an accessory from the arcade machine.
                
                Args:
                accessory (str): The name of the accessory to be removed.
                
                Returns:
                None.
                """
                
                if accessory == 1:
                        self.screenProtector = False
                elif accessory == 2:
                        self.drinksHolder = False
                elif accessory == 3:
                        self.ledLights = False
                elif accessory == 4:
                        self.coolingSystem = False
                elif accessory == 5:
                        self.cleaningKit = False
                elif accessory == 6:
                        self.extensionCable = False

        def ShowAccessories(self):
                """
                This method displays the current status of all accessories.
                
                Returns:
                None.
                """
                
                print(f"Protector de pantalla: {'SI.' if self.screenProtector else 'NO.'}")
                print(f"Portavasos: {'SI.' if self.drinksHolder else 'NO.'}")
                print(f"Luces lED: {'SI.' if self.ledLights else 'NO.'}")
                print(f"Sistema de refrigeración: {'SI.' if self.coolingSystem else 'NO.'}")
                print(f"Kit de limpieza: {'SI.' if self.cleaningKit else 'NO.'}")
                print(f"Cable de extensión: {'SI.' if self.extensionCable else 'NO.'}")

                
class Utilities ():
        def ClearConsole(self):
                """
                This method clears the console screen.
                
                This method detects the operating system and executes the appropriate command to clear the console.
                On Windows, it uses the 'cls' command, and on other operating systems, it uses the 'clear' command.
                """
                if os.name == 'nt':
                        os.system('cls')
                else:
                        os.system('clear')
                
        
        