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
from typing import List
class ArcadeMachine ():
        """
        It represents an arcade video game machine. It allows selecting materials, adding games, 
        and completing the purchase.
        """
        
        def __init__(self): 
                self.machine_type = None
                self.material = None
                self.dimensions = []
                self.gamesadded = []
                self.weight = 100
                self.energyconsumption = 300
                self.memory = None
                self.processors = None
                self.base_price = 0
                self.color = None
                self.dimensions = []
        
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
                print("The game is already in the list.")
                input()
            else:
                self.gamesadded.append(game)
                self.base_price += 2
                        
        def RemoveGame (self, game: str):
            """
            This method removes a game from the list of added games.
            
            This method takes one argument, expected as a string, and removes it from the list of games 
            if it is present. If the game is not in the list, it prints a message indicating that the game 
            is not in the list.
            
            Args:
            game (str): The game to be removed from the list.
                  
            Returns:
            None.
            """
                
            if game in self.gamesadded:
                self.gamesadded.remove(game)
                self.base_price -= 2
            else:
                print("The game is not in the list.")
                input()
                        
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
                print("The list of games is empty.")
                        
        def AddAccessory(self, accessory: str):
            """
            This method adds an accessory to the arcade machine.
                
            Args:
            accessory (str): The name of the accessory to be added.
                
            Returns:
            None.
            """
            self.extraAccesories.AddAccessory(accessory)
                
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
            self.extraAccesories.ShowAccessories()
                
        def GetNumberOfAccessories(self):
            """
            This method returns the number of accessories in the list.
            
            Returns:
            int: The number of accessories in the list.
            """
            return len(self.extraaccesories.accessories)
        
        def GetAccesoryName(self, index: int) -> str:
            """
            This method retrieves an accessory from the list based on its index.
            
            Args:
            index (int): The index of the accessory to retrieve (1-based).
            
            Returns:
            str: The accessory at the specified index.
            """
            return self.extraaccesories.accessories[index - 1]
            
            
        def SetEnergyConsumption(self, material: str):
            """
            This method sets the energy consumption of the arcade machine.
            
            Args:
            energyconsumption (float): The energy consumption of the arcade machine.
            
            Returns:
            None.
            """
            energyconsumption = self.machine.energyconsumption
            if material == "Wood":
                self.energyconsumption *= 1.15
            elif material == "Carbon fiber":
                self.energyconsumption *= 0.9
                
        def SetWeight(self, material: str):
            if material == "Wood":
                self.weight *= 1.1
            elif material == "Aluminium":
                self.weight *= 0.95
            elif material == "Carbon fiber":
                self.weight *= 0.85
            
        
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
            
        def GetNumberOfGames(self) -> int:
            """
            This method returns the number of games in the list.
            
            Returns:
            int: The number of games in the list.
            """
            return len(self.gamesadded)  
                
                
class DanceRevolutionMachine (ArcadeMachine):
    
    def __init__(self):
        super().__init__()
        self.difficulties = None
        self.arrowCardinalities = None
        self.controls_price = None
        self.base_price = 3000
        self.dimensions = [1.5, 2.5, 1.5]
        self.weight = 200
        
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
        self.base_price = 2000
        self.dimensions = [1.5, 2.5, 1.5]
        self.weight = 250
        
    def setMakeVibration(self, makeVibration: int):
        """
        This method sets the vibration for the machine.
        
        Args:
        makeVibration (bool): The vibration for the machine.
        
        Returns:
        None.
        """
        if makeVibration == 1:
            self.makeVibration = True
        else:
            self.makeVibration = False
        
    def setSoundRecordAlert(self, soundRecordAlert: int):
        """
        This method sets the sound record alert for the machine.
        
        Args:
        soundRecordAlert (bool): The sound record alert for the machine.
        
        Returns:
        None.
        """
        if soundRecordAlert == 1:
            self.soundRecordAlert = True
        else:
            self.soundRecordAlert = False
        
        
