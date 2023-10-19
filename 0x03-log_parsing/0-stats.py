#!/usr/bin/python3

import sys
import signal
import re

file_size = 0
count = 0
codes = {"200": 0, "301": 0, "400": 0, "401": 0,
         "403": 0, "404": 0, "405": 0, "500": 0}
pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[[^\]]+\] "GET /projects/\d+ HTTP/1\.1" \d{3} \d+$'


def signal_handler(sig, frame):
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        if re.match(pattern, line):
            nline = line.split()
            codes[nline[-2]] += 1
            file_size += int(nline[-1])
            count += 1

            if count == 10:
                print(f"File size: {file_size}")
                for key, value in codes.items():
                    if value > 0:
                        print(f"{key}: {value}")
                count = 0

except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {file_size}")
    for key, value in codes.items():
        if value > 0:
            print(f"{key}: {value}")
