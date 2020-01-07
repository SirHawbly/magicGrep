#!/bin/bash

# if it exists, remove the database file.
if test -f "scry.db"; then
    rm scry.db
fi

# run the parse file with deck01 and scryfall.json
python3 parse.py 01.txt scryfall-oracle-cards.json

# python3 garbage_functions.py 01.txt tempfall.json
