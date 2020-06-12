import os

mobs = os.path.abspath(os.path.abspath('.') + '/src/assets/entities/mobs.py')
from mobs import Monster

print(Monster)