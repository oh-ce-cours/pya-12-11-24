import random
from pathlib import Path
import time

with open(
    Path(__file__).parent
    / ".."
    / "supports"
    / "medias"
    / "fonctionsAvancees"
    / "logs_apache.txt",
    encoding="utf8",
) as f:
    lines = f.readlines()
while True:
    with open("./log.txt", "a", encoding="utf8") as f:
        f.write(random.choice(lines))
    time.sleep(random.random())
