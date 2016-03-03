"""
spaceshooter.py
Author: David Wilson
Credit: Space War Source Code (by Mr. Dennsion)

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, Sprite, ImageAsset, Frame

class starback(Sprite):
    starback_asset = ImageAsset("images/starfield.jpg")
    starback = Sprite(starback_asset, (0,0))
    
class ship1(Sprite):
    ship1_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(0,0,85,125))
    def __init__(self, position):
        super().__init__(ship1.ship1_asset, position)
        ship1 = Sprite(ship1_asset, (0,0))

myapp = App()
myapp.run()