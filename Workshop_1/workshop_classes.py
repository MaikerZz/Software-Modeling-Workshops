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
        
                if accessory == "screenProtector":
                        self.screenProtector = True
                elif accessory == "drinksHolder":
                        self.drinksHolder = True
                elif accessory == "ledLights":
                        self.ledLights = True
                elif accessory == "coolingSystem":
                        self.coolingSystem = True
                elif accessory == "cleaningKit":
                        self.cleaningKit = True
                elif accessory == "extensionCable":
                        self.extensionCable = True

        def RemoveAccessory(self, accessory: str):
                """
                This method removes an accessory from the arcade machine.
                
                Args:
                accessory (str): The name of the accessory to be removed.
                
                Returns:
                None.
                """
                
                if accessory == "screenProtector":
                        self.screenProtector = False
                elif accessory == "drinksHolder":
                        self.drinksHolder = False
                elif accessory == "ledLights":
                        self.ledLights = False
                elif accessory == "coolingSystem":
                        self.coolingSystem = False
                elif accessory == "cleaningKit":
                        self.cleaningKit = False
                elif accessory == "extensionCable":
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
                
        
        