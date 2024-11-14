import os
import time


def tail_F(some_file):
    first_call = True
    line = ""
    sleep_sec = 0.1
    with open(some_file, encoding="utf8") as file:
        while True:
            tmp = file.readline()
            if tmp is not None and tmp != "":
                line += tmp
                if line.endswith("\n"):
                    yield line
                    line = ""
            elif sleep_sec:
                time.sleep(sleep_sec)


for line in tail_F("./log.txt"):
    if not line:
        continue
    print(line)
