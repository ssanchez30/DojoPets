from Ninja import Ninja
from Pet import Pet
from Snauzzer import Snauzzer

petExample=Pet("Stuart","Dog",["bring the ball", "play with the ball"])
ninjaExample=Ninja("Sergio", "Sanchez", petExample,["candies","icecream"],"SuperPerro")

ninjaExample.feed()
ninjaExample.walk()
ninjaExample.bathe()

petExample.petInfo()

snauzzerExample=Snauzzer("Nani","dog",["run","play"], 20,"white")
snauzzerExample.petInfo()