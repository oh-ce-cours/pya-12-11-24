def tail_F(some_file):
    first_call = True
    while True:
        try:
            with open(some_file) as input:
                if first_call:
                    input.seek(0, 2)
                    first_call = False
                latest_data = input.read()
                while True:
                    if "\n" not in latest_data:
                        latest_data += input.read()
                        if "\n" not in latest_data:
                            yield ""
                            if not os.path.isfile(some_file):
                                break
                            continue
                    latest_lines = latest_data.split("\n")
                    if latest_data[-1] != "\n":
                        latest_data = latest_lines[-1]
                    else:
                        latest_data = input.read()
                    for line in latest_lines[:-1]:
                        yield line + "\n"
        except IOError:
            yield ""
