#!/bin/env python3

import sys
import re
import json

def fill_template(txt, _start=r"\$\$", _end=r"\$\$", **kwargs):
    for key in kwargs:
        txt = re.sub(_start + f'{key}' + _end, kwargs[key], txt)

    return txt


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print(sys.argv[0], "<configuration>")
        exit()

    with open(sys.argv[1], "r") as f:
        conf = json.loads(f.read())

    txt = sys.stdin.read()
    txt = fill_template(txt, _start=conf["start"], _end=conf["end"], **conf["keys"])

    print(txt, end="")
