#!/bin/bash

if test -f "scry.db"; then
    rm scry.db
fi

python3 parse.py 01.txt tempfall.json
