#!/usr/bin/python3

import sys
import signal

file_size = 0
count = 0
codes = {"200": 0, "301": 0, "400": 0, "401": 0,
         "403": 0, "404": 0, "405": 0, "500": 0}


def signal_handler(sig, frame):
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        nline = line.split()
        codes[nline[-2]] += 1
        file_size += int(nline[-1])
        count += 1

        if count == 10:
            print(f"File size: {file_size}")
            for key, value in codes.items():
                print(f"{key}: {value}")
            count = 0

except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {file_size}")
    for key, value in codes.items():
        print(f"{key}: {value}")
