import random
from pathlib import Path
import time

with open(
    Path(__file__)
    / ".."
    / "supports"
    / "medias"
    / "fonctionsAvancees"
    / "logs_apache.txt",
    encoding="utf8",
) as f:
    lines = f.readlines()
while True:
    print(random.choice(lines))
    time.sleep(random.random())
