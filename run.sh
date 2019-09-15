#!/bin/bash

if test -f "scry.db"; then
    rm scry.db
fi

python3 parse.py 01.txt scryfall-oracle-cards.json

# python3 garbage_functions.py 01.txt tempfall.json