class ShottingMachine (ArcadeMachine):
    
    def __init__(self):
        super().__init__()
        self.gunsNumber = None
        self.gunPrice = None
        self.gunType = None
        self.base_price = 2500
        self.dimensions = [1.3, 2.5, 1.2]
        self.weight = 230
        
    def setGunsNumber (self, guns: int):
        """
        This method sets the number of guns for the machine.
        
        Args:
        guns (int): The number of guns for the machine.
        
        Returns:
        None.
        """
        while guns < 1:
            print("Enter a valid number.")
            guns = int(input("Enter the number of guns: "))
            
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
        self.base_price = 3200
        self.dimensions = [2, 2.5, 2]
        self.weight = 300
        
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
        self.base_price = 3000
        self.dimensions = [1.5, 2.5, 2]
        self.weight = 150
        
    def setGlassType (self, glassesType: str):
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
        
    def setGlassResolution (self, glassesResolution: str):
        """
        This method sets the resolution for the glasses between 720p, 1080p, 1440p, and 2160p.
        
        Args:
        glassesResolution (str): The resolution for the glasses.
        
        Returns:
        None.
        """

        self.glassesResolution = glassesResolution
    
    

class GameCatalog ():
        """
        It maintains and displays the list of available games.
        """
        
        def __init__(self):
                self.games = []
                
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
                        
        def SetGames(self, machine: ArcadeMachine):
            """
            This method sets the games for the arcade machine based on its type.
            
            Args:
            machine (ArcadeMachine): The arcade machine instance to set games for.
            
            Returns:
            None.
            """
            if self.games == []:
                if isinstance(machine, DanceRevolutionMachine):
                    games = [
                        "Dance Dance Revolution", "Pump It Up", "In The Groove", 
                        "StepMania", "Just Dance", "Dance Central", 
                        "ParaParaParadise", "Dance Evolution", "Dance Factory", 
                        "Technomotion", "Dance Dance Revolution SuperNova", "Dance Dance Revolution X", 
                        "Dance Dance Revolution Extreme", "Dance Dance Revolution A", "Dance Dance Revolution 5th Mix"
                    ]
                elif isinstance(machine, ClassicalArcadeMachine):
                    games = [
                        "Pac-Man", "Donkey Kong", "Space Invaders", "Galaga", "Asteroids", 
                        "Centipede", "Defender", "Frogger", "Joust", "Missile Command", 
                        "Q*bert", "Robotron: 2084", "Dig Dug", "BurgerTime", "Tempest"
                    ]
                elif isinstance(machine, ShottingMachine):
                    games = [
                        "Time Crisis", "House of the Dead", "Virtua Cop", "Silent Scope", "Point Blank", 
                        "Lethal Enforcers", "Area 51", "Big Buck Hunter", "Operation Wolf", "Police Trainer", 
                        "CarnEvil", "Jurassic Park Arcade", "Aliens: Extermination", "Rambo", "Ghost Squad", 
                        "Terminator Salvation", "Mad Dog McCree"]
                elif isinstance(machine, RacingMachine):
                    games = [
                        "Daytona USA", "Cruis'n USA", "OutRun", "Ridge Racer", "Sega Rally Championship", 
                        "Initial D Arcade Stage", "Mario Kart Arcade GP", "F-Zero AX", "Need for Speed: Underground", 
                        "Hydro Thunder", "Midnight Club", "Burnout", "Crazy Taxi", "Wangan Midnight Maximum Tune", 
                        "Fast & Furious: SuperCars"
                    ]
                elif isinstance(machine, VirtualRealityMachine):
                    games = ["Beat Saber", "Superhot VR", "Half-Life: Alyx"
                    "Arizona Sunshine", "The Walking Dead: Saints & Sinners", "No Man's Sky VR", 
                    "Star Wars: Squadrons", "The Elder Scrolls V: Skyrim VR", "Resident Evil 7: Biohazard", 
                    "Boneworks", "Pavlov VR", "Job Simulator", "Moss", 
                    "Astro Bot Rescue Mission", "Vader Immortal"]
                else:
                    games = []
                
                for game in games:
                    self.games.append(game)
            
                        
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
            
        def FromIndextoGameAdded(self, index: int, machine: ArcadeMachine) -> str:
                """
                This method retrieves a game from the list based on its index.
                
                This method takes one argument, expected as an integer, and returns the game corresponding to that index 
                in the list of games.
                
                Args:
                  index (int): The index of the game to retrieve (1-based).

                Returns:
                  str: The game at the specified index.
                """
                
                return machine.gamesadded[index - 1]
            
        def GetNumberOfGames(self) -> int:
                """
                This method returns the number of games in the list.
                
                Returns:
                  int: The number of games in the list.
                """
                
                return len(self.games)
            
        
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
                
        
        