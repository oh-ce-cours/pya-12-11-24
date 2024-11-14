import os
import time
import collections


def tail_F(file_name, size=5):
    line = ""
    sleep_sec = 0.1
    with open(file_name, encoding="utf8") as file:
        yield from collections.deque(file, size)
        while True:
            tmp = file.readline()
            if tmp is not None and tmp != "":
                line += tmp
                if line.endswith("\n"):
                    yield line
                    line = ""
            elif sleep_sec:
                time.sleep(sleep_sec)


for new_line in tail_F("./log.txt"):
    if not new_line:
        continue
    print(new_line.rstrip())
