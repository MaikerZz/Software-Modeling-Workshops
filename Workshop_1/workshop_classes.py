"""This module contains both abstract and concrete class definitions for an arcade machine seller program.

Author: Maiker Alejandro Hernández <mahernandeza@udistrital.edu.co>
        Joan Sebastián Durán Pradilla <Jsduranp@udistrital.edu.co>
        
this file is part of Workshops.

Arcade Machine Seller is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either versio 3 of the License, or (at your opinion) any later version.

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
                """////////////////Investigar como paso la lista de juegos a esta clase."""
                self.material = None
                self.gamesadded = []
        
        def  SelectMaterial (self, material: str):
                self.material = material

        def AddGame (self, game: str):
                if game in self.gamesadded:
                        print("El juego ya se encuentra en la lista")
                        input()
                else:
                        self.gamesadded.append(game)
                

class GameCatalog ():
        """
        It maintains and displays the list of available games.
        """
        
        def __init__(self):
                self.games = ["Space invaders", "Tetris", "Donkey Kong", "Street Fighter II", "Metal Slug",
                              "Ghosts 'n Goblins", "OutRun", "Double Dragon", "Asteroids", "Galaxian", "Frogger",
                              "Scramble", "Galaga", "Tempest", "Dragon's lair", "1942", "Kung-fu master"]
                
        def DisplayGames(self):
                counter = 0
                for game in self.games:
                        counter += 1
                        print(f"{counter}. {game}")
                        
        def FromIndextoGame(self, index: int) -> str:
                return self.games[index - 1]
        
class Customer ():
        """
        It represents the customer making the purchase. It stores the customer's basic personal information.
        """
        
        def __init__(self):
                self.name = None
                self.address = None
                
        def UpdateInformation (self, name: str, address: str):
                self.name = name
                self.address = address
                
class Utilities ():
        def ClearConsole(self):
                if os.name == 'nt':
                        os.system('cls')
                else:
                        os.system('clear')
                
        
        