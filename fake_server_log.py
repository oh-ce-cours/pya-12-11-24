import random 
from pathlib import Path 

with open(Path(".") / ".." / "supports" / "medias" / "fonctiondAvancees" / "logs_apache.txt") as f:
    lines = f.readlines()
while True:
    